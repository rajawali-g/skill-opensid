# Panduan Instalasi, Konfigurasi Server & Troubleshooting

OpenSID dapat dijalankan pada lingkungan lokal pengembang (Laragon, XAMPP) maupun server produksi Linux (Ubuntu/Debian) dengan Nginx/Apache.

---

## 1. Kebutuhan Sistem
- **PHP**: PHP 8.1 atau PHP 8.2 (disarankan PHP 8.2).
- **Ekstensi PHP Wajib**:
  `curl`, `gd`, `intl`, `mbstring`, `mysqli`, `pdo_mysql`, `zip`, `fileinfo`, `xml`, `bcmath`, `exif`.
- **Database**: MySQL 5.7+ atau MariaDB 10.3+.
- **Web Server**: Apache dengan `mod_rewrite` aktif, atau Nginx.

---

## 2. Pengaturan Lingkungan Lokal di Laragon

1. Pastikan versi PHP pada Laragon disetel ke PHP 8.1 atau PHP 8.2.
2. Buat database baru di HeidiSQL / phpMyAdmin (misal: `db_opensid`).
3. Konfigurasi file database di `desa/config/database.php` atau `.env`:
   ```php
   'hostname' => 'localhost',
   'username' => 'root',
   'password' => '',
   'database' => 'db_opensid',
   'dbdriver' => 'mysqli',
   ```
4. Pastikan `upload_max_filesize` dan `post_max_size` pada `php.ini` dinaikkan minimal `64M` untuk impor database SIAK / e-KTP.

---

## 3. Masalah Umum & Solusi (Troubleshooting)

### A. Blank White Screen / Error 500
- **Penyebab**: Folder log/cache tidak memiliki izin tulis atau ekstensi PHP kurang.
- **Solusi**:
  Periksa error log di `storage/logs/laravel.log` atau `donjo-app/logs/`.
  Pastikan ekstensi `intl`, `fileinfo`, dan `gd` telah diaktifkan di `php.ini`.

### B. Upload Foto Penduduk atau Surat Gagal
- **Penyebab**: Folder `desa/upload/` tidak writable.
- **Solusi**:
  Di Linux: `chmod -R 775 desa/upload storage bootstrap/cache`
  Di Windows/Laragon: Pastikan folder tidak berstatus *Read-Only*.

### C. CSRF Token Mismatch saat Submit Form
- **Penyebab**: Session kedaluwarsa atau cache cookie browser.
- **Solusi**: Bersihkan cache browser atau periksa pengaturan domain session di konfigurasi.

### D. Impor Database Kependudukan Berhenti di Tengah Jalan
- **Penyebab**: `max_execution_time` habis.
- **Solusi**: Naikkan `max_execution_time = 300` dan `memory_limit = 512M` di `php.ini`.
