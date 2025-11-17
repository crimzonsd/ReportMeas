import logging
import os
import io
import datetime

# Import library bot telegram
# Pastikan Anda sudah menginstalnya: pip install python-telegram-bot
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# Import "Otak" (Logika Backend) Anda
import backend

# Atur logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- TAHAPAN (STATES) UNTUK CONVERSATION HANDLER ---
# Ini adalah "langkah-langkah" dalam percakapan
# PERUBAHAN: Menambah 1 state (AWAIT_SITE_ID), total menjadi 8
SELECT_DB, SELECT_TECH, SELECT_GRANULARITY, SELECT_AGG_LEVEL, AWAIT_DATE, AWAIT_SITE_ID, SELECT_MODE, SELECT_KPI = range(8)

# --- FUNGSI START & PEMILIHAN DATABASE ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Memulai percakapan dan meminta pemilihan database."""
    # Bersihkan data pengguna dari percakapan sebelumnya
    context.user_data.clear()
    
    keyboard = [
        [
            InlineKeyboardButton("PostgreSQL", callback_data="db_postgres"),
            InlineKeyboardButton("MySQL", callback_data="db_mysql"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 Selamat datang di Bot KPI Report Generator!\n\n"
        "Saya akan memandu Anda melalui beberapa langkah untuk membuat laporan.\n\n"
        "Langkah 1: Silakan pilih sumber database:",
        reply_markup=reply_markup
    )
    
    # Pindah ke state/langkah SELECT_DB
    return SELECT_DB

# --- FUNGSI PEMILIHAN TEKNOLOGI ---
async def select_db(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Menyimpan DB dan meminta pemilihan Teknologi."""
    query = update.callback_query
    await query.answer()
    
    # Ekstrak data dari tombol ("db_postgres" -> "postgres")
    db_type = query.data.split('_')[1]
    context.user_data['db_type'] = db_type
    
    logger.info(f"User {query.from_user.username} memilih db: {db_type}")

    # Logika untuk menampilkan tombol berdasarkan pilihan DB
    # (Meniru logika di main.js - MySQL hanya mendukung 4G)
    if db_type == 'mysql':
        keyboard = [
            [InlineKeyboardButton("4G", callback_data="tech_4G")]
        ]
    else: # postgres
        keyboard = [
            [
                InlineKeyboardButton("4G", callback_data="tech_4G"),
                InlineKeyboardButton("5G", callback_data="tech_5G"),
                InlineKeyboardButton("2G", callback_data="tech_2G"),
            ]
        ]
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        text=f"Database: {db_type.upper()}\n\n"
             "Langkah 2: Silakan pilih teknologi:",
        reply_markup=reply_markup
    )
    
    # Pindah ke state/langkah SELECT_TECH
    return SELECT_TECH

# --- FUNGSI PEMILIHAN GRANULARITAS ---
async def select_tech(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Menyimpan Teknologi dan meminta Granularitas."""
    query = update.callback_query
    await query.answer()
    
    tech = query.data.split('_')[1]
    context.user_data['tech'] = tech
    db_type = context.user_data.get('db_type')
    
    logger.info(f"User {query.from_user.username} memilih tech: {tech}")

    # Logika untuk tombol Granularitas (MySQL punya 'bh', Postgres punya 'weekly'/'monthly')
    if db_type == 'mysql':
        keyboard = [
            [InlineKeyboardButton("Daily", callback_data="gran_daily")],
            [InlineKeyboardButton("Hourly", callback_data="gran_hourly")],
            [InlineKeyboardButton("Busy Hour", callback_data="gran_busy_hour")],
        ]
    else: # postgres
        keyboard = [
            [InlineKeyboardButton("Daily", callback_data="gran_daily")],
            [InlineKeyboardButton("Hourly", callback_data="gran_hourly")],
            [InlineKeyboardButton("Weekly", callback_data="gran_weekly")],
            [InlineKeyboardButton("Monthly", callback_data="gran_monthly")],
        ]
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        text=f"Database: {db_type.upper()}\n"
             f"Teknologi: {tech}\n\n"
             "Langkah 3: Silakan pilih granularitas (timestamp):",
        reply_markup=reply_markup
    )
    
    return SELECT_GRANULARITY

# --- FUNGSI PEMILIHAN LEVEL AGREGASI ---
async def select_granularity(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Menyimpan Granularitas dan meminta Level Agregasi."""
    query = update.callback_query
    await query.answer()
    
    granularity = query.data.split('_')[1]
    context.user_data['granularity'] = granularity
    
    logger.info(f"User {query.from_user.username} memilih granularity: {granularity}")

    keyboard = [
        [
            InlineKeyboardButton("Cell", callback_data="agg_cell"),
            InlineKeyboardButton("Site", callback_data="agg_site"),
        ],
        [
            InlineKeyboardButton("NOP", callback_data="agg_nop"),
            InlineKeyboardButton("Kabupaten", callback_data="agg_kabupaten"),
        ],
        [
            InlineKeyboardButton("Balnus", callback_data="agg_balnus")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        text=f"{context.user_data['db_type'].upper()} | {context.user_data['tech']} | {granularity.title()}\n\n"
             "Langkah 4: Silakan pilih level agregasi:",
        reply_markup=reply_markup
    )
    
    return SELECT_AGG_LEVEL

# --- FUNGSI MEMINTA TANGGAL ---
async def select_agg_level(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Menyimpan Level Agregasi dan meminta input Tanggal."""
    query = update.callback_query
    await query.answer()
    
    agg_level = query.data.split('_')[1]
    context.user_data['agg_level'] = agg_level
    granularity = context.user_data.get('granularity')

    logger.info(f"User {query.from_user.username} memilih agg_level: {agg_level}")

    # Menyesuaikan contoh format tanggal berdasarkan granularitas
    if granularity == 'weekly':
        prompt = "Contoh: `2025-W39 2025-W40`"
    elif granularity == 'monthly':
        prompt = "Contoh: `2025-09 2025-10`"
    else: # daily, hourly, bh
        prompt = "Contoh: `2025-09-01 2025-09-10`"

    await query.edit_message_text(
        text=f"{context.user_data['db_type'].upper()} | {context.user_data['tech']} | {context.user_data['granularity'].title()} | {agg_level.title()}\n\n"
             f"Langkah 5: Masukkan rentang tanggal (mulai selesai) dipisah spasi.\n"
             f"{prompt}\n\n"
             f"Ketik /cancel untuk membatalkan.",
        parse_mode="Markdown"
    )
    
    return AWAIT_DATE

# --- FUNGSI MENANGANI INPUT TANGGAL ---
async def await_date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Memproses tanggal yang diketik pengguna dan meminta Mode ATAU Site ID."""
    try:
        start_str, end_str = update.message.text.split()
    except (ValueError, TypeError):
        await update.message.reply_text(
            "Format salah. Harap masukkan DUA tanggal dipisah spasi (Contoh: `2025-01-01 2025-01-10`).\n"
            "Silakan coba lagi:",
            parse_mode="Markdown"
        )
        return AWAIT_DATE # Tetap di state ini

    granularity = context.user_data.get('granularity')
    
    # --- Meniru Logika Frontend (main.js) ---
    # Bot ini memformat tanggal persis seperti yang diharapkan backend dari web app
    try:
        if granularity == 'weekly':
            # Harapannya '2025-W39' -> '202539'
            start_date = start_str.replace('-W', '')
            end_date = end_str.replace('-W', '')
            if not (start_date.isdigit() and len(start_date) == 6): raise ValueError("Format Week salah")
        elif granularity == 'monthly':
            # Harapannya '2025-09' -> '202509'
            start_date = start_str.replace('-', '')
            end_date = end_str.replace('-', '')
            if not (start_date.isdigit() and len(start_date) == 6): raise ValueError("Format Month salah")
        elif granularity in ['hourly', 'busy_hour']:
            # Harapannya '2025-09-10' -> '2025-09-10 00:00:00'
            datetime.datetime.strptime(start_str, '%Y-%m-%d') # Validasi format
            datetime.datetime.strptime(end_str, '%Y-%m-%d')   # Validasi format
            start_date = start_str + ' 00:00:00'
            end_date = end_str + ' 23:59:59'
        else: # daily
            datetime.datetime.strptime(start_str, '%Y-%m-%d') # Validasi format
            datetime.datetime.strptime(end_str, '%Y-%m-%d')   # Validasi format
            start_date = start_str
            end_date = end_str
    except Exception as e:
        logger.warning(f"Error parsing date: {e}")
        await update.message.reply_text(
            f"Format tanggal tidak sesuai untuk granularitas '{granularity}'.\n"
            "Contoh (Daily): `2025-01-01 2025-01-10`\n"
            "Contoh (Weekly): `2025-W39 2025-W40`\n"
            "Contoh (Monthly): `2025-01 2025-03`\n"
            "Silakan coba lagi:",
            parse_mode="Markdown"
        )
        return AWAIT_DATE # Tetap di state ini

    context.user_data['start_date'] = start_date
    context.user_data['end_date'] = end_date
    
    logger.info(f"User {update.message.from_user.username} memasukkan tanggal: {start_date} - {end_date}")

    # --- PERUBAHAN LOGIKA ---
    # Cek level agregasi. Jika site/cell, minta Site ID. Jika regional, langsung ke Mode.
    agg_level = context.user_data.get('agg_level')

    if agg_level in ['site', 'cell']:
        # Minta Site ID
        # --- PERBAIKAN: Tambahkan tombol "ALL SITES" ---
        keyboard = [
            [InlineKeyboardButton("Pilih SEMUA SITE", callback_data="site_all")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            f"Langkah 6: Masukkan Site ID (pisahkan dengan koma).\n"
            f"ATAU, klik tombol di bawah untuk mengambil semua site.\n\n"
            f"Ketik /cancel untuk membatalkan.",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
        return AWAIT_SITE_ID
    else:
        # Level Regional (nop, kabupaten, balnus) -> Langsung ke Pilih Mode
        keyboard = [
            [InlineKeyboardButton("Simple (Pilih Kategori)", callback_data="mode_simple")],
            [InlineKeyboardButton("Advanced (Ambil SEMUA KPI)", callback_data="mode_advanced")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "Langkah 6: Silakan pilih mode Laporan:", # Step 6 untuk regional
            reply_markup=reply_markup
        )
        return SELECT_MODE

# --- FUNGSI BARU UNTUK MENANGANI INPUT SITE ID (Teks) ---
async def await_site_id_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Menyimpan Site ID (dari Teks) dan meminta Mode."""
    site_ids_input = update.message.text
    
    if site_ids_input.strip().upper() == 'ALL':
        context.user_data['site_ids'] = "" # Backend menangani string kosong sebagai "semua"
    else:
        context.user_data['site_ids'] = site_ids_input
    
    logger.info(f"User {update.message.from_user.username} memasukkan site_ids: {site_ids_input}")

    keyboard = [
        [InlineKeyboardButton("Simple (Pilih Kategori)", callback_data="mode_simple")],
        [InlineKeyboardButton("Advanced (Ambil SEMUA KPI)", callback_data="mode_advanced")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Ini sekarang menjadi Langkah 7 untuk alur site/cell
    await update.message.reply_text(
        "Langkah 7: Silakan pilih mode Laporan:",
        reply_markup=reply_markup
    )
    
    return SELECT_MODE

# --- FUNGSI BARU UNTUK MENANGANI INPUT SITE ID (Tombol) ---
async def await_site_id_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Menyimpan Site ID (dari Tombol ALL) dan meminta Mode."""
    query = update.callback_query
    await query.answer()

    context.user_data['site_ids'] = "" # Tombol "ALL" berarti string kosong
    
    logger.info(f"User {query.from_user.username} memilih SEMUA SITE")

    keyboard = [
        [InlineKeyboardButton("Simple (Pilih Kategori)", callback_data="mode_simple")],
        [InlineKeyboardButton("Advanced (Ambil SEMUA KPI)", callback_data="mode_advanced")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Edit pesan sebelumnya, jangan kirim baru
    await query.edit_message_text(
        text="Langkah 7: Silakan pilih mode Laporan:",
        reply_markup=reply_markup
    )
    
    return SELECT_MODE

# --- FUNGSI MEMBANGUN KEYBOARD KPI (UNTUK SIMPLE MODE) ---
def build_kpi_keyboard(context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
    """Helper untuk membuat keyboard multi-pilih."""
    kpi_maps = context.user_data.get('kpi_maps', {})
    # Fungsi ini hanya dipanggil untuk mode simple
    kpi_source = kpi_maps.get('simple', {})
    
    selected_kpis = context.user_data.get('selected_kpis', set())
    
    keyboard = []
    # Buat tombol untuk setiap kategori
    for category in kpi_source.keys():
        prefix = "✅ " if category in selected_kpis else "❌ "
        button = InlineKeyboardButton(prefix + category, callback_data=category)
        keyboard.append([button])
        
    # Tambahkan tombol Selesai
    keyboard.append([InlineKeyboardButton(">> SELESAI & GENERATE <<", callback_data="kpi_done")])
    return InlineKeyboardMarkup(keyboard)

# --- FUNGSI PEMILIHAN MODE ---
async def select_mode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Menyimpan Mode. Jika Simple, tampilkan pilihan KPI. Jika Advanced, langsung generate."""
    query = update.callback_query
    await query.answer()
    
    mode = query.data.split('_')[1]
    context.user_data['mode'] = mode
    
    data = context.user_data
    
    logger.info(f"User {query.from_user.username} memilih mode: {mode}")
    
    # Panggil backend.get_kpi_info untuk mendapatkan daftar KPI
    try:
        opt_cols, simple_map, adv_map, mand_cols = backend.get_kpi_info(
            tech=data['tech'],
            granularity=data['granularity'],
            agg_level=data['agg_level'],
            db_type=data['db_type']
        )
        context.user_data['kpi_maps'] = {'simple': simple_map, 'advanced': adv_map}
        context.user_data['optional_cols'] = opt_cols
    except Exception as e:
        logger.error(f"Gagal memuat KPI info dari backend: {e}")
        await query.edit_message_text(f"❌ Error: Gagal memuat konfigurasi KPI dari backend. {e}")
        return ConversationHandler.END

    if mode == 'simple':
        # Tampilkan keyboard multi-pilih untuk mode simple
        reply_markup = build_kpi_keyboard(context)
        
        # PERUBAHAN: Menyesuaikan nomor langkah
        step_number = 8 if context.user_data.get('agg_level') in ['site', 'cell'] else 7
        
        await query.edit_message_text(
            text=f"Langkah {step_number}: Pilih Kategori KPI (bisa lebih dari satu). Klik Selesai jika sudah.",
            reply_markup=reply_markup
        )
        return SELECT_KPI
    else:
        # Mode Advanced: Ambil SEMUA KPI
        adv_map = context.user_data['kpi_maps']['advanced']
        all_advanced_kpis = []
        # Ambil semua alias KPI (kpi[1]) dari semua kategori
        for category_kpis in adv_map.values():
            all_advanced_kpis.extend([kpi[1] for kpi in category_kpis])
        
        # Tambahkan juga kolom opsional
        all_advanced_kpis.extend(context.user_data['optional_cols'])
        
        context.user_data['selected_items'] = all_advanced_kpis
        
        # Langsung lompat ke fungsi generate
        return await generate_report(update, context)

# --- FUNGSI PEMILIHAN KPI (MULTI-PILIH) ---
async def select_kpi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Menangani pemilihan KPI multi-pilih untuk mode Simple."""
    query = update.callback_query
    await query.answer()
    
    selected_item = query.data
    
    # Inisialisasi set jika belum ada
    if 'selected_kpis' not in context.user_data:
        context.user_data['selected_kpis'] = set()

    if selected_item == 'kpi_done':
        # Pengguna menekan tombol Selesai
        if not context.user_data['selected_kpis']:
            await context.bot.send_message(
                chat_id=query.effective_chat.id,
                text="Anda belum memilih kategori KPI. Harap pilih setidaknya satu."
            )
            return SELECT_KPI # Tetap di state ini
            
        # Simpan daftar final
        context.user_data['selected_items'] = list(context.user_data['selected_kpis'])
        # Panggil fungsi generate
        return await generate_report(update, context)
    else:
        # Pengguna memilih/membatalkan pilihan kategori
        if selected_item in context.user_data['selected_kpis']:
            context.user_data['selected_kpis'].remove(selected_item)
        else:
            context.user_data['selected_kpis'].add(selected_item)
            
        # Gambar ulang keyboard dengan status ✅/❌ yang baru
        reply_markup = build_kpi_keyboard(context)
        
        # PERUBAHAN: Menyesuaikan nomor langkah
        step_number = 8 if context.user_data.get('agg_level') in ['site', 'cell'] else 7
        
        await query.edit_message_text(
            text=f"Langkah {step_number}: Pilih Kategori KPI (bisa lebih dari satu). Klik Selesai jika sudah.",
            reply_markup=reply_markup
        )
        return SELECT_KPI # Tetap di state ini

# --- FUNGSI GENERATE LAPORAN ---
async def generate_report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Mengumpulkan semua data dan memanggil backend untuk membuat laporan."""
    # Tampilkan pesan "memproses"
    if update.callback_query:
        await update.callback_query.edit_message_text("⚙️ Sedang memproses laporan... Ini mungkin perlu waktu beberapa saat.")
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="⚙️ Sedang memproses laporan (Advanced Mode)... Ini mungkin perlu waktu beberapa saat."
        )

    data = context.user_data
    
    try:
        logger.info(f"Memulai generate_dynamic_report_for_download dengan data: {data}")
        
        result = backend.generate_dynamic_report_for_download(
            db_type=data['db_type'],
            tech=data['tech'],
            granularity=data['granularity'],
            agg_level=data['agg_level'],
            selected_items=data['selected_items'],
            mode=data['mode'],
            where_conditions={
                "start_date": data['start_date'],
                "end_date": data['end_date'],
                # PERUBAHAN: Ambil site_ids dari context, default ke "" jika tidak ada (untuk regional)
                "site_ids": data.get('site_ids', '') 
            }
        )
        
        if result.get('status') == 'success':
            logger.info("Laporan berhasil dibuat. Mengirim file...")
            excel_data = result.get('excel_data')
            file_name = result.get('file_name')
            query_sql = result.get('query')

            # Kirim file Excel
            await context.bot.send_document(
                chat_id=update.effective_chat.id,
                document=io.BytesIO(excel_data),
                filename=file_name,
                caption=f"✅ Laporan Anda Selesai: `{file_name}`"
            )
            
            # --- PERBAIKAN: CEK MODE & PANJANG QUERY ---
            
            data = context.user_data # Ambil data untuk cek mode
            mode = data.get('mode')
            
            query_message = ""
            
            if mode == 'advanced':
                # JIKA ADVANCED: Jangan kirim query asli. Kirim placeholder.
                # Ini untuk menghindari error "Message is too long" dari Telegram.
                query_message = (
                    "Query yang digunakan (Mode Advanced):\n"
                    "```sql\n"
                    "SELECT [BANYAK KOLOM... (terlalu panjang untuk ditampilkan)]\n"
                    f"FROM {result.get('file_name').split('_')[0]}_table\n" # Ambil nama tabel dari info file
                    "WHERE ...\n"
                    "GROUP BY ...\n"
                    "ORDER BY ...\n"
                    "```"
                )
            else:
                # JIKA SIMPLE: Query biasanya pendek, coba kirim.
                query_message = f"Query yang digunakan:\n```sql\n{query_sql}\n```"

            # Pengecekan terakhir jika query Simple mode ternyata juga terlalu panjang
            if len(query_message) > 4096:
                query_message = "Query yang digunakan terlalu panjang untuk ditampilkan di Telegram."

            # Kirim query sebagai pesan terpisah
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=query_message,
                parse_mode="Markdown"
            )
        else:
            logger.warning(f"Backend mengembalikan error: {result.get('message')}")
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"⚠️ Gagal membuat laporan: {result.get('message')}"
            )
            
    except Exception as e:
        logger.error(f"Terjadi exception di generate_report: {e}", exc_info=True)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"❌ Terjadi kesalahan internal pada bot: {e}"
        )
        
    finally:
        # Akhiri percakapan
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Percakapan selesai. Ketik /start untuk memulai lagi."
        )
        # return ConversationHandler.END  <- DIHAPUS DARI SINI
    
    # DIPINDAHKAN KE SINI:
    # Selalu akhiri percakapan setelah try/except/finally selesai.
    return ConversationHandler.END

