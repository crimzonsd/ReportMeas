const api = {
    /**
     * Mengirim permintaan untuk menguji koneksi database.
     * @param {string} db_type - Tipe database ('postgres' atau 'mysql').
     */
    testConnection: async (db_type) => {
        const response = await fetch('/test_connection', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ db_type })
        });
        return response.json();
    },

    /**
     * Mengambil daftar opsi KPI dari backend.
     * @param {string} db_type - Tipe database yang dipilih.
     * @param {string} tech - Teknologi yang dipilih.
     * @param {string} granularity - Timestamp yang dipilih.
     * @param {string} agg_level - Level agregasi yang dipilih.
     */
    fetchKpiOptions: async (db_type, tech, granularity, agg_level) => {
        const response = await fetch('/get_kpi_options', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ db_type, tech, granularity, agg_level })
        });
        return response.json();
    },

    /**
     * Mengirim semua data yang sudah dikumpulkan untuk men-generate laporan.
     */
    generateReport: async (reportData) => {
        const response = await fetch('/generate_report', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(reportData)
        });
        return response;
    }
};

