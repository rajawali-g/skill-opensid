# Informasi Versi & Arsitektur OpenSID Terkini (Non-Premium / Umum)

> **Catatan Sinkronisasi**: Terakhir diperbarui otomatis pada `26 October 2026 12:12:37` dari repositori GitHub resmi [OpenSID/OpenSID](https://github.com/OpenSID/OpenSID).

---

## 📌 Ringkasan Rilis Terkini
- **Versi OpenSID Umum**: `v2607.0.1` (Rilis v2607.0.1)
- **Tanggal Rilis Publik**: `2026-07-24`
- **Tautan Rilis Resmi**: [GitHub Release](https://github.com/OpenSID/OpenSID/releases/tag/v2607.0.1)
- **Unduh Kode Sumber**: [Download ZIP](https://api.github.com/repos/OpenSID/OpenSID/zipball/v2607.0.1)

---

## ⚙️ Kebutuhan Lingkungan Server
| Komponen | Spesifikasi Terkini | Rekomendasi |
| :--- | :--- | :--- |
| **Versi PHP** | `^8.1` | **PHP 8.2** |
| **Database** | `MySQL 5.7+ / MariaDB 10.3+` | MariaDB 10.6+ |
| **Web Server** | Apache (mod_rewrite) / Nginx | Laragon (Windows) / Nginx (Linux) |
| **Upload Max Size** | Minimal `64M` | Disarankan `128M` (impor kependudukan) |
| **Max Execution Time** | Minimal `180` detik | Disarankan `300` detik |

### Ekstensi PHP Wajib:
`bcmath, curl, exif, fileinfo, gd, intl, mbstring, mysqli, pdo_mysql, xml, zip`

---

## 🏗️ Spesifikasi Backend OpenSID
- **Pola Arsitektur**: **Hybrid Laravel Components + CodeIgniter 3 Core**
- **Sistem Dasar**: CodeIgniter 3 (`donjo-app`) untuk logika warisan modul pelayanan surat dan administrasi.
- **Layanan Modern**: Mengadopsi paket **Laravel Components (`illuminate/*`)**:
  - `illuminate/database` (Eloquent ORM & Query Builder terpusat)
  - `illuminate/auth`, `illuminate/session`, `illuminate/view`
  - `illuminate/cache`, `illuminate/events`, `illuminate/queue`
  - `yajra/laravel-datatables-oracle` (Server-side DataTables kependudukan)
  - `spatie/laravel-activitylog` (Audit trail & pencatatan log aksi operator)
  - `opensid/router` (Modular routing OpenSID)

---

## 🎨 Spesifikasi Frontend & Web Desa
- **Panel Administrator**: AdminLTE responsif berbasis Bootstrap.
- **Peta & WebGIS Desa**: **Leaflet.js** terintegrasi dengan endpoint GeoJSON untuk batas dusun, RW, RT, serta plotting sarana/prasarana.
- **Komponen Interaktif**:
  - DataTables dengan fitur filter multi-kolom dan ekspor Excel/PDF
  - TinyMCE editor untuk penulisan artikel web desa
  - Select2 untuk pemilih NIK & Kepala Keluarga dengan AJAX live search
  - Chart.js untuk infografis statistik kependudukan dan APBDes
- **Sistem Tema Publik**: Mendukung tema resmi (`natra`, `esensi`) dan sub-tema kustom di folder `desa/themes/`.
