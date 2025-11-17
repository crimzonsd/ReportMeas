# --- NAMA TABEL DATABASE ---
# Catatan: Nama tabel ini diasumsikan mengikuti pola 4G. Silakan sesuaikan jika berbeda.
TABLE_NAME_5G = "region_balinusra.ran_cell_5g_week_balinusra_live"

# --- DEFINISI KOLOM 5G ---
# Struktur disamakan dengan daily, namun 'date' diganti 'week'
MANDATORY_COLUMNS_5G_SITE = ['week', 'site_id', 'site_name', 'enodeb_id', 'enodeb_name']
CELL_SPECIFIC_MANDATORY_COLUMNS_5G = ['cell_name', 'ci']

# --- DEFINISI KOLOM OPSIONAL (DISAMAKAN DENGAN DAILY) ---
OPTIONAL_COLUMNS_5G = [
    'vendor', 'tac', 'ne_id', 'region', 'sales_region', 'band', 'type', 'sector', 'site_sign', 'bts_sign', 
    'cell_sign', 'site', 'bts', 'bts_sign_nqm', 'bts_nqm', 'longitude_fix', 'latitude_fix', 'longlat_fix_source', 'azimuth', 
    'horizontal_beamwidth', 'vertical_beamwidth', 'mc_class', 'cluster_name', 'sub_name', 'branch_name', 'id_desa', 'desa', 
    'id_kecamatan', 'kecamatan', 'id_kabupaten', 'kabupaten', 'province', 'priority_city', 'trueconex_scope', 'poi_name', 
    'poi_type_l1', 'poi_key', 'poi_flag', 'gogreen_category', 'bandwidth', 'poi_bbc_class', 'bbc_grouping_cities', 
    'bbc_class', 'trueconex_class', 'area', 'ip_source', 'bandtype', 'sector_id', 'flag_uso', 'flexible_bandwidth', 
    'cell_name6', 'site_name6', 'bandcarrier', 'month_updated', 'week_updated', 'lac_ci_flag', 'longlat_invalid', 
    'cluster_invalid', 'filename', 'etilt', 'mtilt', 'height', 'trueconex_priority', 'on_service', 'service_level', 
    'class_city', 'poi_2020', 'priority_list_city', 'frequency', 'departement', 'technical_area', 'tower_provider_name', 
    'prime_zone', 'prime_poi', 'prime_route', 'poi_2020_type', 'region_new'
]

# --- DAFTAR KPI UNTUK 5G WEEKLY (SIMPLE MODE - DISAMAKAN DENGAN DAILY) ---
SIMPLE_KPI_MAP_5G = {
    "Accessibility": [
        ("nr_sn_setup_success_rate", "NR SN Setup SR (%)", "AVG"),
        ("nr_erab_setup_success_rate", "NR ERAB Setup SR (%)", "AVG"),
    ],
    "Retainability": [
        ("nr_retainability_rate", "NR Retainability Rate (%)", "AVG"),
    ],
    "Mobility": [
        ("nr_intra_handover_success_rate", "NR Intra-Freq HO SR (%)", "AVG"),
        ("nr_inter_handover_success_rate", "NR Inter-Freq HO SR (%)", "AVG"),
    ],
    "Traffic": [
        ("nr_payload_volume_gbyte", "Total Payload (GB)", "SUM"),
    ],
    "Users": [
        ("max_number_of_rrc_connected_users", "Max RRC Connected Users", "MAX"),
        ("nr_dl_active_user_avg", "Avg DL Active Users", "AVG"),
    ],
    "Integrity (Throughput)": [
        ("nr_user_throughput_dl_mbps_relactuserdl", "User DL Throughput (Mbps)", "AVG"),
        ("nr_cell_throughput_dl_mbps_relactuserdl", "Cell DL Throughput (Mbps)", "AVG"),
    ],
    "Availability": [
        ("nr_availability_rate", "NR Availability Rate (%)", "AVG"),
    ],
    "PRB": [
        ("nr_prb_utilization_dl_rate", "DL PRB Utilization (%)", "AVG"),
        ("nr_prb_utilization_ul_rate", "UL PRB Utilization (%)", "AVG"),
    ],
    "Quality (CQI)": [
        ("nr_average_cqi", "Average CQI", "AVG"),
    ]
}