# --- FUNGSI PEMBATALAN ---
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Membatalkan percakapan."""
    await update.message.reply_text("Dibatalkan. Ketik /start untuk memulai lagi.")
    context.user_data.clear()
    return ConversationHandler.END

# --- FUNGSI MAIN ---
def main() -> None:
    """Jalankan bot."""
    
    # --- MASUKKAN TOKEN BOT ANDA DI SINI ---
    # Dapatkan token ini dari BotFather di Telegram
    TOKEN = "8542118225:AAFAluAigTQU5_iRiGuMmeQD9Ihv-ibrXXc"
    
    # --- PERBAIKAN ---
    # HAPUS BLOK 'IF' DI BAWAH INI.
    # Blok ini adalah penyebab error. Dia membandingkan token Anda yang sudah benar
    # dan mengira itu adalah placeholder.
    #
    # if TOKEN == "8542118225:AAFAluAigTQU5_iRiGuMmeQD9Ihv-ibrXXc":
    #     logger.error("FATAL: Token Bot belum diisi. Harap edit file bot.py")
    #     return
    
    # Baris di bawah ini sekarang akan berjalan dengan benar
    application = Application.builder().token(TOKEN).build()

    # Definisikan ConversationHandler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_DB: [CallbackQueryHandler(select_db, pattern='^db_')],
            SELECT_TECH: [CallbackQueryHandler(select_tech, pattern='^tech_')],
            SELECT_GRANULARITY: [CallbackQueryHandler(select_granularity, pattern='^gran_')],
            SELECT_AGG_LEVEL: [CallbackQueryHandler(select_agg_level, pattern='^agg_')],
            AWAIT_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, await_date)],
            # PERUBAHAN: Menambahkan handler untuk tombol & teks
            AWAIT_SITE_ID: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, await_site_id_text),
                CallbackQueryHandler(await_site_id_button, pattern='^site_all$')
            ],
            SELECT_MODE: [CallbackQueryHandler(select_mode, pattern='^mode_')],
            SELECT_KPI: [CallbackQueryHandler(select_kpi)], # Menangani SEMUA callback di state ini
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(conv_handler)
    
    logger.info("Bot mulai berjalan...")
    # Jalankan bot
    application.run_polling()

if __name__ == '__main__':
    main()