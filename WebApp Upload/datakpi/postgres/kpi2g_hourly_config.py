# --- NAMA TABEL DATABASE ---
TABLE_NAME_2G = "region_balinusra.ran_cell_2g_hour_balinusra" # <-- PENTING: GANTI DENGAN NAMA TABEL YANG BENAR

# --- DEFINISI KOLOM ---
MANDATORY_COLUMNS_2G = ['datetime', 'hour', 'site_id', 'site_name', 'bsc_name', 'ci']
CELL_SPECIFIC_MANDATORY_COLUMNS_2G = ['cell_name', 'ci']
OPTIONAL_COLUMNS_2G = [
    'dayofyear', 'date', 'vendor', 'cell_name', 'lac', 'ne_id', 'region', 'sales_region', 'cgipre', 'cgipost', 'band', 
    'type', 'bts_type', 'sector', 'sector_id', 'site_sign', 'bts_sign', 'cell_sign', 'site', 'bts', 'bts_sign_nqm', 
    'bts_nqm', 'longitude_fix', 'latitude_fix', 'longlat_fix_source', 'longitude_tmp', 'latitude_tmp', 'longlat_tmp_source', 
    'azimuth', 'horizontal_beamwidth', 'vertical_beamwidth', 'mc_class', 'cluster_name', 'sub_name', 'branch_name', 
    'id_desa', 'desa', 'id_kecamatan', 'kecamatan', 'id_kabupaten', 'kabupaten', 'province', 'priority_city', 
    'trueconex_scope', 'month_updated', 'week_updated', 'lac_ci_flag', 'longlat_invalid', 'cluster_invalid', 'poi_name', 
    'poi_type_l1', 'poi_key', 'poi_flag', 'gogreen_category', 'poi_bbc_class', 'bbc_grouping_cities', 'bbc_class', 
    'trueconex_class', 'area', 'ip_source', 'departement', 'technical_area', 'tower_provider_name', 'bandtype', 
    'frequency', 'poi_2020', 'poi_2020_type', 'flexible_bandwidth', 'region_new'
]

# --- DAFTAR KPI UNTUK 2G HOURLY (SIMPLE MODE) ---
SIMPLE_KPI_MAP_2G = {
    "Accessibility": [
        ("cssr_voice_rate", "CSSR Voice (%)", "AVG"),
        ("tch_blocking", "TCH Blocking Rate (%)", "AVG"),
        ("sdcch_blocking_rate", "SDCCH Blocking Rate (%)", "AVG"),
    ],
    "Retainability": [
        ("tch_drop_rate_rate", "TCH Drop Rate (%)", "AVG"),
    ],
    "Traffic": [
        ("tch_traffic", "TCH Traffic (Erl)", "SUM"),
        ("sms_traffic_erl", "SMS Traffic (Erl)", "SUM"),
        ("ussd_traffic_erl", "USSD Traffic (Erl)", "SUM"),
    ],
    "Data Payload & Throughput": [
        ("total_payload_mbyte", "Total Payload (MB)", "SUM"),
        ("total_thr_kbps", "Total Throughput (kbps)", "AVG"),
    ],
    "Availability": [
        ("availability_rate", "Cell Availability Rate (%)", "AVG"),
    ],
    "Quality": [
        ("mos_dl", "MOS DL", "AVG"),
    ]
}

