# --- NAMA TABEL DATABASE ---
TABLE_NAME_4G = "4g_kpi_daily_ftp"
# --- DEFINISI KOLOM ---
# Kolom dasar yang selalu digunakan (basisnya adalah Site Level)
MANDATORY_COLUMNS_4G_SITE = ['Date', 'siteid', 'eNodeB Name', 'eNodeB Function Name']

# Kolom tambahan HANYA untuk Cell Level
CELL_SPECIFIC_MANDATORY_COLUMNS_4G = ['LocalCell Id', 'Cell Name', 'Cell FDD TDD Indication', 'Sector']

# --- KOLOM UNTUK LEVEL BARU ---
# Kolom untuk NOP Level - hanya Date dan Branch_name
NOP_LEVEL_COLUMNS_4G = ['Date', 'Branch_name']

# Kolom untuk Kabupaten Level - hanya Date dan Kabupaten
KABUPATEN_LEVEL_COLUMNS_4G = ['Date', 'Kabupaten']

# Kolom untuk Balnus Level - hanya Date
BALNUS_LEVEL_COLUMNS_4G = ['Date']

# --- DEFINISI KOLOM OPSIONAL ---
# Kolom deskriptif tambahan yang bisa dipilih
OPTIONAL_COLUMNS_4G = [
    'Downlink EARFCN', 'Downlink bandwidth', 'Physical cell ID', 'Tracking area code', 
    'eNodeB identity'
]

# --- DAFTAR KPI UNTUK 4G HOURLY (SIMPLE MODE) ---
SIMPLE_KPI_MAP_4G = {
    "Accessibility": [
        ("Call Setup Success Rate (%)", "Call Setup Success Rate (%)", "AVG"),
        ("RRC Success Rate (%)", "RRC Success Rate (%)", "AVG"),
        ("E-RAB Setup Success Rate (%)", "E-RAB Setup Success Rate (%)", "AVG")
    ],
    "Retainability": [
        ("Service Drop Rate (%)", "Service Drop Rate (%)", "AVG")
    ],
    "CSFB": [
        ("CSFB Preparation Success Rate (%)", "CSFB Preparation Success Rate (%)", "AVG")
    ],
    "Mobility": [
        ("Intra-Frequency Handover Out Success Rate (%)", "Intra-Frequency Handover Out SR (%)", "AVG"),
        ("Inter-Frequency Handover Out Success Rate (%)", "Inter-Frequency Handover Out SR (%)", "AVG")
    ],
    "Traffic": [
        ("Downlink Traffic Volume (MB)", "Downlink Traffic Volume (MB)", "SUM"),
        ("Uplink Traffic Volume (MB)", "Uplink Traffic Volume (MB)", "SUM"),
        ("Payload (MB)", "Total Payload (MB)", "SUM"),
        ("Payload (MB) / 1024", "Total Payload (GB)", "SUM")
    ],
    "Users": [
        ("Average User Number", "Average User Number", "AVG"),
        ("Avg_Active_User", "Active User", "AVG"),
        ("Max_RRC_Connected_User", "Total Users (Max)", "MAX")
    ],
    "Integrity": [
        ("Cell Downlink Average Throughput (Mbps)", "Cell Downlink Average Throughput (Mbps)", "AVG"),
        ("Cell Uplink Average Throughput (Mbps)", "Cell Uplink Average Throughput (Mbps)", "AVG"),
        ("User Downlink Average Throughput (Mbps)", "User Downlink Average Throughput (Mbps)", "AVG"),
        ("User Uplink Average Throughput (Mbps)", "User Uplink Average Throughput (Mbps)", "AVG")
    ],
    "Availability": [
        ("Radio Network Availability Rate (%)", "Radio Network Availability Rate (%)", "AVG")
    ],
    "Interference": [
        ("L.UL.Interference.Avg(dBm)", "Average UL Interference (dBm)", "AVG")
    ],
    "CQI": [
        ("cqiaverage_ro_hq", "CQI", "AVG")
    ],
    "SE": [
        ("SE", "SE Value", "AVG")
    ],
    "MCS": [
        ("DL_avg_MCS", "Average DL MCS", "AVG")
    ],
    "Rank Ind": [
        ("L.ChMeas.RI.Rank2", "Rank 2 (Samples)", "SUM")
    ],
    "IBLER": [
        ("DL IBLER %", "DL BLER (%)", "AVG")
    ],
    "PRB": [
        ("DL Resource Block Utilizing Rate (%)", "DL RB UTIL (%)", "AVG"),
        ("UL Resource Block Utilizing Rate (%)", "UL RB UTIL (%)", "AVG")
    ]
}

