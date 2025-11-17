from flask import Flask, render_template, request, jsonify, send_file, make_response, redirect, url_for, flash
import backend
from io import BytesIO
import urllib.parse
import os

# Import tambahan untuk sistem login
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
# --------------------------------------------------------------------------
# --- Inisialisasi Aplikasi dan Konfigurasi Login ---
# --------------------------------------------------------------------------

# Inisialisasi aplikasi Flask
app = Flask(__name__)
# Kunci rahasia ini PENTING untuk keamanan sesi login. Ganti dengan string acak Anda sendiri.
app.config['SECRET_KEY'] = 'ganti-dengan-kunci-rahasia-yang-sangat-aman'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config['SESSION_PERMANENT'] = True
# Inisialisasi Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Jika pengguna mencoba mengakses halaman yang dilindungi, arahkan ke route 'login'
login_manager.login_message = "Harap login untuk mengakses halaman ini."

# --------------------------------------------------------------------------
# --- Model Pengguna dan Database Sederhana ---
# --------------------------------------------------------------------------

# Model Pengguna (User Model) yang dibutuhkan oleh Flask-Login
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Untuk sekarang, kita simpan pengguna di sini. Di aplikasi nyata, ini akan ada di database.
# Anda bisa menambah atau mengubah pengguna di sini.
users = {
    "1": User(id="1", username="admin", password="password123"),
    "2": User(id="2", username="user_satu", password="passwordsatu")
}

@login_manager.user_loader
def load_user(user_id):
    """Fungsi ini digunakan oleh Flask-Login untuk memuat pengguna dari sesi."""
    return users.get(user_id)

# --------------------------------------------------------------------------
# --- Form Login ---
# --------------------------------------------------------------------------

class LoginForm(FlaskForm):
    """Form login yang akan ditampilkan di halaman login."""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# --------------------------------------------------------------------------
# --- Rute untuk Autentikasi (Login/Logout) ---
# --------------------------------------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Menangani proses login pengguna."""
    form = LoginForm()
    if form.validate_on_submit():
        user_to_check = None
        # Cari pengguna berdasarkan username yang diinput
        for user in users.values():
            if user.username == form.username.data:
                user_to_check = user
                break
        
        # Jika pengguna ditemukan dan password cocok
        if user_to_check and user_to_check.check_password(form.password.data):
            login_user(user_to_check)
            flash('Login berhasil!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Username atau password salah.', 'error')
            
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    """Menangani proses logout pengguna."""
    logout_user()
    flash('Anda telah berhasil logout.', 'success')
    return redirect(url_for('login'))

# --------------------------------------------------------------------------
# --- Rute Aplikasi Utama (Sekarang Dilindungi) ---
# --------------------------------------------------------------------------

@app.route('/')
@login_required  # <-- DECORATOR PENTING: Pengguna harus login untuk mengakses ini
def index():
    """Menampilkan halaman utama web app (file index.html)."""
    return render_template('index.html')

@app.route('/test_connection', methods=['POST'])
@login_required # <-- API juga dilindungi
def test_connection():
    """Endpoint untuk menerima permintaan tes koneksi dari frontend."""
    db_type = request.json.get('db_type')
    if not db_type:
        return jsonify({"status": "error", "message": "Tipe database tidak dipilih."}), 400
    
    result = backend.check_db_connection(db_type)
    
    if result is True:
        return jsonify({"status": "success", "message": "Koneksi Berhasil!"})
    else:
        return jsonify({"status": "error", "message": str(result)})

@app.route('/get_kpi_options', methods=['POST'])
@login_required # <-- API juga dilindungi
def get_kpi_options():
    """Endpoint untuk mendapatkan daftar kolom KPI secara dinamis."""
    data = request.json
    db_type = data.get('db_type')
    tech = data.get('tech')
    granularity = data.get('granularity')
    agg_level = data.get('agg_level')
    
    if not all([db_type, tech, granularity, agg_level]):
        return jsonify({"status": "error", "message": "Opsi data belum lengkap."}), 400
    
    try:
        optional_cols, simple_kpi_map, advanced_kpi_map, mandatory_cols = backend.get_kpi_info(tech, granularity, agg_level, db_type)
        
        return jsonify({
            "status": "success",
            "mandatory_cols": mandatory_cols,
            "optional_cols": optional_cols,
            "simple_kpi_map": simple_kpi_map,
            "advanced_kpi_map": advanced_kpi_map
        })
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 404

@app.route('/generate_report', methods=['POST'])
@login_required # <-- API juga dilindungi
def generate_report():
    """Endpoint utama untuk memproses semua input dan menghasilkan laporan."""
    data = request.json
    
    result = backend.generate_dynamic_report_for_download(
        data.get('db_type'),
        data.get('tech'),
        data.get('granularity'),
        data.get('agg_level'),
        data.get('selected_items'),
        data.get('mode'),
        {
            "start_date": data.get('start_date'),
            "end_date": data.get('end_date'),
            "site_ids": data.get('site_ids')
        }
    )
    
    if result.get('status') == 'success':
        excel_data = result.get('excel_data')
        file_name = result.get('file_name')
        
        response = make_response(send_file(
            BytesIO(excel_data),
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=file_name
        ))
        
        query_encoded = urllib.parse.quote(result.get('query'))
        message_encoded = urllib.parse.quote(result.get('message'))
        response.headers['X-Report-Query'] = query_encoded
        response.headers['X-Report-Message'] = message_encoded
        response.headers['Access-Control-Expose-Headers'] = 'X-Report-Query, X-Report-Message'
        
        return response
    else:
        return jsonify(result)

# CATATAN: Blok if __name__ == '__main__' sudah dihapus agar siap untuk deployment.
# Gunakan 'waitress-serve app:app' untuk menjalankan server produksi.
