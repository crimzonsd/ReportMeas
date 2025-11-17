/**
 * =================================================================
 * STATE MANAGEMENT
 * =================================================================
 */
const state = {
    currentStep: 1,
    kpiDataCache: null,
};


/**
 * =================================================================
 * UI MANAGEMENT
 * =================================================================
 */
const ui = {
    elements: {
        steps: document.querySelectorAll('.step'),
        navItems: document.querySelectorAll('.step-indicator li'),
        statusBox: document.getElementById('status-box'),
        kpiOptions: document.getElementById('kpi-options'),
        kpiOptionsLoader: document.getElementById('kpi-options-loader'),
        testConnBtn: document.getElementById('test-conn-btn'),
        testConnStatus: document.getElementById('test-conn-status'),
        startDateInput: document.getElementById('start-date'),
        endDateInput: document.getElementById('end-date'),
        startDateLabel: document.getElementById('start-date-label'),
        endDateLabel: document.getElementById('end-date-label'),
        generateBtn: document.getElementById('generate-btn'),
        modeSimpleBtn: document.getElementById('mode-simple-btn'),
        modeAdvancedBtn: document.getElementById('mode-advanced-btn'),
        nextButtonStep3: document.querySelector('#step3 .btn-primary'),
        dbRadios: document.querySelectorAll('input[name="db_type"]'),
        tech2gLabel: document.getElementById('tech-2g-label'),
        tech5gLabel: document.getElementById('tech-5g-label'),
        tech4gRadio: document.getElementById('tech-4g-radio'),
        granularityBhLabel: document.getElementById('granularity-bh-label'),
        granularityWeeklyLabel: document.getElementById('granularity-weekly-label'),
        granularityMonthlyLabel: document.getElementById('granularity-monthly-label'),
        granularityDailyRadio: document.querySelector('input[name="granularity"][value="daily"]'),
        // --- PERBAIKAN BUG 2: Tambahkan elemen site ID ke UI ---
        siteIdLabel: document.querySelector('label[for="site-ids"]'),
        siteIdInput: document.getElementById('site-ids'),
    },

    goToStep: (stepNumber) => {
        if (stepNumber > 1 && !document.querySelector('input[name="db_type"]:checked')?.value) {
            console.error('Silakan pilih sumber database terlebih dahulu.'); 
            return;
        }
            if (stepNumber > 3 && (!state.kpiDataCache || state.kpiDataCache.status !== 'success')) {
            console.warn('Konfigurasi mungkin tidak lengkap, tetapi tetap dapat dilanjutkan.');
            const db_type = document.querySelector('input[name="db_type"]:checked')?.value;
            const granularity = document.querySelector('input[name="granularity"]:checked')?.value;
            const aggLevel = document.querySelector('input[name="agg_level"]:checked')?.value;
            
            // Izinkan lanjut jika error karena memang tidak ada config (cth: MySQL Busy Hour) atau level regional
            if (db_type === 'mysql' && granularity === 'busy_hour') {
                // Lanjutkan
            } else if (aggLevel === 'nop' || aggLevel === 'kabupaten' || aggLevel === 'balnus') {
                // Untuk level regional, tetap izinkan lanjut meski konfigurasi tidak lengkap
                console.warn(`Konfigurasi untuk ${aggLevel} level mungkin tidak lengkap, tetapi tetap dapat dilanjutkan.`);
            } else {
                console.error('Harap pilih opsi di Langkah 3 dan tunggu data KPI selesai dimuat dengan sukses.');
                return;
            }
        }
        state.currentStep = stepNumber;
        ui.elements.steps.forEach((step, index) => {
            step.classList.toggle('hidden', index + 1 !== state.currentStep);
        });
        ui.elements.navItems.forEach((nav, index) => {
            nav.classList.toggle('active', index + 1 === state.currentStep);
        });
        if (stepNumber === 4) {
            ui.renderKpiCheckboxes();
        }

        // --- PERBAIKAN BUG 2 (FRONTEND): Sembunyikan input Site ID jika level regional ---
        if (stepNumber === 5) {
            const aggLevel = document.querySelector('input[name="agg_level"]:checked')?.value;
            const isRegional = ['nop', 'kabupaten', 'balnus'].includes(aggLevel);
            
            // Tampilkan/Sembunyikan label dan input
            ui.elements.siteIdLabel.classList.toggle('hidden', isRegional);
            ui.elements.siteIdInput.classList.toggle('hidden', isRegional);

            // Bersihkan nilainya jika disembunyikan untuk menghindari pengiriman data
            if (isRegional) {
                ui.elements.siteIdInput.value = '';
            }
        }
        // --- AKHIR PERBAIKAN ---
    },

    setKpiLoading: (isLoading) => {
        const loader = ui.elements.kpiOptionsLoader;
        const content = ui.elements.kpiOptions;
        if (isLoading) {
            content.innerHTML = '';
            loader.style.display = 'flex';
            content.style.display = 'none';
        } else {
            loader.style.display = 'none';
            content.style.display = 'block';
        }
    },

    showStatus: (message, type) => {
        ui.elements.statusBox.className = type === 'error' ? 'status-error' : (type === 'success' ? 'status-success' : (type === 'loading' ? 'status-loading' : ''));
        ui.elements.statusBox.innerHTML = message;
    },

    showConnectionStatus: (message, type) => {
        const icon = type === 'success' ? '✅' : (type === 'loading' ? '<div class="loader-container"><div class="loader"></div></div>' : '❌');
        let colorClass = `color:${type === 'loading' ? 'var(--text-secondary)' : `var(--color-${type})`}`;
        ui.elements.testConnStatus.innerHTML = `<div style="${colorClass}; font-weight:500;">${icon} ${message}</div>`;
    },

    updateDateInputs: (granularity) => {
        const { startDateInput, endDateInput, startDateLabel, endDateLabel } = ui.elements;
        
        if (granularity === 'weekly') {
            startDateInput.type = 'week';
            endDateInput.type = 'week';
            startDateLabel.textContent = 'Minggu Mulai';
            endDateLabel.textContent = 'Minggu Selesai';
        } else if (granularity === 'monthly') {
            startDateInput.type = 'month';
            endDateInput.type = 'month';
            startDateLabel.textContent = 'Bulan Mulai';
            endDateLabel.textContent = 'Bulan Selesai';
        } else { // daily, hourly, busy_hour
            startDateInput.type = 'date';
            endDateInput.type = 'date';
            startDateLabel.textContent = 'Tanggal Mulai';
            endDateLabel.textContent = 'Tanggal Selesai';
        }
    },

    updateTechOptions: (db_type) => {
        const isMySql = db_type === 'mysql';

        // --- Logic for Technology Options (2G/5G disabled for MySQL) ---
        ui.elements.tech2gLabel.classList.toggle('disabled', isMySql);
        ui.elements.tech5gLabel.classList.toggle('disabled', isMySql);
        ui.elements.tech2gLabel.querySelector('input').disabled = isMySql;
        ui.elements.tech5gLabel.querySelector('input').disabled = isMySql;

        if (isMySql) {
            const selectedTechRadio = document.querySelector('input[name="tech"]:checked');
            if (selectedTechRadio && (selectedTechRadio.value === '2G' || selectedTechRadio.value === '5G')) {
                ui.elements.tech4gRadio.checked = true;
            }
        }

        // --- Logic for Granularity Options (Weekly/Monthly/BH) ---
        
        // 1. Sembunyikan/Tampilkan "Busy Hour"
        ui.elements.granularityBhLabel.classList.toggle('hidden', !isMySql);
        ui.elements.granularityBhLabel.querySelector('input').disabled = !isMySql;

        // 2. Nonaktifkan/Aktifkan "Weekly" & "Monthly" untuk MySQL, dan HILANGKAN teks "Maintenance" untuk PostgreSQL
        ['granularityWeeklyLabel', 'granularityMonthlyLabel'].forEach(elName => {
            const label = ui.elements[elName];
            const maintenanceText = label.querySelector('.maintenance-text');
            
            // Nonaktifkan/Aktifkan radio button itu sendiri (hanya untuk MySQL)
            label.classList.toggle('disabled', isMySql);
            label.querySelector('input').disabled = isMySql;
            
            // Sembunyikan/Tampilkan teks Maintenance
            if (maintenanceText) {
                // Sembunyikan teks maintenance jika BUKAN MySQL (yaitu PostgreSQL)
                maintenanceText.classList.toggle('hidden', !isMySql);
            }
        });

        // Pindahkan pilihan secara otomatis jika pilihan saat ini menjadi tidak valid
        const selectedGranularity = document.querySelector('input[name="granularity"]:checked');
        if (selectedGranularity) {
            // Jika Postgres dipilih & "Busy Hour" aktif, pindah ke "Daily"
            if (!isMySql && selectedGranularity.value === 'busy_hour') {
                ui.elements.granularityDailyRadio.checked = true; 
            }
            // Jika MySQL dipilih & "Weekly" atau "Monthly" aktif, pindah ke "Daily"
            if (isMySql && (selectedGranularity.value === 'weekly' || selectedGranularity.value === 'monthly')) {
                ui.elements.granularityDailyRadio.checked = true;
            }
        }
        
        // Panggil ulang untuk me-refresh data KPI
        handlers.handleOptionsChange();
    },

    renderKpiCheckboxes: () => {
        const mode = document.querySelector('.mode-switcher button.active').id.includes('simple') ? 'simple' : 'advanced';
        const aggLevel = document.querySelector('input[name="agg_level"]:checked')?.value;
        const container = ui.elements.kpiOptions;

        if (!state.kpiDataCache || state.kpiDataCache.status !== 'success') {
            container.innerHTML = `<div class="info-box" style="border-color: var(--color-error);"><p>${state.kpiDataCache?.message || "Data KPI belum termuat atau konfigurasi tidak ditemukan."}</p></div>`;
            return;
        }
        
        let html = `<div class="info-box"><h4>Data Dasar (Otomatis)</h4><p>${state.kpiDataCache.mandatory_cols.join(', ')}</p></div>`;
        
        if (mode === 'advanced') {
            html += `<div class="kpi-group" style="padding: 10px; border: 1px solid var(--border-color); border-radius: 8px; margin-bottom: 10px;"><label class="select-all-label"><input type="checkbox" id="master-select-all" onchange="handlers.toggleSelectAllEverything(this)"> <strong>PILIH SEMUA KOLOM</strong></label></div>`;
            
            const CELL_SPECIFIC_COLS = ['cell_name', 'ci', 'tac', 'azimuth', 'etilt', 'mtilt', 'horizontal_beamwidth', 'vertical_beamwidth', 'LocalCell Id', 'Cell Name'];
            let descriptiveCols = state.kpiDataCache.optional_cols;

            if (aggLevel === 'site') {
                descriptiveCols = descriptiveCols.filter(col => !CELL_SPECIFIC_COLS.includes(col));
            } else {
                descriptiveCols = descriptiveCols.filter(col => !state.kpiDataCache.mandatory_cols.includes(col));
            }

            if (descriptiveCols.length > 0) {
                html += `<details open class="kpi-group"><summary>Kolom Deskriptif & Dasar</summary><div class="details-content">
                            <label class="select-all-label"><input type="checkbox" class="group-select-all" onchange="handlers.toggleSelectAllInGroup(this)"> <strong>Pilih Semua di Grup Ini</strong></label>
                            <div class="kpi-grid">
                                ${descriptiveCols.map(col => `<label class="checkbox-label"><input type="checkbox" class="kpi-item" value="${col}" onchange="handlers.updateGroupSelectAll(this)"> <span>${col}</span></label>`).join('')}
                            </div>
                         </div></details>`;
            }

            Object.keys(state.kpiDataCache.advanced_kpi_map).forEach(category => {
                const kpis = state.kpiDataCache.advanced_kpi_map[category];
                html += `<details open class="kpi-group"><summary>${category}</summary><div class="details-content"><label class="select-all-label"><input type="checkbox" class="group-select-all" onchange="handlers.toggleSelectAllInGroup(this)"> <strong>Pilih Semua di Grup Ini</strong></label><div class="kpi-grid">${kpis.map(kpi => `<label class="checkbox-label"><input type="checkbox" class="kpi-item" value="${kpi[1]}" onchange="handlers.updateGroupSelectAll(this)"> <span>${kpi[1]}</span></label>`).join('')}</div></div></details>`;
            });
        } else {
            html += `<h4>Grup KPI (Pilih Kategori)</h4><div class="kpi-list-simple">${Object.keys(state.kpiDataCache.simple_kpi_map).map(category => `<label class="kpi-category-item"><input type="checkbox" class="kpi-item" value="${category}"><div class="content-wrapper"><strong>${category}</strong><svg class="checkmark-icon" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></div></label>`).join('')}</div>`;
        }
        
        container.innerHTML = html;
    }
};

