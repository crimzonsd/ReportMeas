import pandas as pd
import psycopg2
import mysql.connector
import os
import configparser
from io import BytesIO
import traceback
import re

# Import spesifik error dari library database
from psycopg2 import Error as PostgresError
from mysql.connector import Error as MySQLError

# --- FUNGSI KONFIGURASI & KONEKSI ---
def get_kpi_config(tech: str, granularity: str, db_type: str):
    """
    Memuat modul konfigurasi dari subfolder yang benar (postgres/mysql).
    """
    db_type_folder = 'postgres' if db_type == 'postgres' else 'mysql'
    
    # --- PERBAIKAN BUG PENAMAAN 'busy_hour' vs 'bh' ---
    granularity_for_filename = granularity.lower()
    if granularity_for_filename == 'busy_hour':
        granularity_for_filename = 'bh'
        
    config_name = f"kpi{tech.lower()}_{granularity_for_filename}_config"
    try:
        import_path = f"datakpi.{db_type_folder}.{config_name}"
        config_module = __import__(import_path, fromlist=[config_name])
        
        tech_upper = tech.upper()
        table_name = getattr(config_module, f"TABLE_NAME_{tech_upper}")
        
        mandatory_cols_site = getattr(config_module, f"MANDATORY_COLUMNS_{tech_upper}_SITE", [])
        if not mandatory_cols_site:
            mandatory_cols_site = getattr(config_module, f"MANDATORY_COLUMNS_{tech_upper}", [])
            
        cell_specific_cols = getattr(config_module, f"CELL_SPECIFIC_MANDATORY_COLUMNS_{tech_upper}", [])
        optional_cols = getattr(config_module, f"OPTIONAL_COLUMNS_{tech_upper}", [])
        simple_map = getattr(config_module, f"SIMPLE_KPI_MAP_{tech_upper}", {})
        advanced_map = getattr(config_module, f"ADVANCED_KPI_MAP_{tech_upper}", {})
        
        return table_name, mandatory_cols_site, cell_specific_cols, optional_cols, simple_map, advanced_map
    except (ImportError, AttributeError) as e:
        print(f"Error loading config for {import_path}: {e}")
        raise ValueError(f"Konfigurasi untuk {db_type.upper()}/{tech.upper()}/{granularity.upper()} tidak ditemukan atau tidak lengkap.")

def get_config(db_type: str):
    """
    Membaca konfigurasi database dari Environment Variables (untuk deployment)
    atau dari config.ini (untuk testing lokal).
    """
    config = {}
    
    # Cek apakah berjalan di server (Render, dll. akan mengatur ENV VAR)
    # Kita cek satu variabel saja, misal POSTGRESQL_HOST
    if os.environ.get('POSTGRESQL_HOST'):
        # Mode Server: Baca dari Environment Variables
        if db_type == 'postgres':
            prefix = 'POSTGRESQL_'
        else:
            prefix = 'MYSQL_'
            
        config['host'] = os.environ.get(prefix + 'HOST')
        config['database'] = os.environ.get(prefix + 'DATABASE')
        config['user'] = os.environ.get(prefix + 'USER')
        config['password'] = os.environ.get(prefix + 'PASSWORD')
        config['port'] = os.environ.get(prefix + 'PORT', 5432 if db_type == 'postgres' else 3306)
        
        # Periksa apakah semua variabel penting ada
        if not all([config['host'], config['database'], config['user'], config['password']]):
            raise Exception(f"Environment variables untuk {db_type} tidak diatur lengkap di server.")
            
        return config
    else:
        # Mode Lokal: Baca dari config.ini
        parser = configparser.ConfigParser()
        if not os.path.exists('config.ini'):
            raise Exception("File config.ini tidak ditemukan untuk mode lokal.")
            
        parser.read('config.ini')
        section = 'POSTGRESQL' if db_type == 'postgres' else 'MYSQL'
        if section not in parser:
            raise Exception(f"Seksi [{section}] tidak ditemukan di config.ini")
        
        return dict(parser[section])