# --- DAFTAR KPI LENGKAP UNTUK 2G HOURLY (ADVANCED MODE) ---
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
        ("sdcch_blocking_rate", "SDCCH Blocking Rate (%)", "AVG"),
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
    ],
    "Raw Traffic": [
        ("tch_traffic", "TCH Traffic (Erl)", "SUM"),
        ("tch_traffic_sum", "TCH Traffic Sum (Erl)", "SUM"),
        ("tch_traffic_max", "TCH Traffic Max (Erl)", "MAX"),
        ("tch_traffic_fr", "TCH Traffic FR (Erl)", "SUM"),
        ("tch_traffic_hr", "TCH Traffic HR (Erl)", "SUM"),
        ("sms_traffic_erl", "SMS Traffic (Erl)", "SUM"),
        ("ussd_traffic_erl", "USSD Traffic (Erl)", "SUM"),
        ("sdcch_traffic", "SDCCH Traffic (Erl)", "SUM"),
    ],
    "Raw Payload (Data)": [
        ("total_payload_mbyte", "Total Payload (MB)", "SUM"),
        ("total_payload_dl_mbyte", "DL Payload (MB)", "SUM"),
        ("total_payload_ul_mbyte", "UL Payload (MB)", "SUM"),
        ("gprs_payload_mbyte", "GPRS Payload (MB)", "SUM"),
        ("edge_payload_mbyte", "EDGE Payload (MB)", "SUM"),
        ("max_2g_payload_mbyte", "Max Total Payload (MB)", "MAX"),
    ],
    "Raw Throughput (Data)": [
        ("total_thr_kbps", "Total Throughput (kbps)", "AVG"),
        ("edge_thp_kbps", "EDGE Throughput (kbps)", "AVG"),
        ("gprs_thp_kbps", "GPRS Throughput (kbps)", "AVG"),
        ("average_throughput_of_downlink_gprs_rlc_kbps", "Avg GPRS DL RLC Tput (kbps)", "AVG"),
        ("average_throughput_of_downlink_egprs_rlc_kbps", "Avg EGPRS DL RLC Tput (kbps)", "AVG"),
    ],
    "Raw Availability & Utilization": [
        ("availability_rate", "Cell Availability Rate (%)", "AVG"),
        ("availability_num", "Num Cell Availability", "SUM"),
        ("availability_denum", "Denum Cell Availability", "SUM"),
        ("tch_availability_rate", "TCH Availability Rate (%)", "AVG"),
        ("tch_available", "TCH Available", "AVG"),
        ("tch_define", "TCH Defined", "AVG"),
        ("available_tchs", "TCHs Available (Sum)", "SUM"),
        ("sdcch_availability_rate", "SDCCH Availability Rate (%)", "AVG"),
        ("sdcch_available", "SDCCH Available", "AVG"),
        ("sdcch_define", "SDCCH Defined", "AVG"),
        ("utilization_full_rate_tch_rate", "TCH FR Utilization (%)", "AVG"),
        ("utilization_sdcch_rate", "SDCCH Utilization (%)", "AVG"),
        ("hr_penetration_rate", "HR Penetration Rate (%)", "AVG"),
    ],
    "Raw Quality (Voice & MOS)": [
        ("rx_qual_dl", "DL RX Quality", "AVG"),
        ("rx_qual_dl_num", "Num DL RX Quality", "SUM"),
        ("rx_qual_dl_denum", "Denum DL RX Quality", "SUM"),
        ("rx_qual_ul", "UL RX Quality", "AVG"),
        ("rx_qual_ul_num", "Num UL RX Quality", "SUM"),
        ("rx_qual_ul_denum", "Denum UL RX Quality", "SUM"),
        ("avg_evqi_dl", "Avg EVQI DL", "AVG"),
        ("avg_evqi_ul", "Avg EVQI UL", "AVG"),
        ("gsm_vqi_dl", "GSM VQI DL", "AVG"),
        ("gsm_vqi_dl_num", "Num GSM VQI DL", "SUM"),
        ("gsm_vqi_dl_denum", "Denum GSM VQI DL", "SUM"),
        ("gsm_vqi_ul", "GSM VQI UL", "AVG"),
        ("gsm_vqi_ul_num", "Num GSM VQI UL", "SUM"),
        ("gsm_vqi_ul_denum", "Denum GSM VQI UL", "SUM"),
        ("mos_dl", "MOS DL", "AVG"),
        ("mos_dl_num", "Num MOS DL", "SUM"),
        ("mos_dl_denum", "Denum MOS DL", "SUM"),
        ("mos_ul", "MOS UL", "AVG"),
        ("mos_ul_num", "Num MOS UL", "SUM"),
        ("mos_ul_denum", "Denum MOS UL", "SUM"),
    ],
    "Raw Users (Data)": [
        ("max_gprs_user", "Max GPRS Users", "MAX"),
        ("max_egprs_user", "Max EGPRS Users", "MAX"),
    ]
}