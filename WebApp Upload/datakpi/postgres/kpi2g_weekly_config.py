# --- NAMA TABEL DATABASE ---
# Catatan: Nama tabel diasumsikan mengikuti pola. Sesuaikan jika perlu.
TABLE_NAME_2G = "region_balinusra.ran_cell_2g_week_balinusra_live"

# --- DEFINISI KOLOM ---
# Struktur disamakan dengan daily, namun 'date' diganti 'week'
MANDATORY_COLUMNS_2G_SITE = ['week', 'site_id', 'site_name', 'bsc_name']
CELL_SPECIFIC_MANDATORY_COLUMNS_2G = ['cell_name', 'ci']

# --- DEFINISI KOLOM OPSIONAL (DISAMAKAN DENGAN DAILY) ---
OPTIONAL_COLUMNS_2G = [
    'vendor', 'lac', 'ne_id', 'region', 'sales_region', 'cgipre', 'cgipost', 'band', 'type', 'bts_type', 'sector', 
    'site_sign', 'bts_sign', 'cell_sign', 'site', 'bts', 'bts_sign_nqm', 'bts_nqm', 'longitude_fix', 'latitude_fix', 
    'longlat_fix_source', 'longitude_tmp', 'latitude_tmp', 'longlat_tmp_source', 'azimuth', 'horizontal_beamwidth', 
    'vertical_beamwidth', 'mc_class', 'cluster_name', 'sub_name', 'branch_name', 'id_desa', 'desa', 'id_kecamatan', 
    'kecamatan', 'id_kabupaten', 'kabupaten', 'province', 'priority_city', 'trueconex_scope', 'month_updated', 'week_updated', 
    'lac_ci_flag', 'longlat_invalid', 'cluster_invalid', 'poi_name', 'poi_type_l1', 'poi_key', 'poi_flag', 'gogreen_category', 
    'poi_bbc_class', 'bbc_grouping_cities', 'bbc_class', 'trueconex_class', 'area', 'ip_source', 'sector_id', 'bandcarrier', 
    'bandwidth', 'filename', 'etilt', 'mtilt', 'height', 'trueconex_priority', 'on_service', 'service_level', 'class_city', 
    'poi_2020', 'priority_list_city', 'frequency', 'departement', 'technical_area', 'tower_provider_name', 'prime_zone', 
    'prime_poi', 'prime_route', 'poi_2020_type', 'bandtype', 'flexible_bandwidth', 'region_new'
]

# --- DAFTAR KPI UNTUK 2G WEEKLY (SIMPLE MODE - DISAMAKAN DENGAN DAILY) ---
SIMPLE_KPI_MAP_2G = {
    "Accessibility": [
        ("cssr_voice_rate", "CSSR Voice (%)", "AVG"),
        ("tch_blocking_rate", "TCH Blocking Rate (%)", "AVG"),
        ("sdcch_blocking_rate", "SDCCH Blocking Rate (%)", "AVG"),
    ],
    "Retainability": [
        ("tch_drop_rate_rate", "TCH Drop Rate (%)", "AVG"),
    ],
    "Traffic & Payload": [
        ("tch_traffic_sum", "TCH Traffic (Erl)", "SUM"),
        ("total_payload_mbyte", "Total Payload (MB)", "SUM"),
    ],
    "Throughput": [
        ("total_thr_kbps", "Total Throughput (kbps)", "AVG"),
        ("edge_thp_kbps", "EDGE Throughput (kbps)", "AVG"),
    ],
    "Availability": [
        ("availability_rate", "Cell Availability Rate (%)", "AVG"),
        ("tch_availability_rate", "TCH Availability Rate (%)", "AVG"),
    ],
    "Mobility": [
        ("hosr", "Handover SR (%)", "AVG"),
    ]
}

