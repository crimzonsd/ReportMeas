# --- NAMA TABEL DATABASE ---
TABLE_NAME_4G = "region_balinusra.ran_cell_4g_month_balinusra"

# --- DEFINISI KOLOM ---
# Struktur disamakan dengan daily/weekly, namun kolom waktu adalah 'month'
# Kolom dasar yang selalu digunakan (basisnya adalah Site Level)
MANDATORY_COLUMNS_4G_SITE = ['month', 'site_id', 'site_name', 'enodeb_id', 'enodeb_name']

# Kolom tambahan HANYA untuk Cell Level
CELL_SPECIFIC_MANDATORY_COLUMNS_4G = ['cell_name', 'ci']

# --- DEFINISI KOLOM OPSIONAL (DISAMAKAN DENGAN DAILY/WEEKLY) ---
OPTIONAL_COLUMNS_4G = [
    'vendor', 'tac', 'ne_id', 'region', 'sales_region', 'band', 'type', 'sector', 'site_sign', 'bts_sign', 
    'cell_sign', 'site', 'bts', 'bts_sign_nqm', 'bts_nqm', 'longitude_fix', 'latitude_fix', 'longlat_fix_source', 'azimuth', 
    'horizontal_beamwidth', 'vertical_beamwidth', 'mc_class', 'cluster_name', 'sub_name', 'branch_name', 'id_desa', 'desa', 
    'id_kecamatan', 'kecamatan', 'id_kabupaten', 'kabupaten', 'province', 'priority_city', 'trueconex_scope', 'poi_name', 
    'poi_type_l1', 'poi_key', 'poi_flag', 'gogreen_category', 'bandwidth', 'poi_bbc_class', 'bbc_grouping_cities', 
    'bbc_class', 'trueconex_class', 'area', 'ip_source', 'bandtype', 'sector_id', 'flexible_bandwidth', 'bandcarrier', 
    'month_updated', 'week_updated', 'lac_ci_flag', 'longlat_invalid', 'cluster_invalid', 'filename', 'etilt', 'mtilt', 
    'height', 'trueconex_priority', 'on_service', 'service_level', 'class_city', 'poi_2020', 'priority_list_city', 
    'frequency', 'departement', 'technical_area', 'tower_provider_name', 'prime_zone', 'prime_poi', 'prime_route', 
    'poi_2020_type', 'region_new'
]

# --- DAFTAR KPI UNTUK 4G MONTHLY (SIMPLE MODE - DISAMAKAN DENGAN DAILY/WEEKLY) ---
SIMPLE_KPI_MAP_4G = {
    "Accessibility": [
        ("call_setup_success_rate", "Call Setup Success Rate (%)", "AVG"),
        ("rrc_setup_success_rate", "RRC Success Rate (%)", "AVG"),
        ("e_rab_setup_success_rate", "E-RAB Setup Success Rate (%)", "AVG")
    ],
    "Retainability": [
        ("service_drop_rate_excluding_mme", "Service Drop Rate (%)", "AVG")
    ],
    "CSFB": [
        ("csfb_preparation_success_rate", "CSFB Preparation Success Rate (%)", "AVG")
    ],
    "Mobility": [
        ("intra_frequency_handover_out_success_rate", "Intra-Frequency Handover Out SR (%)", "AVG"),
        ("inter_frequency_handover_out_success_rate", "Inter-Frequency Handover Out SR (%)", "AVG")
    ],
    "Traffic": [
        ("dl_traffic_volume_mbyte / 1024", "Downlink Traffic Volume (GB)", "SUM"),
        ("ul_traffic_volume_mbyte / 1024", "Uplink Traffic Volume (GB)", "SUM"),
        ("total_traffic_volume_mbyte / 1024", "Total Payload (GB)", "SUM")
    ],
    "Users": [
        ("rrc_avg_user_number", "Average User Number", "AVG"),
        ("active_user_ue_rrc_connected_avg", "Active User", "AVG"),
        ("rrc_max_user_number", "Total Users (Max)", "MAX")
    ],
    "Integrity": [
        ("cell_downlink_throughput", "Cell Downlink Average Throughput (Mbps)", "AVG"),
        ("cell_uplink_throughput", "Cell Uplink Average Throughput (Mbps)", "AVG"),
        ("user_downlink_throughput", "User Downlink Average Throughput (Mbps)", "AVG"),
        ("user_uplink_throughput", "User Uplink Average Throughput (Mbps)", "AVG")
    ],
    "Availability": [
        ("radio_network_availability_rate", "Radio Network Availability Rate (%)", "AVG")
    ],
    "Interference": [
        ("non_bh_interference", "Average UL Interference (dBm)", "AVG")
    ],
    "CQI": [
        ("average_cqi_rate", "CQI", "AVG")
    ],
    "SE": [
        ("se_prb_used_dl", "SE Value", "AVG")
    ],
    "MCS": [
        ("mcs_16qam_percent", "Average DL MCS (16QAM %)", "AVG")
    ],
    "Rank Ind": [
        ("rank_indicator_2", "Rank 2 (Samples)", "SUM")
    ],
    "IBLER": [
        ("ul_packet_loss_rate_qci_1", "DL IBLER (UL Packet Loss QCI1)", "AVG")
    ],
    "PRB": [
        ("dl_resource_block_utilizing_rate", "DL RB Utilization (%)", "AVG"),
        ("ul_resource_block_utilizing_rate", "UL RB Utilization (%)", "AVG")
    ]
}