def check_db_connection(db_type: str):
    koneksi = None
    try:
        db_config = get_config(db_type)
        if db_type == "postgres":
            koneksi = psycopg2.connect(**db_config, connect_timeout=5)
        elif db_type == "mysql":
            koneksi = mysql.connector.connect(**db_config, connection_timeout=5)
        return True
    except (PostgresError, MySQLError, Exception) as error:
        return f"Gagal terhubung: {error}"
    finally:
        if koneksi:
            if db_type == "postgres": koneksi.close()
            elif db_type == "mysql" and koneksi.is_connected(): koneksi.close()

def get_kpi_info(tech: str, granularity: str, agg_level: str, db_type: str):
    """
    Menyiapkan daftar kolom mandatori secara dinamis berdasarkan level agregasi.
    """
    table_name, mandatory_cols_site, cell_specific_cols, optional_cols, simple_map, advanced_map = get_kpi_config(tech, granularity, db_type)
    
    # Tentukan date_column berdasarkan granularity
    if db_type == 'postgres':
        date_column = granularity.lower() # 'daily' -> 'date', 'weekly' -> 'week', 'monthly' -> 'month'
        if date_column == 'daily':
            date_column = 'date'
    else: # mysql
        if granularity in ['daily', 'weekly', 'monthly']:
            date_column = 'Date'
        else:  # hourly, busy_hour
            date_column = 'Date_Hour'
    
    # Inisialisasi mandatory_cols berdasarkan level
    if agg_level == 'cell':
        mandatory_cols = mandatory_cols_site.copy() + cell_specific_cols
    elif agg_level == 'site':
        mandatory_cols = mandatory_cols_site.copy()
    elif agg_level == 'nop':
        mandatory_cols = [date_column, 'Branch_name']
    elif agg_level == 'kabupaten':
        mandatory_cols = [date_column, 'Kabupaten']
    elif agg_level == 'balnus':
        mandatory_cols = [date_column]
    else:
        mandatory_cols = mandatory_cols_site.copy()
    
    return optional_cols, simple_map, advanced_map, mandatory_cols

def _clean_alias_for_sql(alias_str: str) -> str:
    s = str(alias_str).strip()
    s = re.sub(r'[^a-zA-Z0-9\s_]', '', s)
    s = re.sub(r'\s+', '_', s).lower()
    return s if s else "kpi"

# --- FUNGSI PEMBANTU UNTUK QUERY BUILDER ---

def _build_select_clause(mode, selected_items, mandatory_cols, optional_cols, simple_kpi_map, advanced_kpi_map, q, agg_level):
    """Membangun klausa SELECT, rename_map, dan info KPI yang dipilih."""
    
    select_expressions = {}
    if agg_level in ['site', 'cell']:
        select_expressions = {col: f'{q}{col}{q}' for col in mandatory_cols}

    rename_map = {}
    selected_kpis_info = []

    kpi_source_map = simple_kpi_map if mode == 'simple' else advanced_kpi_map

    if mode == 'advanced':
        for item in selected_items:
            if item in optional_cols:
                if item not in mandatory_cols:
                    select_expressions[item] = f'{q}{item}{q}'

    for category, kpis in kpi_source_map.items():
        if mode == 'simple' and category not in selected_items: continue
        for db_expr, alias, agg_func in kpis:
            if mode == 'advanced' and alias not in selected_items: continue
            
            clean_alias = _clean_alias_for_sql(alias)
            selected_kpis_info.append({'db_expr': db_expr, 'alias': alias, 'agg_func': agg_func, 'clean_alias': clean_alias})
            rename_map[clean_alias] = alias
            
            # --- PERBAIKAN LOGIKA QUOTING SQL ---
            # Cek apakah ini rumus (mengandung operator dengan spasi)
            if re.search(r'\s[/\*\+\-]\s', db_expr):
                # Ini adalah RUMUS, misal: "Payload (MB) / 1024"
                expr_parts = re.split(r'(\s[/\*\+\-]\s)', db_expr) # Pisahkan berdasarkan operator
                quoted_parts = []
                for part in expr_parts:
                    part_stripped = part.strip()
                    if part_stripped in ['/', '*', '+', '-']:
                        quoted_parts.append(part) # Tambahkan operator (dgn spasi)
                    elif part_stripped.isnumeric() or (part_stripped.replace('.','',1).isdigit()):
                        quoted_parts.append(part) # Tambahkan angka
                    elif part_stripped:
                        quoted_parts.append(f'{q}{part_stripped}{q}') # Kutip nama kolom
                db_expr_quoted = f"({''.join(quoted_parts)})"
            else:
                # Ini adalah NAMA KOLOM TUNGGAL, misal: "Radio Network Availability Rate (%)"
                db_expr_quoted = f"{q}{db_expr}{q}"
            # --- AKHIR PERBAIKAN ---

            select_expressions[clean_alias] = f'{db_expr_quoted} AS {q}{clean_alias}{q}'

    if not selected_kpis_info and not any(item in optional_cols for item in selected_items if mode == 'advanced'):
        raise ValueError("❌ Harap pilih setidaknya satu KPI atau Kolom DeskriptIF.")

    final_select_parts = [expr for expr in select_expressions.values() if expr]
    return ", ".join(final_select_parts), rename_map, selected_kpis_info