# --- DAFTAR KPI LENGKAP UNTUK 4G HOURLY (ADVANCED MODE) ---
ADVANCED_KPI_MAP_4G = {
    "Raw Accessibility": [
        ("RRC Success Rate (%)", "RRC Success Rate (%)", "AVG"),
        ("RRC Success Rate_Num", "Num RRC Success", "SUM"),
        ("RRC Success Rate_Denum", "Denum RRC Success", "SUM"),
        ("E-RAB Setup Success Rate (%)", "E-RAB Setup SR (%)", "AVG"),
        ("E-RAB Setup Success Rate_Num", "Num E-RAB Setup Success", "SUM"),
        ("E-RAB Setup Success Rate_Denum", "Denum E-RAB Setup Success", "SUM"),
        ("Call Setup Success Rate (%)", "Call Setup SR (%)", "AVG"),
        ("L.E-RAB.SuccEst", "Success E-RAB Establishments", "SUM"),
    ],
    "Raw Retainability": [
        ("Service Drop Rate (%)", "Service Drop Rate (%)", "AVG"),
        ("Service Drop Rate_Num", "Num Service Drop", "SUM"),
        ("Service Drop Rate_Denum", "Denum Service Drop", "SUM"),
        ("Service Drop Rate_New (%)", "Service Drop Rate (New) (%)", "AVG"),
        ("Service Drop Rate_New_Num", "Num Service Drop (New)", "SUM"),
        ("Service Drop Rate_New_Denum", "Denum Service Drop (New)", "SUM"),
    ],
    "Raw Mobility": [
        ("Intra-Frequency Handover Out Success Rate (%)", "Intra-Freq HO SR (%)", "AVG"),
        ("Intra-Frequency Handover Out Success Rate_Num", "Num Intra-Freq HO", "SUM"),
        ("Intra-Frequency Handover Out Success Rate_Denum", "Denum Intra-Freq HO", "SUM"),
        ("Intra-Frequency Handover In Succes Rate (%)", "Intra-Freq HO In SR (%)", "AVG"),
        ("Intra-Frequency Handover In Succes Rate_Num", "Num Intra-Freq HO In", "SUM"),
        ("Intra-Frequency Handover In Succes Rate_Denum", "Denum Intra-Freq HO In", "SUM"),
        ("Inter-Frequency Handover Out Success Rate (%)", "Inter-Freq HO SR (%)", "AVG"),
        ("Inter-Frequency Handover Out Success Rate_Num", "Num Inter-Freq HO", "SUM"),
        ("Inter-Frequency Handover Out Success Rate_Denum", "Denum Inter-Freq HO", "SUM"),
    ],
    "Raw CSFB & Redirection": [
        ("CSFB Preparation Success Rate (%)", "CSFB Preparation SR (%)", "AVG"),
        ("CSFB Preparation Success Rate_Num", "Num CSFB Preparation", "SUM"),
        ("CSFB Preparation Success Rate_Denum", "Denum CSFB Preparation", "SUM"),
        ("CSFB Execution Success Rate (%)", "CSFB Execution SR (%)", "AVG"),
        ("CSFB Execution Success Rate_Num", "Num CSFB Execution", "SUM"),
        ("CSFB Execution Success Rate_Denum", "Denum CSFB Execution", "SUM"),
        ("LTE to WCDMA Redirection Success Rate (%)", "LTE to WCDMA Redirection SR (%)", "AVG"),
        ("LTE to WCDMA Redirection Success Rate_Num", "Num LTE to WCDMA Redirection", "SUM"),
        ("LTE to WCDMA Redirection Success Rate_Denum", "Denum LTE to WCDMA Redirection", "SUM"),
        ("L.CSFB.E2W", "CSFB to WCDMA", "SUM"),
        ("L.CSFB.E2G", "CSFB to GERAN", "SUM"),
    ],
    "Raw Throughput": [
        ("Cell Downlink Average Throughput (Mbps)", "Cell DL Avg Tput (Mbps)", "AVG"),
        ("Cell Downlink Average Throughput_Num", "Num Cell DL Tput", "SUM"),
        ("Cell Downlink Average Throughput_Denum", "Denum Cell DL Tput", "SUM"),
        ("Cell Uplink Average Throughput (Mbps)", "Cell UL Avg Tput (Mbps)", "AVG"),
        ("Cell Uplink Average Throughput_Num", "Num Cell UL Tput", "SUM"),
        ("Cell Uplink Average Throughput_Denum", "Denum Cell UL Tput", "SUM"),
        ("User Downlink Average Throughput (Mbps)", "User DL Avg Tput (Mbps)", "AVG"),
        ("User Downlink Average Throughput_Num", "Num User DL Tput", "SUM"),
        ("User Downlink Average Throughput_Denum", "Denum User DL Tput", "SUM"),
        ("User Uplink Average Throughput (Mbps)", "User UL Avg Tput (Mbps)", "AVG"),
        ("User Uplink Average Throughput_Num", "Num User UL Tput", "SUM"),
        ("User Uplink Average Throughput_Denum", "Denum User UL Tput", "SUM"),
        ("CA User Throughput (Mbps)", "CA User Tput (Mbps)", "AVG"),
        ("CA User Throughput_Num", "Num CA User Tput", "SUM"),
        ("CA User Throughput_Denum", "Denum CA User Tput", "SUM"),
    ],
    "Raw Traffic": [
        ("Downlink Traffic Volume (MB)", "DL Traffic Volume (MB)", "SUM"),
        ("Uplink Traffic Volume (MB)", "UL Traffic Volume (MB)", "SUM"),
        ("Payload (MB)", "Total Payload (MB)", "SUM"),
        ("Payload (MB) / 1024", "Total Payload (GB)", "SUM"),
        ("Payload (MB) / 1024 / 1024", "Total Payload (TB)", "SUM"),
        ("DL CA Payload", "DL CA Payload", "SUM"),
    ],
    "Raw Users": [
        ("Average User Number", "Avg User Number", "AVG"),
        ("Max_RRC_Connected_User", "Max RRC Connected User", "MAX"),
        ("Avg_Active_User", "Avg Active User", "AVG"),
        ("Max_Active_User", "Max Active User", "MAX"),
        ("Max of Average User Number", "Max of Avg User Number", "MAX"),
        ("Maximum User Number", "Maximum User Number", "MAX"),
    ],
    "Raw PRB Utilization": [
        ("DL Resource Block Utilizing Rate (%)", "DL PRB Utilizing Rate (%)", "AVG"),
        ("PRB DL Util_New_Num", "Num DL PRB Util", "SUM"),
        ("PRB DL Util_New_Denum", "Denum DL PRB Util", "SUM"),
        ("UL Resource Block Utilizing Rate (%)", "UL PRB Utilizing Rate (%)", "AVG"),
        ("PRB UL Util_New_Num", "Num UL PRB Util", "SUM"),
        ("PRB UL Util_New_Denum", "Denum UL PRB Util", "SUM"),
        ("PUSCH Resource Block Utilizing Rate", "PUSCH RB Utilizing Rate (%)", "AVG"),
        ("PUSCH Resource Block Utilizing Rate_Num", "Num PUSCH RB Util", "SUM"),
        ("PUSCH Resource Block Utilizing Rate_Denum", "Denum PUSCH RB Util", "SUM"),
    ],
    "Raw Quality & Interference": [
        ("DL IBLER %", "DL BLER (%)", "AVG"),
        ("DL IBLER_NUM", "Num DL BLER", "SUM"),
        ("DL IBLER_DENUM", "Denum DL BLER", "SUM"),
        ("UL IBLER %", "UL BLER (%)", "AVG"),
        ("UL IBLER_NUM", "Num UL BLER", "SUM"),
        ("UL IBLER_DENUM", "Denum UL BLER", "SUM"),
        ("L.UL.Interference.Avg(dBm)", "UL Interference Avg (dBm)", "AVG"),
        ("cqiaverage_ro_hq", "Average CQI", "AVG"),
        ("cqiaveragenum1_ro_hq", "Num1 CQI", "SUM"),
        ("cqiaveragenum2_ro_hq", "Num2 CQI", "SUM"),
        ("cqiaveragedenum_ro_hq", "Denum CQI", "SUM"),
        ("CQI>=10", "CQI >= 10 (%)", "AVG"),
        ("CQI>=10_NUM", "Num CQI >= 10", "SUM"),
        ("CQI>=10_DENUM", "Denum CQI >= 10", "SUM"),
    ],
    "Raw TA Distribution": [
        ("L.TA.UE.Index0", "TA Index 0", "SUM"),
        ("L.TA.UE.Index1", "TA Index 1", "SUM"),
        ("L.TA.UE.Index2", "TA Index 2", "SUM"),
        ("L.TA.UE.Index3", "TA Index 3", "SUM"),
        ("L.TA.UE.Index4", "TA Index 4", "SUM"),
        ("L.TA.UE.Index5", "TA Index 5", "SUM"),
        ("L.TA.UE.Index6", "TA Index 6", "SUM"),
        ("L.TA.UE.Index7", "TA Index 7", "SUM"),
        ("L.TA.UE.Index8", "TA Index 8", "SUM"),
        ("L.TA.UE.Index9", "TA Index 9", "SUM"),
        ("L.TA.UE.Index10", "TA Index 10", "SUM"),
        ("L.TA.UE.Index11", "TA Index 11", "SUM"),
        ("L.TA.UE.Index12", "TA Index 12", "SUM"),
        ("L.TA.UE.Index13", "TA Index 13", "SUM"),
        ("L.TA.UE.Index14", "TA Index 14", "SUM"),
        ("L.TA.UE.Index15", "TA Index 15", "SUM"),
        ("Average TA", "Average TA", "AVG"),
        ("Average TA_NUM", "Num Average TA", "SUM"),
        ("Average TA_DENUM", "Denum Average TA", "SUM"),
    ],
    "Raw Rank & MCS": [
        ("L.ChMeas.RI.Rank1", "Rank 1 Samples", "SUM"),
        ("L.ChMeas.RI.Rank2", "Rank 2 Samples", "SUM"),
        ("DL_avg_MCS", "DL Avg MCS", "AVG"),
        ("DL_avg_MCS_num", "Num DL Avg MCS", "SUM"),
        ("DL_avg_MCS_denum", "Denum DL Avg MCS", "SUM"),
        ("UL_avg_MCS", "UL Avg MCS", "AVG"),
        ("UL_avg_MCS_num", "Num UL Avg MCS", "SUM"),
        ("UL_avg_MCS_denum", "Denum UL Avg MCS", "SUM"),
    ],
    "Raw Latency & VoLTE": [
        ("L.Traffic.DL.PktDelay.Time", "DL Packet Delay (ms)", "AVG"),
        ("L.Traffic.DL.PktDelay.Num", "Num DL Packet Delay", "SUM"),
        ("volte Traffic_erl", "VoLTE Traffic (Erl)", "SUM"),
        ("Average E2E VQI", "Average E2E VQI", "AVG"),
        ("Average E2E VQI_num", "Num E2E VQI", "SUM"),
        ("Average E2E VQI_den", "Denum E2E VQI", "SUM"),
    ],
    "Raw RSRP Distribution": [
        ("RSRP >= -110", "RSRP >= -110", "SUM"),
        ("RSRP >= -105", "RSRP >= -105", "SUM"),
        ("RSRP >= -100", "RSRP >= -100", "SUM"),
        ("RSRP >= -95", "RSRP >= -95", "SUM"),
    ],
    "Raw PDCCH": [
        ("L.ChMeas.PDCCH.AggLvl1Num", "PDCCH Agg Level 1", "SUM"),
        ("L.ChMeas.PDCCH.AggLvl2Num", "PDCCH Agg Level 2", "SUM"),
        ("L.ChMeas.PDCCH.AggLvl4Num", "PDCCH Agg Level 4", "SUM"),
        ("L.ChMeas.PDCCH.AggLvl8Num", "PDCCH Agg Level 8", "SUM"),
        ("PDCCH Agg8 %", "PDCCH Agg8 (%)", "AVG"),
        ("PDCCH Agg8 Num", "Num PDCCH Agg8", "SUM"),
        ("PDCCH Agg8 Denum", "Denum PDCCH Agg8", "SUM"),
        ("PDCCH CCE Utilization Rate", "PDCCH CCE Utilization Rate", "AVG"),
    ],
    "Raw NSA DC": [
        ("L.NsaDc.Capable.5gUser.RRC.Avg", "NSA DC Capable 5G User RRC Avg", "AVG"),
        ("L.NsaDc.Capable.User.RRC.Avg", "NSA DC Capable User RRC Avg", "AVG"),
        ("L.Thrp.bits.DL.NsaDc.MCG", "NSA DC DL Tput Bits (MCG)", "SUM"),
        ("L.Traffic.User.NsaDc.PCell.Avg", "NSA DC PCell User Avg", "AVG"),
        ("L.Thrp.bits.DL.NsaDc", "NSA DC DL Tput Bits", "SUM"),
        ("L.Thrp.bits.UL.NsaDc", "NSA DC UL Tput Bits", "SUM"),
    ]
}