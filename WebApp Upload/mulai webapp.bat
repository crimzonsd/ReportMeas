@echo off
title KPI Report Server

echo Changing directory to the script's location...
:: Perintah ini secara otomatis pindah ke folder di mana file .bat ini berada
cd /d "%~dp0"

echo Starting server on http://127.0.0.1:5000
echo Press Ctrl+C to stop the server.

:: Menjalankan server menggunakan Waitress, bukan python
waitress-serve --host=127.0.0.1 --port=5000 app:app

pause