def _build_where_clause(db_type, date_column, site_id_col, where_conditions, q, agg_level):
    """Membangun klausa WHERE dan daftar parameter untuk query."""
    site_ids_input = where_conditions.get('site_ids', '').strip()
    site_list = [site.strip().upper() for site in site_ids_input.split(',') if site.strip()]
    
    params = [where_conditions['start_date'], where_conditions['end_date']]
    
    # Tentukan prefix tabel (a.) untuk kolom tanggal
    date_col_prefixed = f'a.{q}{date_column}{q}'
    where_clause = f'WHERE {date_col_prefixed} BETWEEN %s AND %s'
    
    if agg_level in ['site', 'cell'] and site_list:
        site_id_col_prefixed = f'a.{q}{site_id_col}{q}' # Tambahkan prefix 'a.'
        if db_type == 'mysql':
            placeholders = ', '.join(['%s'] * len(site_list))
            where_clause += f' AND {site_id_col_prefixed} IN ({placeholders})'
            params.extend(site_list)
        else: # postgres
            where_clause += f' AND {site_id_col_prefixed} IN %s'
            params.append(tuple(site_list))
            
    return where_clause, params

def _format_dataframe(df, rename_map, mandatory_cols, optional_cols, selected_items, selected_kpis_info, mode):
    """Mengganti nama dan mengurutkan kolom pada DataFrame final."""
    if rename_map:
        df.rename(columns=rename_map, inplace=True)
    
    final_ordered_columns = mandatory_cols.copy()
    if mode == 'advanced':
        final_ordered_columns.extend([item for item in selected_items if item in optional_cols])
    final_ordered_columns.extend([kpi['alias'] for kpi in selected_kpis_info])
    
    final_ordered_columns = [col for col in final_ordered_columns if col in df.columns]
    
    return df[final_ordered_columns]

def _build_regional_query(db_type, agg_level, table_name, date_column, select_clause, where_clause, q):
    """Membangun query untuk level regional tanpa duplicate columns"""
    
    regional_tables = {
        'nop': 'kabupaten_list',
        'kabupaten': 'kabupaten_list',
        'balnus': 'kabupaten_list'
    }
    
    target_table = regional_tables.get(agg_level)
    
    if not target_table:
        raise ValueError(f"Level agregasi {agg_level} tidak didukung")
    
    site_id_col_main = 'siteid' if db_type == 'mysql' else 'site_id'
    site_id_col_ref = 'SiteID' if db_type == 'mysql' else 'siteid' 
    
    if agg_level == 'nop':
        base_query = f"""
            SELECT a.{q}{date_column}{q} as {q}{date_column}{q}, b.{q}Branch_name{q} as {q}Branch_name{q}, {select_clause}
            FROM {table_name} a
            JOIN {target_table} b ON a.{q}{site_id_col_main}{q} = b.{q}{site_id_col_ref}{q}
            {where_clause}
        """
    elif agg_level == 'kabupaten':
        base_query = f"""
            SELECT a.{q}{date_column}{q} as {q}{date_column}{q}, b.{q}Kabupaten{q} as {q}Kabupaten{q}, {select_clause}
            FROM {table_name} a
            JOIN {target_table} b ON a.{q}{site_id_col_main}{q} = b.{q}{site_id_col_ref}{q}
            {where_clause}
        """
    elif agg_level == 'balnus':
        base_query = f"""
            SELECT a.{q}{date_column}{q} as {q}{date_column}{q}, 'BALNUS' as {q}Region{q}, {select_clause}
            FROM {table_name} a
            JOIN {target_table} b ON a.{q}{site_id_col_main}{q} = b.{q}{site_id_col_ref}{q}
            {where_clause}
        """
    else:
        base_query = f"SELECT {select_clause} FROM {table_name} a {where_clause}"
    
    return base_query