# --- DAFTAR KPI LENGKAP UNTUK 2G WEEKLY (ADVANCED MODE - DISAMAKAN DENGAN DAILY) ---
ADVANCED_KPI_MAP_2G = {
    "Raw Accessibility (Voice)": [
        ("cssr_voice_rate", "CSSR Voice Rate (%)", "AVG"),
        ("cssr_voice_num", "Num CSSR Voice", "SUM"),
        ("cssr_voice_denum", "Denum CSSR Voice", "SUM"),
        ("ccsr_voice_rate", "CCSR Voice Rate (%)", "AVG"),
        ("ccsr_voice_num", "Num CCSR Voice", "SUM"),
        ("ccsr_voice_denum", "Denum CCSR Voice", "SUM"),
        ("sd_setup_sr_rate", "SDCCH Setup SR (%)", "AVG"),
        ("sd_setup_sr_num", "Num SDCCH Setup SR", "SUM"),
        ("sd_setup_sr_denum", "Denum SDCCH Setup SR", "SUM"),
        ("tch_blocking", "TCH Blocking Rate (%)", "AVG"),
        ("tch_blocking_num", "Num TCH Blocking", "SUM"),
        ("tch_blocking_denum", "Denum TCH Blocking", "SUM"),
        ("sd_blocking", "SDCCH Blocking Rate (SD)", "AVG"),
        ("sd_blocking_num", "Num SDCCH Blocking (SD)", "SUM"),
        ("sd_blocking_denum", "Denum SDCCH Blocking (SD)", "SUM"),
        ("sdcch_blocking_rate", "SDCCH Blocking Rate", "AVG"),
        ("sdcch_blocking_num", "Num SDCCH Blocking", "SUM"),
        ("sdcch_blocking_denum", "Denum SDCCH Blocking", "SUM"),
    ],
    "Raw Retainability (Voice)": [
        ("tch_drop_rate_rate", "TCH Drop Rate (%)", "AVG"),
        ("tch_drop_rate_num", "Num TCH Drop", "SUM"),
        ("tch_drop_rate_denum", "Denum TCH Drop", "SUM"),
    ],
    "Raw Mobility (Handover)": [
        ("hosr", "Handover Success Rate (%)", "AVG"),
        ("hosr_num", "Num HOSR", "SUM"),
        ("hosr_denum", "Denum HOSR", "SUM"),
    ],
    "Raw Accessibility (Data)": [
        ("tbf_dl_est_sr_rate", "DL TBF Establish SR (%)", "AVG"),
        ("tbf_dl_est_sr_num", "Num DL TBF Establish SR", "SUM"),
        ("tbf_dl_est_sr_denum", "Denum DL TBF Establish SR", "SUM"),
        ("tbf_ul_est_sr", "UL TBF Establish SR (%)", "AVG"),
        ("tbf_ul_est_sr_num", "Num UL TBF Establish SR", "SUM"),
        ("tbf_ul_est_sr_denum", "Denum UL TBF Establish SR", "SUM"),
        ("tbf_complete", "TBF Completion Rate (%)", "AVG"),
        ("tbf_complete_num", "Num TBF Complete", "SUM"),
        ("tbf_complete_denum", "Denum TBF Complete", "SUM"),
    ],
    "Raw Traffic (Voice)": [
        ("tch_traffic_sum", "TCH Traffic Total (Erl)", "SUM"),
        ("tch_traffic_max", "TCH Traffic Max (Erl)", "MAX"),
        ("tch_traffic_fr_sum", "TCH Traffic FR Sum (Erl)", "SUM"),
        ("tch_traffic_fr_max", "TCH Traffic FR Max (Erl)", "MAX"),
        ("tch_traffic_hr_sum", "TCH Traffic HR Sum (Erl)", "SUM"),
        ("tch_traffic_hr_max", "TCH Traffic HR Max (Erl)", "MAX"),
        ("sdcch_traffic", "SDCCH Traffic (Erl)", "AVG"),
    ],
    "Raw Payload (Data)": [
        ("total_payload_mbyte", "Total Payload (MB)", "SUM"),
        ("total_payload_dl_mbyte", "DL Payload (MB)", "SUM"),
        ("total_payload_ul_mbyte", "UL Payload (MB)", "SUM"),
        ("gprs_payload_mbyte", "GPRS Payload (MB)", "SUM"),
        ("gprs_payload_dl_mbyte", "GPRS DL Payload (MB)", "SUM"),
        ("gprs_payload_ul_mbyte", "GPRS UL Payload (MB)", "SUM"),
        ("edge_payload_mbyte", "EDGE Payload (MB)", "SUM"),
        ("edge_payload_dl_mbyte", "EDGE DL Payload (MB)", "SUM"),
        ("edge_payload_ul_mbyte", "EDGE UL Payload (MB)", "SUM"),
        ("max_2g_payload_mbyte", "Max Total Payload (MB)", "MAX"),
    ],
    "Raw Throughput (Data)": [
        ("total_thr_kbps", "Total Throughput (kbps)", "AVG"),
        ("total_thr_dl_kbps", "Total DL Throughput (kbps)", "AVG"),
        ("total_thr_ul_kbps", "Total UL Throughput (kbps)", "AVG"),
        ("edge_thp_kbps", "EDGE Throughput (kbps)", "AVG"),
        ("edge_dl_thp_kbps", "EDGE DL Throughput (kbps)", "AVG"),
        ("edge_ul_thp_kbps", "EDGE UL Throughput (kbps)", "AVG"),
        ("gprs_thp_kbps", "GPRS Throughput (kbps)", "AVG"),
        ("gprs_dl_thp_kbps", "GPRS DL Throughput (kbps)", "AVG"),
        ("gprs_ul_thp_kbps", "GPRS UL Throughput (kbps)", "AVG"),
    ],
    "Raw Availability & Utilization": [
        ("availability_rate", "Cell Availability Rate (%)", "AVG"),
        ("availability_num", "Num Cell Availability", "SUM"),
        ("availability_denum", "Denum Cell Availability", "SUM"),
        ("tch_availability_rate", "TCH Availability Rate (%)", "AVG"),
        ("tch_available", "TCH Available", "AVG"),
        ("tch_define", "TCH Defined", "AVG"),
        ("sdcch_availability_rate", "SDCCH Availability Rate (%)", "AVG"),
        ("sdcch_available", "SDCCH Available", "AVG"),
        ("sdcch_define", "SDCCH Defined", "AVG"),
        ("utilization_full_rate_tch_rate", "TCH FR Utilization (%)", "AVG"),
        ("hr_penetration_rate", "HR Penetration Rate (%)", "AVG"),
        ("utilization_sdcch_rate", "SDCCH Utilization (%)", "AVG"),
    ],
    "Raw Quality": [
        ("rx_qual_dl", "DL RX Quality", "AVG"),
        ("rx_qual_dl_num", "Num DL RX Quality", "SUM"),
        ("rx_qual_dl_denum", "Denum DL RX Quality", "SUM"),
        ("rx_qual_ul", "UL RX Quality", "AVG"),
        ("rx_qual_ul_num", "Num UL RX Quality", "SUM"),
        ("rx_qual_ul_denum", "Denum UL RX Quality", "SUM"),
        ("avg_evqi_dl", "Avg EVQI DL", "AVG"),
        ("avg_evqi_ul", "Avg EVQI UL", "AVG"),
    ],
    "Busy Hour (BH) Metrics": [
        ("bh_total_thr_kbps", "BH Total Throughput (kbps)", "AVG"),
        ("bh_edge_thp_kbps", "BH EDGE Throughput (kbps)", "AVG"),
        ("bh_gprs_thp_kbps", "BH GPRS Throughput (kbps)", "AVG"),
        ("bh_tch_traffic", "BH TCH Traffic (Erl)", "AVG"),
        ("bh_sdcch_traffic", "BH SDCCH Traffic (Erl)", "AVG"),
        ("bh_max_2g_payload_mbyte", "BH Max Payload (MB)", "MAX"),
    ]
}