# --- DAFTAR KPI LENGKAP UNTUK 4G MONTHLY (ADVANCED MODE - DISAMAKAN DENGAN DAILY/WEEKLY) ---
ADVANCED_KPI_MAP_4G = {
    "Raw Accessibility": [
        ("rrc_setup_success_rate", "RRC Setup SR (%)", "AVG"),
        ("numerator_rrc_setup_success", "Num RRC Setup Success", "SUM"), 
        ("denumerator_rrc_setup_success", "Denum RRC Setup Success", "SUM"),
        ("e_rab_setup_success_rate", "ERAB Setup SR (%)", "AVG"),
        ("numerator_e_rab_setup_success_rate", "Num ERAB Setup Success", "SUM"), 
        ("denumerator_e_rab_setup_success_rate", "Denum ERAB Setup Success", "SUM"),
        ("call_setup_success_rate", "Call Setup SR (%)", "AVG"),
        ("numerator_call_setup_success_rate", "Num Call Setup Success", "SUM"), 
        ("denumerator_call_setup_success_rate", "Denum Call Setup Success", "SUM"),
        ("success_rate_s1", "S1 Success Rate (%)", "AVG"),
        ("numerator_s1", "Num S1 Success", "SUM"), 
        ("denumerator_s1", "Denum S1 Success", "SUM")
    ],
    "Raw Retainability": [
        ("service_drop_rate_excluding_mme", "Service Drop Rate (exc MME) (%)", "AVG"),
        ("numerator_service_drop_excluding_mme", "Num Service Drop (exc MME)", "SUM"), 
        ("denumerator_service_drop_excluding_mme", "Denum Service Drop (exc MME)", "SUM"),
        ("service_drop_rate_including_mme", "Service Drop Rate (inc MME) (%)", "AVG"),
        ("numerator_service_drop_rate_including_mme", "Num Service Drop (inc MME)", "SUM"), 
        ("denumerator_service_drop_rate_including_mme", "Denum Service Drop (inc MME)", "SUM")
    ],
    "Raw Mobility": [
        ("intra_frequency_handover_out_success_rate", "Intra Freq HO SR (%)", "AVG"),
        ("numerator_intra_frequency_handover_out_success_rate", "Num Intra Freq HO", "SUM"), 
        ("denumerator_intra_frequency_handover_out_success_rate", "Denum Intra Freq HO", "SUM"),
        ("inter_frequency_handover_out_success_rate", "Inter Freq HO SR (%)", "AVG"),
        ("num_inter_frequency_handover_out_success_rate", "Num Inter Freq HO", "SUM"), 
        ("denum_inter_frequency_handover_out_success_rate", "Denum Inter Freq HO", "SUM"),
        ("lte_wcdma_redirection_success_rate", "LTE to WCDMA Redir SR (%)", "AVG"),
        ("numerator_lte_wcdma_redirection_success_rate", "Num LTE to WCDMA Redir", "SUM"), 
        ("denumerator_lte_wcdma_redirection_success_rate", "Denum LTE to WCDMA Redir", "SUM"),
        ("lte_geran_redirect_sr", "LTE to GERAN Redir SR (%)", "AVG"),
        ("numerator_lte_geran_redirection_success_rate", "Num LTE to GERAN Redir", "SUM"), 
        ("denumerator_lte_geran_redirection_success_rate", "Denum LTE to GERAN Redir", "SUM"),
        ("iratho", "IRAT HO SR (%)", "AVG"),
        ("numerator_iratho", "Num IRAT HO", "SUM"), 
        ("denumerator_iratho", "Denum IRAT HO", "SUM")
    ],
    "Raw Traffic & User": [
        ("total_traffic_volume_mbyte", "Total Payload (MB)", "SUM"),
        ("dl_traffic_volume_mbyte", "DL Payload (MB)", "SUM"),
        ("ul_traffic_volume_mbyte", "UL Payload (MB)", "SUM"),
        ("max_total_traffic_volume_mbyte", "Max Total Payload (MB)", "MAX"),
        ("min_total_traffic_volume_mbyte", "Min Total Payload (MB)", "MIN")
    ],
    "Raw User": [
        ("rrc_avg_user_number", "Avg RRC User", "AVG"),
        ("rrc_max_user_number", "Max RRC User", "MAX"),
        ("min_rrc_avg_user_number", "Min Avg RRC User", "MIN"),
        ("min_rrc_max_user_number", "Min Max RRC User", "MIN"),
        ("active_user_ue_rrc_connected_avg", "Avg Active User", "AVG"),
        ("active_user_ue_rrc_connected_max", "Max Active User", "MAX"),
        ("active_user_dl_data_in_buffer_avg", "Avg Active User DL Buffer", "AVG"),
        ("active_user_dl_data_in_buffer_max", "Max Active User DL Buffer", "MAX"),
        ("active_user_ul_data_in_buffer_avg", "Avg Active User UL Buffer", "AVG"),
        ("active_user_ul_data_in_buffer_max", "Max Active User UL Buffer", "MAX")
    ],
    "Raw Throughput": [
        ("cell_downlink_throughput", "Cell DL Tput (kbps)", "AVG"),
        ("numerator_cell_downlink_throughput", "Num Cell DL Tput", "SUM"), 
        ("denumerator_cell_downlink_throughput", "Denum Cell DL Tput", "SUM"),
        ("cell_uplink_throughput", "Cell UL Tput (kbps)", "AVG"),
        ("numerator_cell_uplink_throughput", "Num Cell UL Tput", "SUM"), 
        ("denumerator_cell_uplink_throughput", "Denum Cell UL Tput", "SUM"),
        ("user_downlink_throughput", "User DL Tput (kbps)", "AVG"),
        ("numerator_user_downlink_throughput", "Num User DL Tput", "SUM"), 
        ("denumerator_user_downlink_throughput", "Denum User DL Tput", "SUM"),
        ("user_uplink_throughput", "User UL Tput (kbps)", "AVG"),
        ("numerator_user_uplink_throughput", "Num User UL Tput", "SUM"), 
        ("denumerator_user_uplink_throughput", "Denum User UL Tput", "SUM"),
        ("cell_dl_dimensioning_throughput", "Cell DL Dimensioning Tput (kbps)", "AVG"),
        ("cell_ul_dimensioning_throughput", "Cell UL Dimensioning Tput (kbps)", "AVG"),
        ("total_dimensioning_throughput", "Total Dimensioning Tput (kbps)", "AVG"),
        ("max_dimensioning_throughput", "Max Dimensioning Tput (kbps)", "MAX")
    ],
    "Raw Availability": [
        ("radio_network_availability_rate", "Radio Network Availability (%)", "AVG"),
        ("numerator_radio_network_availability_rate", "Num Radio Network Availability", "SUM"),
        ("denumerator_radio_network_availability_rate", "Denum Radio Network Availability", "SUM")
    ],
    "Raw PRB": [
        ("dl_resource_block_utilizing_rate", "DL PRB Utilization (%)", "AVG"),
        ("numerator_dl_resource_block_utilizing_rate", "Num DL PRB Util", "SUM"),
        ("denumerator_dl_resource_block_utilizing_rate", "Denum DL PRB Util", "SUM"),
        ("ul_resource_block_utilizing_rate", "UL PRB Utilization (%)", "AVG"),
        ("numerator_ul_resource_block_utilizing_rate", "Num UL PRB Util", "SUM"),
        ("denumerator_ul_resource_block_utilizing_rate", "Denum UL PRB Util", "SUM"),
        ("max_resource_block_utilizing_rate", "Max PRB Utilization (%)", "MAX"),
        ("min_dl_resource_block_utilization_rate", "Min DL PRB Util (%)", "MIN"),
        ("min_ul_resource_block_utilization_rate", "Min UL PRB Util (%)", "MIN"),
        ("prb_dl_available", "DL PRB Available", "SUM"),
        ("average_prb_usage_dl", "Avg PRB Usage DL", "AVG"),
        ("avg_prb_usage_ul", "Avg PRB Usage UL", "AVG")
    ],
    "Raw CSFB": [
        ("csfb_preparation_success_rate", "CSFB Prep SR (%)", "AVG"),
        ("numerator_csfb_preparation_success_rate", "Num CSFB Prep Success", "SUM"),
        ("denumerator_csfb_preparation_success_rate", "Denum CSFB Prep Success", "SUM"),
        ("no_redirection_requests_lte_utran_csfb", "No. Redir Req LTE-UTRAN CSFB", "SUM"),
        ("no_redirection_requests_lte_gsm_csfb", "No. Redir Req LTE-GSM CSFB", "SUM")
    ],
    "Raw VoLTE": [
        ("volte_traffic_erl", "VoLTE Traffic (Erl)", "SUM"),
        ("volte_cssr_rate", "VoLTE CSSR (%)", "AVG"),
        ("volte_cssr_num", "Num VoLTE CSSR", "SUM"),
        ("volte_cssr_denum", "Denum VoLTE CSSR", "SUM"),
        ("volte_erab_ssr_rate", "VoLTE ERAB SR (%)", "AVG"),
        ("volte_erab_ssr_num", "Num VoLTE ERAB SR", "SUM"),
        ("volte_erab_ssr_denum", "Denum VoLTE ERAB SR", "SUM"),
        ("volte_call_dr_rate", "VoLTE Call Drop Rate (%)", "AVG"),
        ("volte_call_dr_num", "Num VoLTE Call Drop", "SUM"),
        ("volte_call_dr_denum", "Denum VoLTE Call Drop", "SUM"),
        ("volte_call_dr_mme_rate", "VoLTE Call Drop Rate (MME) (%)", "AVG"),
        ("volte_call_dr_mme_num", "Num VoLTE Call Drop (MME)", "SUM"),
        ("volte_call_dr_mme_denum", "Denum VoLTE Call Drop (MME)", "SUM"),
        ("volte_intra_rat_out_inter_fho_succ_rate", "VoLTE Inter-F HO SR (%)", "AVG"),
        ("volte_intra_rat_out_intra_fho_succ_rate", "VoLTE Intra-F HO SR (%)", "AVG"),
        ("srvcc_sr_inter_rat_e2w_rate", "SRVCC to WCDMA SR (%)", "AVG"),
        ("srvcc_sr_inter_rat_e2w_num", "Num SRVCC to WCDMA", "SUM"),
        ("srvcc_sr_inter_rat_e2w_denum", "Denum SRVCC to WCDMA", "SUM"),
        ("srvcc_sr_inter_rat_e2g_rate", "SRVCC to GERAN SR (%)", "AVG"),
        ("srvcc_sr_inter_rat_e2g_num", "Num SRVCC to GERAN", "SUM"),
        ("srvcc_sr_inter_rat_e2g_denum", "Denum SRVCC to GERAN", "SUM"),
        ("vqi_voice_quality_excellent_good_calls_to_all_calls_rate", "VQI Good Calls Rate (%)", "AVG"),
        ("vqi_voice_quality_excellent_good_calls_to_all_calls_num", "Num VQI Good Calls", "SUM"),
        ("vqi_voice_quality_excellent_good_calls_to_all_calls_denum", "Denum VQI Good Calls", "SUM"),
        ("vqi_awr_wb_excellent_good_calls_to_all_calls_rate", "VQI AWR WB Good Calls Rate (%)", "AVG"),
        ("vqi_awr_wb_excellent_good_calls_to_all_calls_num", "Num VQI AWR WB Good Calls", "SUM"),
        ("vqi_awr_wb_excellent_good_calls_to_all_calls_denum", "Denum VQI AWR WB Good Calls", "SUM"),
        ("avg_e2e_vqi", "Avg E2E VQI", "AVG")
    ],
    "Packet Loss": [
        ("ul_packet_loss_rate_qci_1", "UL Packet Loss QCI1", "AVG"),
        ("ul_packet_loss_rate_qci_1_num", "Num UL Packet Loss QCI1", "SUM"),
        ("ul_packet_loss_rate_qci_1_denum", "Denum UL Packet Loss QCI1", "SUM"),
        ("dl_packet_loss_rate_qci_1", "DL Packet Loss QCI1", "AVG"),
        ("dl_packet_loss_rate_qci_1_num", "Num DL Packet Loss QCI1", "SUM"),
        ("dl_packet_loss_rate_qci_1_denum", "Denum DL Packet Loss QCI1", "SUM")
    ],
    "Packet Delay": [
        ("dl_packet_delay_time_qci_1", "DL Packet Delay QCI1 (ms)", "AVG"),
        ("dl_packet_delay_time_qci_1_num", "Num DL Packet Delay QCI1", "SUM"),
        ("dl_packet_delay_time_qci_1_denum", "Denum DL Packet Delay QCI1", "SUM")
    ],
    "TA Distribution": [
        ("total_ta", "Total TA Samples", "SUM"), 
        ("ta_index0", "TA Index 0", "SUM"), ("ta_index1", "TA Index 1", "SUM"), ("ta_index2", "TA Index 2", "SUM"), 
        ("ta_index3", "TA Index 3", "SUM"), ("ta_index4", "TA Index 4", "SUM"), ("ta_index5", "TA Index 5", "SUM"), 
        ("ta_index6", "TA Index 6", "SUM"), ("ta_index7", "TA Index 7", "SUM"), ("ta_index8", "TA Index 8", "SUM"), 
        ("ta_index9", "TA Index 9", "SUM"), ("ta_index10", "TA Index 10", "SUM"), ("ta_index11", "TA Index 11", "SUM"), 
        ("ta_index12", "TA Index 12", "SUM"), ("ta_index13", "TA Index 13", "SUM"), ("ta_index14", "TA Index 14", "SUM"),
        ("ta_index15", "TA Index 15", "SUM"), ("ta_index16", "TA Index 16", "SUM"), ("ta_index17", "TA Index 17", "SUM"),
        ("ta_index18", "TA Index 18", "SUM"), ("ta_index19", "TA Index 19", "SUM"), ("ta_index20", "TA Index 20", "SUM"),
        ("ta_index0_ratio", "TA Idx0 Ratio (%)", "AVG"), ("ta_index1_ratio", "TA Idx1 Ratio (%)", "AVG"),
        ("ta_index2_ratio", "TA Idx2 Ratio (%)", "AVG"), ("ta_index3_ratio", "TA Idx3 Ratio (%)", "AVG"),
        ("ta_index4_ratio", "TA Idx4 Ratio (%)", "AVG"), ("ta_index5_ratio", "TA Idx5 Ratio (%)", "AVG"),
        ("ta_index6_ratio", "TA Idx6 Ratio (%)", "AVG"), ("ta_index7_ratio", "TA Idx7 Ratio (%)", "AVG"),
        ("ta_index8_ratio", "TA Idx8 Ratio (%)", "AVG"), ("ta_index9_ratio", "TA Idx9 Ratio (%)", "AVG"),
        ("ta_index10_ratio", "TA Idx10 Ratio (%)", "AVG"), ("ta_index11_ratio", "TA Idx11 Ratio (%)", "AVG"),
        ("ta_index12_ratio", "TA Idx12 Ratio (%)", "AVG"), ("ta_index13_ratio", "TA Idx13 Ratio (%)", "AVG"), 
        ("ta_index14_ratio", "TA Idx14 Ratio (%)", "AVG"), ("ta_index15_ratio", "TA Idx15 Ratio (%)", "AVG"), 
        ("ta_index16_ratio", "TA Idx16 Ratio (%)", "AVG"), ("ta_index17_ratio", "TA Idx17 Ratio (%)", "AVG"),
        ("ta_index18_ratio", "TA Idx18 Ratio (%)", "AVG"), ("ta_index19_ratio", "TA Idx19 Ratio (%)", "AVG"), 
        ("ta_index20_ratio", "TA Idx20 Ratio (%)", "AVG")
    ],
    "CQI": [
        ("average_cqi_rate", "Average CQI", "AVG"),
        ("good_cqi_rate", "Good CQI Rate (%)", "AVG"),
        ("cqi_dist_denum", "CQI Dist Denum", "SUM"),
        ("cqi_0", "CQI 0", "SUM"), ("cqi_1", "CQI 1", "SUM"), ("cqi_2", "CQI 2", "SUM"), ("cqi_3", "CQI 3", "SUM"),
        ("cqi_4", "CQI 4", "SUM"), ("cqi_5", "CQI 5", "SUM"), ("cqi_6", "CQI 6", "SUM"), ("cqi_7", "CQI 7", "SUM"),
        ("cqi_8", "CQI 8", "SUM"), ("cqi_9", "CQI 9", "SUM"), ("cqi_10", "CQI 10", "SUM"), ("cqi_11", "CQI 11", "SUM"),
        ("cqi_12", "CQI 12", "SUM"), ("cqi_13", "CQI 13", "SUM"), ("cqi_14", "CQI 14", "SUM"), ("cqi_15", "CQI 15", "SUM")
    ],
    "MCS" : [
        ("mcs_0", "MCS 0", "SUM"), ("mcs_1", "MCS 1", "SUM"), ("mcs_2", "MCS 2", "SUM"), ("mcs_3", "MCS 3", "SUM"),
        ("mcs_4", "MCS 4", "SUM"), ("mcs_5", "MCS 5", "SUM"), ("mcs_6", "MCS 6", "SUM"), ("mcs_7", "MCS 7", "SUM"),
        ("mcs_8", "MCS 8", "SUM"), ("mcs_9", "MCS 9", "SUM"), ("mcs_10", "MCS 10", "SUM"), ("mcs_11", "MCS 11", "SUM"),
        ("mcs_12", "MCS 12", "SUM"), ("mcs_13", "MCS 13", "SUM"), ("mcs_14", "MCS 14", "SUM"), ("mcs_15", "MCS 15", "SUM"),
        ("mcs_16", "MCS 16", "SUM"), ("mcs_17", "MCS 17", "SUM"), ("mcs_18", "MCS 18", "SUM"), ("mcs_19", "MCS 19", "SUM"),
        ("mcs_20", "MCS 20", "SUM"), ("mcs_21", "MCS 21", "SUM"), ("mcs_22", "MCS 22", "SUM"), ("mcs_23", "MCS 23", "SUM"),
        ("mcs_24", "MCS 24", "SUM"), ("mcs_25", "MCS 25", "SUM"), ("mcs_26", "MCS 26", "SUM"), ("mcs_27", "MCS 27", "SUM"),
        ("mcs_28", "MCS 28", "SUM"), ("mcs_29", "MCS 29", "SUM"), ("mcs_30", "MCS 30", "SUM"), ("mcs_31", "MCS 31", "SUM"),
        ("mcs_qpsk_percent", "MCS QPSK Pct (%)", "AVG"),
        ("mcs_16qam_percent", "MCS 16QAM Pct (%)", "AVG"),
        ("mcs_64qam_percent", "MCS 64QAM Pct (%)", "AVG")
    ],
    "Rank Distribution" : [
        ("rank_indicator_1", "Rank Indicator 1", "SUM"),
        ("rank_indicator_2", "Rank Indicator 2", "SUM"),
        ("rank_indicator_3", "Rank Indicator 3", "SUM"),
        ("rank_indicator_4", "Rank Indicator 4", "SUM"),
        ("mimo_spatial_rank_1", "MIMO Spatial Rank 1", "SUM"),
        ("mimo_spatial_rank_2", "MIMO Spatial Rank 2", "SUM")
    ],
    "Busy Hour (BH) Metrics": [
        ("bh_rrc_avg_user_number", "BH Avg RRC User", "AVG"),
        ("bh_rrc_max_user_number", "BH Max RRC User", "MAX"),
        ("bh_dl_resource_block_utilizing_rate", "BH DL PRB Util (%)", "AVG"),
        ("bh_ul_resource_block_utilizing_rate", "BH UL PRB Util (%)", "AVG"),
        ("bh_max_resource_block_utilizing_rate", "BH Max PRB Util (%)", "MAX"),
        ("bh_cell_downlink_throughput", "BH Cell DL Tput (kbps)", "AVG"),
        ("bh_cell_uplink_throughput", "BH Cell UL Tput (kbps)", "AVG"),
        ("bh_user_downlink_throughput", "BH User DL Tput (kbps)", "AVG"),
        ("bh_user_uplink_throughput", "BH User UL Tput (kbps)", "AVG"),
        ("bh_paging_number_from_s1", "BH Paging Number from S1", "AVG"),
        ("bh_active_user_dl_data_in_buffer_max", "BH Max Active User DL Buffer", "MAX"),
        ("bh_active_user_ul_data_in_buffer_max", "BH Max Active User UL Buffer", "MAX"),
        ("bh_active_user_dl_data_in_buffer_avg", "BH Avg Active User DL Buffer", "AVG"),
        ("bh_active_user_ul_data_in_buffer_avg", "BH Avg Active User UL Buffer", "AVG"),
        ("bh_active_user_ue_rrc_connected_max", "BH Max Active User", "MAX"),
        ("bh_active_user_ue_rrc_connected_avg", "BH Avg Active User", "AVG"),
        ("bh_max_total_traffic_volume_mbyte", "BH Max Total Payload (MB)", "MAX"),
        ("bh_total_usage_ul_average_mbps", "BH Total Usage UL Avg (Mbps)", "AVG"),
        ("bh_total_usage_dl_average_mbps", "BH Total Usage DL Avg (Mbps)", "AVG"),
        ("bh_total_usage_ul_maximum_mbps", "BH Total Usage UL Max (Mbps)", "MAX"),
        ("bh_total_usage_dl_maximum_mbps", "BH Total Usage DL Max (Mbps)", "MAX"),
        ("bh_s1_usage_ul_average_mbps", "BH S1 Usage UL Avg (Mbps)", "AVG"),
        ("bh_s1_usage_dl_average_mbps", "BH S1 Usage DL Avg (Mbps)", "AVG"),
        ("bh_s1_usage_ul_maximum_mbps", "BH S1 Usage UL Max (Mbps)", "MAX"),
        ("bh_s1_usage_dl_maximum_mbps", "BH S1 Usage DL Max (Mbps)", "MAX"),
        ("bh_x2_usage_ul_average_mbps", "BH X2 Usage UL Avg (Mbps)", "AVG"),
        ("bh_x2_usage_dl_average_mbps", "BH X2 Usage DL Avg (Mbps)", "AVG"),
        ("bh_x2_usage_ul_maximum_mbps", "BH X2 Usage UL Max (Mbps)", "MAX"),
        ("bh_x2_usage_dl_maximum_mbps", "BH X2 Usage DL Max (Mbps)", "MAX")
    ],
    "Usage Metrics (Mbps)": [
        ("total_usage_ul_average_mbps", "Total Usage UL Avg (Mbps)", "AVG"),
        ("total_usage_dl_average_mbps", "Total Usage DL Avg (Mbps)", "AVG"),
        ("total_usage_ul_maximum_mbps", "Total Usage UL Max (Mbps)", "MAX"),
        ("total_usage_dl_maximum_mbps", "Total Usage DL Max (Mbps)", "MAX"),
        ("s1_usage_ul_average_mbps", "S1 Usage UL Avg (Mbps)", "AVG"),
        ("s1_usage_dl_average_mbps", "S1 Usage DL Avg (Mbps)", "AVG"),
        ("s1_usage_ul_maximum_mbps", "S1 Usage UL Max (Mbps)", "MAX"),
        ("s1_usage_dl_maximum_mbps", "S1 Usage DL Max (Mbps)", "MAX"),
        ("x2_usage_ul_average_mbps", "X2 Usage UL Avg (Mbps)", "AVG"),
        ("x2_usage_dl_average_mbps", "X2 Usage DL Avg (Mbps)", "AVG"),
        ("x2_usage_ul_maximum_mbps", "X2 Usage UL Max (Mbps)", "MAX"),
        ("x2_usage_dl_maximum_mbps", "X2 Usage DL Max (Mbps)", "MAX")
    ],
    "Other KPI": [
        ("pdcch_agg8", "PDCCH AGG8", "AVG"),
        ("average_cqi_lom_rate", "Avg CQI LOM Rate", "AVG")
    ]
}