# --- FUNGSI UTAMA PEMBUATAN LAPORAN (REFACTORED) ---
def generate_dynamic_report_for_download(db_type, tech, granularity, agg_level, selected_items, mode, where_conditions):
    koneksi = None
    try:
        table_name, mandatory_cols_site, cell_specific_cols, optional_cols, simple_kpi_map, advanced_kpi_map = get_kpi_config(tech, granularity, db_type)
        
        if db_type == 'postgres':
            date_column = granularity.lower() 
            if date_column == 'daily':
                date_column = 'date'
        else: # mysql
            if granularity in ['daily', 'weekly', 'monthly']:
                date_column = 'Date'
            else:  # hourly, busy_hour
                date_column = 'Date_Hour'
        
        if agg_level == 'cell':
            mandatory_cols = mandatory_cols_site.copy() + cell_specific_cols
        elif agg_level == 'site':
            mandatory_cols = mandatory_cols_site.copy()
        elif agg_level == 'nop':
            mandatory_cols = [date_column, 'Branch_name']
        elif agg_level == 'kabupaten':
            mandatory_cols = [date_column, 'Kabupaten']
        elif agg_level == 'balnus':
            mandatory_cols = [date_column, 'Region'] 
        else:
            mandatory_cols = mandatory_cols_site.copy()

        q = '"' if db_type == 'postgres' else '`'
        
        select_clause, rename_map, selected_kpis_info = _build_select_clause(
            mode, selected_items, mandatory_cols, optional_cols, simple_kpi_map, advanced_kpi_map, q, agg_level
        )

        site_id_col = 'siteid' if db_type == 'mysql' else 'site_id'
        where_clause, params = _build_where_clause(
            db_type, date_column, site_id_col, where_conditions, q, agg_level
        )

        db_config = get_config(db_type)
        koneksi = psycopg2.connect(**db_config) if db_type == "postgres" else mysql.connector.connect(**db_config)
        
        if agg_level in ['nop', 'kabupaten', 'balnus']:
            base_query = _build_regional_query(db_type, agg_level, table_name, date_column, select_clause, where_clause, q)
        else:
            base_query = f"SELECT {select_clause} FROM {table_name} a {where_clause}"

        if agg_level == 'site':
            group_by_cols = mandatory_cols_site
            select_expressions = [f'{q}{col}{q}' for col in group_by_cols]
            for kpi in selected_kpis_info:
                select_expressions.append(f"{kpi['agg_func']}({q}{kpi['clean_alias']}{q}) AS {q}{kpi['clean_alias']}{q}")
            
            group_by_clause = ', '.join([f'{q}{col}{q}' for col in group_by_cols])
            query_sql = f"SELECT {', '.join(select_expressions)} FROM ({base_query}) AS cell_data GROUP BY {group_by_clause}"

        elif agg_level in ['nop', 'kabupaten', 'balnus']:
            if agg_level == 'nop':
                group_by_cols = [date_column, 'Branch_name']
            elif agg_level == 'kabupaten':
                group_by_cols = [date_column, 'Kabupaten']
            elif agg_level == 'balnus':
                group_by_cols = [date_column, 'Region'] 
            
            select_expressions = [f'{q}{col}{q}' for col in group_by_cols]
            for kpi in selected_kpis_info:
                select_expressions.append(f"{kpi['agg_func']}({q}{kpi['clean_alias']}{q}) AS {q}{kpi['clean_alias']}{q}")
            
            group_by_clause = ', '.join([f'{q}{col}{q}' for col in group_by_cols])
            query_sql = f"SELECT {', '.join(select_expressions)} FROM ({base_query}) AS regional_data GROUP BY {group_by_clause}"

        else:
            query_sql = base_query

        if agg_level in ['cell', 'site']:
            orderby_clause = f'ORDER BY {q}{date_column}{q}, {q}{site_id_col}{q}'
            cell_id_col = 'LocalCell Id' if db_type == 'mysql' else 'ci'
            if agg_level == 'cell' and cell_id_col in mandatory_cols:
                orderby_clause += f', {q}{cell_id_col}{q}'
        elif agg_level == 'nop':
            orderby_clause = f'ORDER BY {q}{date_column}{q}, {q}Branch_name{q}'
        elif agg_level == 'kabupaten':
            orderby_clause = f'ORDER BY {q}{date_column}{q}, {q}Kabupaten{q}'
        elif agg_level == 'balnus':
            orderby_clause = f'ORDER BY {q}{date_column}{q}, {q}Region{q}'
        else:
            orderby_clause = f'ORDER BY {q}{date_column}{q}'
        
        query_sql += f" {orderby_clause};"

        df_laporan = pd.read_sql_query(query_sql, koneksi, params=params)

        if df_laporan.empty:
            return {"status": "warning", "message": "⚠️ Tidak ada data yang ditemukan untuk kriteria yang dipilih."}
        
        df_laporan = _format_dataframe(df_laporan, rename_map, mandatory_cols, optional_cols, selected_items, selected_kpis_info, mode)

        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df_laporan.to_excel(writer, index=False, sheet_name='Report')
        excel_data = output.getvalue()

        site_ids_input = where_conditions.get('site_ids', '').strip()
        site_list = [site.strip().upper() for site in site_ids_input.split(',') if site.strip()]
        
        if len(site_list) > 3:
            site_identifier = f"grupSiteid_{len(site_list)}sites"
        elif site_list:
            site_identifier = '_'.join(site_list)
        else:
            site_identifier = 'ALL_SITES'
        
        if agg_level != 'site' and agg_level != 'cell':
            site_identifier = 'REGIONAL'

        site_identifier = re.sub(r'[<>:"/\\|?*]', '_', site_identifier)
        
        if len(site_identifier) > 50:
            site_identifier = site_identifier[:47] + "..."
        
        start_date_str = str(where_conditions['start_date'])
        end_date_str = str(where_conditions['end_date'])

        file_name = f"{tech}_{granularity.upper()}_{agg_level.upper()}_{mode.upper()}_{site_identifier}_{start_date_str.split(' ')[0]}_to_{end_date_str.split(' ')[0]}.xlsx"
        
        display_query = ""
        if koneksi and db_type == "postgres":
            display_query = koneksi.cursor().mogrify(query_sql, params).decode('utf-8', 'ignore')
        else:
            temp_query = query_sql
            for p in params:
                temp_query = temp_query.replace('%s', f"'{p}'", 1)
            display_query = temp_query
        
        return {"status": "success", "excel_data": excel_data, "file_name": file_name, "query": display_query, "message": "Laporan berhasil dibuat dan siap diunduh."}

    except ValueError as e:
        return {"status": "error", "message": f"❌ Error Konfigurasi atau Input: {e}"}
    except (PostgresError, MySQLError) as db_error:
        print(traceback.format_exc())
        return {"status": "error", "message": f"❌ Terjadi kesalahan pada database: {db_error}"}
    except Exception as general_error:
        print(traceback.format_exc())
        return {"status": "error", "message": f"❌ Terjadi kesalahan tidak terduga di backend: {general_error}"}
    finally:
        if koneksi:
            if db_type == 'postgres': koneksi.close()
            elif db_type == 'mysql' and koneksi.is_connected(): koneksi.close()