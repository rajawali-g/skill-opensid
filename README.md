# 🏛️ Skill OpenSID untuk Antigravity AI

[![GitHub Repository](https://img.shields.io/badge/GitHub-rajawali--g%2Fskill--opensid-blue?logo=github)](https://github.com/rajawali-g/skill-opensid)
[![Release Version](https://img.shields.io/badge/Release-v2610.003-brightgreen)](#-riwayat-perubahan-changelog)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Target Platform](https://img.shields.io/badge/Platform-Antigravity%20AI-blueviolet)](https://antigravity.google/)

Paket keahlian (*AI Skill*) terlengkap untuk agen **Antigravity AI** dalam memandu, mengotomasi, dan mempercepat pengembangan ekosistem **OpenSID** (Sistem Informasi Desa berbasis open source terpopuler di Indonesia).

---

## 📌 Daftar Isi
- [Fitur Utama](#-fitur-utama)
- [Struktur & Cakupan Skill](#-struktur--cakupan-skill)
- [Fitur 1: Informasi Versi OpenSID dari GitHub](#-fitur-1-informasi-versi-opensid-dari-github)
- [Fitur 2: Folder Khusus Output Pembuatan Tema](#-fitur-2-folder-khusus-output-pembuatan-tema)
- [Sistem Penomoran Versi (TAG & RELEASE)](#-sistem-penomoran-versi-tag--release)
- [Skrip Otomatisasi Release](#-skrip-otomatisasi-release)
- [Panduan Integrasi ke GitHub](#-panduan-integrasi-ke-github)
- [Cara Pemasangan di Antigravity](#-cara-pemasangan-di-antigravity)
- [Riwayat Perubahan (Changelog)](#-riwayat-perubahan-changelog)

---

## 💡 Fitur Utama

- 🔄 **Sinkronisasi Versi GitHub Realtime**: Pelacakan otomatis rilis publik OpenSID Umum terkini (`OpenSID/OpenSID`), syarat PHP, ekstensi, dan dependensi backend/frontend.
- 🎨 **Folder Khusus Output Pembuatan Tema (`themes_output/`)**: Generator tema desa instan, pengemasan otomatis ke file `.zip` siap unggah via Web Admin OpenSID, dan sinkronisasi ke folder `desa/themes/`.
- 🧩 **Arsitektur Ganda (Hybrid)**: Memandu integrasi modern **Laravel Components** (`illuminate/*`) dan fondasi teruji **CodeIgniter 3** (`donjo-app`).
- 🛡️ **Aturan Wilayah Kustomisasi `desa/`**: Memastikan kustomisasi konfigurasi, tema, surat, dan upload aman dari penimpaan saat update sistem.
- 📜 **Layanan Surat & TTE**: Kamus lengkap kode variabel isian kependudukan dokumen ODT (LibreOffice) / RTF dan integrasi tanda tangan elektronik.
- 👥 **Kamus Database Kependudukan**: Relasi master tabel `tweb_penduduk`, `tweb_keluarga`, `tweb_wil_clusterdesa`, log surat, dan konfigurasi profil desa.

---

## 📂 Struktur Repositori

```text
skill-opensid/
├── .agents/skills/opensid/           # Paket Skill Utama Antigravity AI
│   ├── SKILL.md                      # Prompt utama & panduan aktivasi agen
│   ├── data/
│   │   └── opensid_latest_info.json  # Cache data rilis & stack OpenSID terkini
│   ├── references/                   # Dokumentasi teknis terperinci
│   │   ├── opensid-version-info.md   # Info rilis resmi GitHub, PHP & stack
│   │   ├── architecture.md           # Arsitektur sistem (Laravel + CI + folder desa/)
│   │   ├── modules-development.md    # Pembuatan modul, controller, model, migration
│   │   ├── themes-and-views.md       # Panduan tema & output themes_output/
│   │   ├── surat-dan-pelayanan.md    # Kamus kode variabel surat ODT & alur TTE
│   │   ├── database-kependudukan.md  # Relasi tabel kependudukan & wilayah
│   │   └── deployment-troubleshooting.md # Instalasi (Laragon/Linux), error umum, permission
│   ├── scripts/
│   │   ├── fetch_opensid_info.py     # Pengambil data rilis GitHub API
│   │   └── theme_manager.py          # Generator & packager ZIP tema
│   └── examples/
│       ├── contoh-modul.md           # Contoh modul starter
│       └── template-surat-keterangan.md # Contoh kode isian template ODT
├── themes_output/                    # FOLDER KHUSUS OUTPUT PEMBUATAN TEMA
│   ├── tema-starter-minsel/          # Kode sumber tema lengkap hasil kreasi
│   └── tema-starter-minsel.zip       # Paket ZIP siap unggah ke admin OpenSID
├── update-opensid-info.ps1           # Shortcut update data versi GitHub
├── manage-theme.ps1                  # Shortcut generator & packager tema
├── release.ps1                       # Skrip otomatisasi versi TAG & RELEASE
├── README.md                         # Dokumentasi utama proyek
└── CHANGELOG.md                      # Log riwayat seluruh versi
```

---

## 🔄 Fitur 1: Informasi Versi OpenSID dari GitHub

Fitur ini mengambil langsung data rilis umum (non-premium) dari repositori resmi [OpenSID/OpenSID](https://github.com/OpenSID/OpenSID):

### Cara Menjalankan Sinkronisasi:
```powershell
.\update-opensid-info.ps1
```

### Data yang Diperoleh Otomatis:
- **Versi Rilis Terkini**: `v2607.0.1` (Rilis Publik)
- **Persyaratan PHP**: `^8.1` (Rekomendasi: PHP 8.2)
- **Ekstensi PHP Wajib**: `curl`, `gd`, `intl`, `mbstring`, `mysqli`, `pdo_mysql`, `zip`, `fileinfo`, `xml`, `bcmath`, `exif`.
- **Backend Stack**: Hybrid Architecture (`codeigniter/framework` + Laravel `illuminate/*` components: Database, Auth, View, Cache, Spatie ActivityLog, Yajra DataTables).
- **Frontend Stack**: AdminLTE, Leaflet.js WebGIS, Bootstrap, TinyMCE, Select2, DataTables.

---

## 🎨 Fitur 2: Folder Khusus Output Pembuatan Tema

Semua hasil pembuatan tema web desa ditampung secara terpusat di folder `themes_output/`.

### Perintah Cepat Pengelola Tema (`manage-theme.ps1`):
```powershell
# 1. Buat kerangka tema baru
.\manage-theme.ps1 new -Name "minsel-modern" -Title "Tema Minsel Modern"

# 2. Kemas tema ke format ZIP siap unggah
.\manage-theme.ps1 package -Name "minsel-modern"

# 3. Lihat daftar tema yang tersedia
.\manage-theme.ps1 list

# 4. Sinkronkan langsung ke OpenSID lokal (Laragon/XAMPP)
.\manage-theme.ps1 deploy -Name "minsel-modern" -Target "D:\laragon\www\opensid"
```

### Cara Memasang Tema di OpenSID:
1. Buka Web Admin OpenSID.
2. Masuk ke menu **Pengaturan Web > Tema**.
3. Klik tombol **Unggah Tema**.
4. Pilih berkas dari `themes_output/<nama_tema>.zip`.

---

## 🏷️ Sistem Penomoran Versi (TAG & RELEASE)

Format versi: **`v[TAG].[RELEASE]`** (Contoh: `v2610.002`)
- **`TAG` (YYMM)**: 4 digit tahun dan bulan (`2610` = Oktober 2026).
- **`RELEASE` (XXX)**: 3 digit nomor urut rilis berurutan pada periode bulan tersebut (`001`, `002`, dst).

---

## 🚀 Skrip Otomatisasi Release

```powershell
.\release.ps1 -Message "Penambahan Fitur 1 (Update Versi GitHub) dan Fitur 2 (Output Tema)"
```

---

## 💻 Cara Pemasangan di Antigravity

### Pemasangan Global:
```powershell
Copy-Item -Recurse -Force ".agents\skills\opensid" "$env:USERPROFILE\.gemini\config\skills\opensid"
```
Setelah disalin, skill akan aktif secara permanen di seluruh sesi Antigravity AI.

---

## 📝 Riwayat Perubahan (Changelog)

### [v2610.002] - 2026-10-26
- **TAG**: `2610` | **RELEASE**: `002`
- **Added**:
  - **Fitur 1**: Skrip `fetch_opensid_info.py` dan shortcut `update-opensid-info.ps1` untuk mengambil data rilis resmi OpenSID umum, spesifikasi PHP, backend stack (Laravel & CI3), dan frontend stack dari GitHub `OpenSID/OpenSID`.
  - Berkas data terstruktur `data/opensid_latest_info.json` dan referensi dinamis `references/opensid-version-info.md`.
  - **Fitur 2**: Folder khusus output pembuatan tema desa (`themes_output/`).
  - Skrip utilitas tema `theme_manager.py` dan shortcut `manage-theme.ps1` untuk membuat tema, mengompresi ke ZIP siap upload, dan deploy ke OpenSID.
  - Tema starter contoh: `themes_output/tema-starter-minsel` beserta arsip `themes_output/tema-starter-minsel.zip`.

### [v2610.001] - 2026-10-26
- Inisialisasi awal repositori `skill-opensid` dan paket skill dasar.