# --- DAFTAR KPI LENGKAP UNTUK 5G WEEKLY (ADVANCED MODE - DISAMAKAN DENGAN DAILY) ---
ADVANCED_KPI_MAP_5G = {
    "Raw Accessibility": [
        ("nr_sn_setup_success_rate", "NR SN Setup SR (%)", "AVG"),
        ("nr_sn_setup_success_num", "Num NR SN Setup Success", "SUM"),
        ("nr_sn_setup_success_denum", "Denum NR SN Setup Success", "SUM"),
        ("nr_erab_setup_success_rate", "NR ERAB Setup SR (%)", "AVG"),
        ("nr_erab_setup_success_num", "Num NR ERAB Setup Success", "SUM"),
        ("nr_erab_setup_success_denum", "Denum NR ERAB Setup Success", "SUM"),
    ],
    "Raw Retainability": [
        ("nr_retainability_rate", "NR Retainability Rate (%)", "AVG"),
        ("nr_retainability_num", "Num NR Retainability", "SUM"),
        ("nr_retainability_denum", "Denum NR Retainability", "SUM"),
        ("lte_nr_retainability_all_rate", "LTE-NR Retainability (All) (%)", "AVG"),
        ("lte_nr_retainability_all_num", "Num LTE-NR Retainability (All)", "SUM"),
        ("lte_nr_retainability_all_denum", "Denum LTE-NR Retainability (All)", "SUM"),
        ("lte_nr_retainability_enb_only_rate", "LTE-NR Retainability (eNB) (%)", "AVG"),
        ("lte_nr_retainability_enb_only_num", "Num LTE-NR Retainability (eNB)", "SUM"),
        ("lte_nr_retainability_enb_only_denum", "Denum LTE-NR Retainability (eNB)", "SUM"),
    ],
    "Raw Throughput": [
        ("nr_user_throughput_dl_mbps_relactuserdl", "User DL Tput (Mbps)", "AVG"),
        ("nr_user_throughput_dl_mbps_num_relactuserdl", "Num User DL Tput", "SUM"),
        ("nr_user_throughput_dl_mbps_denum_relactuserdl", "Denum User DL Tput", "SUM"),
        ("nr_user_throughput_ul_mbps_relactuserdl", "User UL Tput (Mbps)", "AVG"),
        ("nr_user_throughput_ul_mbps_num_relactuserdl", "Num User UL Tput", "SUM"),
        ("nr_user_throughput_ul_mbps_denum_relactuserdl", "Denum User UL Tput", "SUM"),
        ("nr_cell_throughput_dl_mbps_relactuserdl", "Cell DL Tput (Mbps)", "AVG"),
        ("nr_cell_throughput_dl_mbps_num_relactuserdl", "Num Cell DL Tput", "SUM"),
        ("nr_cell_throughput_dl_mbps_denum_relactuserdl", "Denum Cell DL Tput", "SUM"),
        ("nr_cell_throughput_ul_mbps_relactuserdl", "Cell UL Tput (Mbps)", "AVG"),
        ("nr_cell_throughput_ul_mbps_num_relactuserdl", "Num Cell UL Tput", "SUM"),
        ("nr_cell_throughput_ul_mbps_denum_relactuserdl", "Denum Cell UL Tput", "SUM"),
        ("nr_cell_dl_dimensioning_throughput_mbps", "Cell DL Dimensioning Tput (Mbps)", "AVG"),
        ("nr_cell_ul_dimensioning_throughput_mbps", "Cell UL Dimensioning Tput (Mbps)", "AVG"),
        ("nr_total_dimensioning_throughput_mbps", "Total Dimensioning Tput (Mbps)", "AVG"),
        ("nr_max_dimensioning_throughput_mbps", "Max Dimensioning Tput (Mbps)", "MAX"),
    ],
    "Raw PRB": [
        ("nr_prb_utilization_dl_rate", "DL PRB Utilization (%)", "AVG"),
        ("nr_prb_utilization_dl_num", "Num DL PRB Util", "SUM"),
        ("nr_prb_utilization_dl_denum", "Denum DL PRB Util", "SUM"),
        ("nr_prb_utilization_ul_rate", "UL PRB Utilization (%)", "AVG"),
        ("nr_prb_utilization_ul_num", "Num UL PRB Util", "SUM"),
        ("nr_prb_utilization_ul_denum", "Denum UL PRB Util", "SUM"),
        ("nr_max_prb_utilization_rate", "Max PRB Util (%)", "MAX"),
        ("nr_prb_utilization_dl_rate_relactuserdl", "DL PRB Util (Rel Act User) (%)", "AVG"),
        ("nr_prb_utilization_dl_num_relactuserdl", "Num DL PRB Util (Rel Act User)", "SUM"),
        ("nr_prb_utilization_dl_denum_relactuserdl", "Denum DL PRB Util (Rel Act User)", "SUM"),
        ("nr_prb_utilization_ul_rate_relactuserdl", "UL PRB Util (Rel Act User) (%)", "AVG"),
        ("nr_prb_utilization_ul_num_relactuserdl", "Num UL PRB Util (Rel Act User)", "SUM"),
        ("nr_prb_utilization_ul_denum_relactuserdl", "Denum UL PRB Util (Rel Act User)", "SUM"),
        ("nr_max_prb_utilization_rate_relactuserdl", "Max PRB Util (Rel Act User) (%)", "MAX"),
        ("nr_prb_usage_dl_relactuserdl", "DL PRB Usage (Rel Act User)", "AVG"),
        ("nr_prb_usage_ul_relactuserdl", "UL PRB Usage (Rel Act User)", "AVG"),
    ],
    "Raw Mobility (Handover)": [
        ("nr_intra_handover_success_rate", "Intra-Freq HO SR (%)", "AVG"),
        ("nr_intra_handover_success_num", "Num Intra-Freq HO", "SUM"),
        ("nr_intra_handover_success_denum", "Denum Intra-Freq HO", "SUM"),
        ("nr_inter_handover_success_rate", "Inter-Freq HO SR (%)", "AVG"),
        ("nr_inter_handover_success_num", "Num Inter-Freq HO", "SUM"),
        ("nr_inter_handover_success_denum", "Denum Inter-Freq HO", "SUM"),
    ],
    "Raw Payload (Traffic)": [
        ("nr_payload_volume_gbyte", "Total Payload (GB)", "SUM"),
        ("nr_dl_payload_volume_gbyte", "DL Payload (GB)", "SUM"),
        ("nr_ul_payload_volume_gbyte", "UL Payload (GB)", "SUM"),
        ("nr_payload_max_gbyte", "Max Payload (GB)", "MAX"),
        ("nr_dl_payload_max_gbyte", "Max DL Payload (GB)", "MAX"),
        ("nr_ul_payload_max_gbyte", "Max UL Payload (GB)", "MAX"),
        ("nr_payload_max_gbyte_relactuserdl", "Max Payload (GB, Rel Act User)", "MAX"),
        ("nr_dl_payload_max_gbyte_relactuserdl", "Max DL Payload (GB, Rel Act User)", "MAX"),
        ("nr_ul_payload_max_gbyte_relactuserdl", "Max UL Payload (GB, Rel Act User)", "MAX"),
    ],
    "Raw Users": [
        ("active_user_number", "Active User Number", "AVG"),
        ("max_number_of_rrc_connected_users", "Max RRC Connected Users", "MAX"),
        ("average_number_of_rrc_connected_users", "Avg RRC Connected Users", "AVG"),
        ("nr_rrc_user_number", "NR RRC User Number", "AVG"),
        ("nr_dl_active_user_max", "Max DL Active Users", "MAX"),
        ("nr_ul_active_user_max", "Max UL Active Users", "MAX"),
        ("nr_dl_active_user_avg", "Avg DL Active Users", "AVG"),
        ("nr_ul_active_user_avg", "Avg UL Active Users", "AVG"),
    ],
    "Raw Quality (CQI, SE, Interference)": [
        ("nr_average_cqi", "Average CQI", "AVG"),
        ("nr_average_cqi_num", "Num Average CQI", "SUM"),
        ("nr_average_cqi_denum", "Denum Average CQI", "SUM"),
        ("nr_average_cqi_relactuserdl", "Average CQI (Rel Act User)", "AVG"),
        ("nr_average_cqi_num_relactuserdl", "Num Avg CQI (Rel Act User)", "SUM"),
        ("nr_average_cqi_denum_relactuserdl", "Denum Avg CQI (Rel Act User)", "SUM"),
        ("nr_average_cqi_64qam", "Avg CQI 64QAM", "AVG"),
        ("nr_average_cqi_64qam_num", "Num Avg CQI 64QAM", "SUM"),
        ("nr_average_cqi_64qam_denum", "Denum Avg CQI 64QAM", "SUM"),
        ("nr_average_cqi_256qam", "Avg CQI 256QAM", "AVG"),
        ("nr_average_cqi_256qam_num", "Num Avg CQI 256QAM", "SUM"),
        ("nr_average_cqi_256qam_denum", "Denum Avg CQI 256QAM", "SUM"),
        ("nr_uplink_interference_dbm", "UL Interference (dBm)", "AVG"),
        ("nr_se_prb_dl_bpsperhz_relactuserdl", "DL Spectral Efficiency (bps/Hz)", "AVG"),
        ("nr_se_prb_dl_bpsperhz_relactuserdl_num", "Num DL SE", "SUM"),
        ("nr_se_prb_dl_bpsperhz_relactuserdl_denum", "Denum DL SE", "SUM"),
    ],
    "Raw Latency & Packet Loss": [
        ("nr_latency_dl_ms", "DL Latency (ms)", "AVG"),
        ("nr_latency_dl_ms_num", "Num DL Latency", "SUM"),
        ("nr_latency_dl_ms_denum", "Denum DL Latency", "SUM"),
        ("nr_latency_ul_ms", "UL Latency (ms)", "AVG"),
        ("nr_latency_ul_ms_num", "Num UL Latency", "SUM"),
        ("nr_latency_ul_ms_denum", "Denum UL Latency", "SUM"),
        ("nr_packet_loss_rate", "Packet Loss Rate (%)", "AVG"),
        ("nr_packet_loss_num", "Num Packet Loss", "SUM"),
        ("nr_packet_loss_denum", "Denum Packet Loss", "SUM"),
    ],
    "Raw Availability": [
        ("nr_availability_rate", "NR Availability Rate (%)", "AVG"),
        ("nr_availability_num", "Num NR Availability", "SUM"),
        ("nr_availability_denum", "Denum NR Availability", "SUM"),
    ],
    "Raw TA Distribution": [
        ("nr_average_ta_meter", "Average TA (meter)", "AVG"),
        ("nr_average_ta_meter_num", "Num Average TA", "SUM"),
        ("nr_average_ta_meter_denum", "Denum Average TA", "SUM"),
        ("nr_ta_index_0", "TA Idx 0", "SUM"), ("nr_ta_index_1", "TA Idx 1", "SUM"), ("nr_ta_index_2", "TA Idx 2", "SUM"),
        ("nr_ta_index_3", "TA Idx 3", "SUM"), ("nr_ta_index_4", "TA Idx 4", "SUM"), ("nr_ta_index_5", "TA Idx 5", "SUM"),
        ("nr_ta_index_6", "TA Idx 6", "SUM"), ("nr_ta_index_7", "TA Idx 7", "SUM"), ("nr_ta_index_8", "TA Idx 8", "SUM"),
        ("nr_ta_index_9", "TA Idx 9", "SUM"), ("nr_ta_index_10", "TA Idx 10", "SUM"), ("nr_ta_index_11", "TA Idx 11", "SUM"),
        ("nr_ta_index_12", "TA Idx 12", "SUM"), ("nr_ta_index_13", "TA Idx 13", "SUM"), ("nr_ta_index_14", "TA Idx 14", "SUM"),
        ("nr_ta_index_15", "TA Idx 15", "SUM"), ("nr_ta_index_16", "TA Idx 16", "SUM"), ("nr_ta_index_17", "TA Idx 17", "SUM"),
        ("nr_ta_index_18", "TA Idx 18", "SUM"), ("nr_ta_index_19", "TA Idx 19", "SUM"), ("nr_ta_index_20", "TA Idx 20", "SUM"),
        ("nr_ta_index_21", "TA Idx 21", "SUM"), ("nr_ta_index_22", "TA Idx 22", "SUM"), ("nr_ta_index_23", "TA Idx 23", "SUM"),
    ],
    "Busy Hour (BH) Metrics": [
        ("bh_nr_dl_active_user_avg", "BH Avg DL Active User", "AVG"),
        ("bh_nr_ul_active_user_avg", "BH Avg UL Active User", "AVG"),
        ("bh_nr_dl_payload_max_gbyte", "BH Max DL Payload (GB)", "MAX"),
        ("bh_nr_ul_payload_max_gbyte", "BH Max UL Payload (GB)", "MAX"),
        ("bh_nr_payload_max_gbyte", "BH Max Total Payload (GB)", "MAX"),
        ("bh_nr_prb_utilization_dl_rate", "BH DL PRB Util Rate (%)", "AVG"),
        ("bh_nr_prb_utilization_ul_rate", "BH UL PRB Util Rate (%)", "AVG"),
        ("bh_nr_max_prb_utilization_rate", "BH Max PRB Util Rate (%)", "MAX"),
        ("bh_nr_rrc_user_number", "BH RRC User Number", "AVG"),
    ]
}