/**
 * =================================================================
 * EVENT HANDLERS & LOGIC
 * =================================================================
 */
const handlers = {
    init: () => {
        ui.goToStep(1);
        ui.elements.navItems.forEach((item, index) => {
            if(item.id !== 'nav-logout') {
                 item.addEventListener('click', () => ui.goToStep(index + 1));
            }
        });
        document.querySelectorAll('input[name="tech"], input[name="granularity"], input[name="agg_level"]').forEach(radio => {
            radio.addEventListener('change', handlers.handleOptionsChange);
        });

        ui.elements.dbRadios.forEach(radio => {
            radio.addEventListener('change', (event) => {
                ui.updateTechOptions(event.target.value);
            });
        });

        ui.elements.testConnBtn.addEventListener('click', handlers.handleTestConnection);
        ui.elements.generateBtn.addEventListener('click', handlers.handleGenerateReport);
        ui.elements.modeSimpleBtn.addEventListener('click', () => handlers.switchMode('simple'));
        ui.elements.modeAdvancedBtn.addEventListener('click', () => handlers.switchMode('advanced'));
        
        const initialDbType = document.querySelector('input[name="db_type"]:checked')?.value;
        if(initialDbType) {
            ui.updateTechOptions(initialDbType);
        }
    },

    handleTestConnection: async () => {
        ui.elements.testConnBtn.disabled = true;
        ui.showConnectionStatus('Menghubungkan...', 'loading');
        
        const db_type = document.querySelector('input[name="db_type"]:checked')?.value;
        if (!db_type) {
            ui.showConnectionStatus('Gagal: Tipe database tidak dipilih.', 'error');
            ui.elements.testConnBtn.disabled = false;
            return;
        }

        const result = await api.testConnection(db_type);

        if (result.status === 'success') {
            ui.showConnectionStatus(result.message, 'success');
            setTimeout(() => ui.goToStep(3), 1000);
        } else {
            ui.showConnectionStatus(`Gagal: ${result.message}`, 'error');
        }
        ui.elements.testConnBtn.disabled = false;
    },

    handleOptionsChange: async () => {
    const granularity = document.querySelector('input[name="granularity"]:checked')?.value;
    if (granularity) ui.updateDateInputs(granularity);

    const db_type = document.querySelector('input[name="db_type"]:checked')?.value;
    const tech = document.querySelector('input[name="tech"]:checked')?.value;
    const aggLevel = document.querySelector('input[name="agg_level"]:checked')?.value;
    
    const nextBtn = ui.elements.nextButtonStep3;
    if (!db_type || !tech || !granularity || !aggLevel) {
        nextBtn.disabled = true;
        return;
    };

    nextBtn.disabled = true;
    nextBtn.textContent = 'Memuat...';

    ui.setKpiLoading(true);
    state.kpiDataCache = null;

    try {
        const result = await api.fetchKpiOptions(db_type, tech, granularity, aggLevel);
        state.kpiDataCache = result;
        
        // --- PERBAIKAN: Selalu aktifkan tombol untuk SEMUA level ---
        nextBtn.disabled = false;
        
        if (result.status !== 'success') {
            console.warn(`Konfigurasi untuk ${aggLevel} level mungkin tidak lengkap, tetapi tetap dapat dilanjutkan.`);
        }
    } catch (error) {
        console.error("Gagal memuat KPI:", error);
        state.kpiDataCache = { status: "error", message: "Terjadi kesalahan jaringan atau konfigurasi tidak ditemukan." };
        
        // --- PERBAIKAN: Untuk semua error, tetap aktifkan tombol ---
        nextBtn.disabled = false;
    } finally {
        ui.setKpiLoading(false);
        nextBtn.textContent = 'Lanjutkan →';
        if (state.currentStep === 4) {
            ui.renderKpiCheckboxes();
        }
    }
},

    handleGenerateReport: async () => {
        ui.elements.generateBtn.disabled = true;
        ui.showStatus('<div class="loader-container"><div class="loader"></div><p style="text-align:center;">Sedang memproses laporan...</p></div>', 'loading');
        
        const granularity = document.querySelector('input[name="granularity"]:checked').value;
        let startDate = ui.elements.startDateInput.value, endDate = ui.elements.endDateInput.value;
        
        // --- LOGIKA PERBAIKAN FORMAT DATE ---
        if (granularity === 'weekly') {
            // Konversi 'YYYY-Wnn' menjadi 'YYYYnn' (misal: '2025-W39' -> '202539')
            startDate = startDate.replace('-W', '');
            endDate = endDate.replace('-W', '');
        } else if (granularity === 'monthly') {
            // Konversi 'YYYY-MM' menjadi 'YYYYMM' (misal: '2025-09' -> '202509')
            startDate = startDate.replace('-', '');
            endDate = endDate.replace('-', '');
        } else if (granularity === 'hourly' || granularity === 'busy_hour') {
            // Tambahkan waktu untuk daily, hourly, busy_hour jika input hanya tanggal
            if (startDate && startDate.length === 10) startDate += ' 00:00:00';
            if (endDate && endDate.length === 10) endDate += ' 23:59:59';
        }
        // --- AKHIR LOGIKA PERBAIKAN FORMAT DATE ---

        const reportData = {
            db_type: document.querySelector('input[name="db_type"]:checked').value,
            tech: document.querySelector('input[name="tech"]:checked').value,
            granularity: granularity,
            agg_level: document.querySelector('input[name="agg_level"]:checked').value,
            selected_items: Array.from(document.querySelectorAll('.kpi-item:checked')).map(el => el.value),
            mode: document.querySelector('.mode-switcher button.active').id.includes('simple') ? 'simple' : 'advanced',
            start_date: startDate, // Menggunakan format yang sudah diolah
            end_date: endDate,     // Menggunakan format yang sudah diolah
            site_ids: document.getElementById('site-ids').value,
        };

        const response = await api.generateReport(reportData);
        
        if (response.headers?.get("content-type")?.includes("spreadsheetml")) {
            const queryEncoded = response.headers.get('X-Report-Query');
            const messageEncoded = response.headers.get('X-Report-Message');
            if (queryEncoded) {
                const queryText = decodeURIComponent(queryEncoded);
                const messageText = decodeURIComponent(messageEncoded);
                ui.showStatus(`<h3 style="color: var(--color-success);">✅ ${messageText}</h3><h4 style="margin-top:15px;">Query:</h4><div id="query-box"><button id="copy-btn" onclick="handlers.copyQuery(this)">Copy</button><pre id="query-text">${queryText}</pre></div>`, 'success');
            }
            const blob = await response.blob();
            const header = response.headers.get('Content-Disposition');
            let filename = 'report.xlsx';
            if(header) { const parts = header.split(';'); const filenamePart = parts.find(p => p.trim().startsWith('filename=')); if (filenamePart) filename = filenamePart.split('=')[1].trim().replaceAll('"', ''); }
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a'); a.href = url; a.download = filename;
            document.body.appendChild(a); a.click(); a.remove(); window.URL.revokeObjectURL(url);
        } else {
            const result = await response.json();
            ui.showStatus(`<h3 style="color: var(--color-error);">⚠️ Terjadi Masalah</h3><p>${result.message}</p>`, 'error');
        }
        ui.elements.generateBtn.disabled = false;
    },

    switchMode: (mode) => {
        ui.elements.modeSimpleBtn.classList.toggle('active', mode === 'simple');
        ui.elements.modeAdvancedBtn.classList.toggle('active', mode === 'advanced');
        ui.renderKpiCheckboxes();
    },

    toggleSelectAllInGroup: (checkbox) => {
        const group = checkbox.closest('.kpi-group');
        const items = group.querySelectorAll('.kpi-item');
        items.forEach(item => item.checked = checkbox.checked);
        handlers.updateMasterSelectAll();
    },

    toggleSelectAllEverything: (masterCheckbox) => {
        const allItems = document.querySelectorAll('#kpi-options .kpi-item, #kpi-options .group-select-all');
        allItems.forEach(cb => cb.checked = masterCheckbox.checked);
    },

    updateGroupSelectAll: (itemCheckbox) => {
        const group = itemCheckbox.closest('.kpi-group');
        if (!group) return;
        const groupSelectAll = group.querySelector('.group-select-all');
        const allItems = group.querySelectorAll('.kpi-item');
        const allChecked = Array.from(allItems).every(item => item.checked);
        groupSelectAll.checked = allChecked;
        handlers.updateMasterSelectAll();
    },

    updateMasterSelectAll: () => {
        const masterSelectAll = document.getElementById('master-select-all');
        if (!masterSelectAll) return;
        const allIndividualItems = document.querySelectorAll('#kpi-options .kpi-item');
        if(allIndividualItems.length === 0) return;
        const allItemsChecked = Array.from(allIndividualItems).every(item => item.checked);
        masterSelectAll.checked = allItemsChecked;
    },
    
    copyQuery: (button) => {
        const queryText = document.getElementById('query-text').innerText;
        // Menggunakan document.execCommand untuk kompatibilitas yang lebih baik di lingkungan iframe
        try {
            const tempInput = document.createElement('textarea');
            tempInput.value = queryText;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand('copy');
            document.body.removeChild(tempInput);
            button.innerText = 'Disalin!';
            setTimeout(() => { button.innerText = 'Copy'; }, 2000);
        } catch (err) {
            console.error('Gagal menyalin query: ', err);
            button.innerText = 'Gagal';
        }
    }
};

/**
 * =================================================================
 * INITIALIZATION
 * =================================================================
 */
document.addEventListener('DOMContentLoaded', handlers.init);