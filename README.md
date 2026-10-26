# 🏛️ Skill OpenSID untuk Antigravity AI

[![GitHub Repository](https://img.shields.io/badge/GitHub-rajawali--g%2Fskill--opensid-blue?logo=github)](https://github.com/rajawali-g/skill-opensid)
[![Release Version](https://img.shields.io/badge/Release-v2610.007-brightgreen)](#-riwayat-perubahan-changelog)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Target Platform](https://img.shields.io/badge/Platform-Antigravity%20AI-blueviolet)](https://antigravity.google/)

Paket keahlian (*AI Skill*) terlengkap untuk agen **Antigravity AI** dalam memandu, mengotomasi, dan mempercepat pengembangan ekosistem **OpenSID** (Sistem Informasi Desa berbasis open source terpopuler di Indonesia).

---

## 📌 Daftar Isi
- [Fitur Utama](#-fitur-utama)
- [3 Tema Dasar Resmi Siap Pakai](#-3-tema-dasar-resmi-siap-pakai)
- [Fitur 1: Informasi Versi OpenSID dari GitHub](#-fitur-1-informasi-versi-opensid-dari-github)
- [Fitur 2: Folder Khusus Output Tema & Packager ZIP](#-fitur-2-folder-khusus-output-tema--packager-zip)
- [Sistem Penomoran Versi (TAG & RELEASE)](#-sistem-penomoran-versi-tag--release)
- [Skrip Otomatisasi Release](#-skrip-otomatisasi-release)
- [Cara Pemasangan di Antigravity](#-cara-pemasangan-di-antigravity)
- [Riwayat Perubahan (Changelog)](#-riwayat-perubahan-changelog)

---

## 💡 Fitur Utama

- 🎨 **3 Tema Dasar Siap Pakai**: Pedesaan Klasik, Desa Modern, dan Desa Digital (Smart Village) berstandar resmi Laravel Blade.
- 🔄 **Sinkronisasi Versi GitHub Realtime**: Pelacakan otomatis rilis publik OpenSID Umum terkini (`OpenSID/OpenSID`), syarat PHP, ekstensi, dan dependensi backend/frontend.
- 📦 **Folder Khusus Output Tema (`themes_output/`)**: Generator tema desa instan, pengemasan otomatis ke file `.zip` siap unggah via Web Admin OpenSID.
- 🧩 **Arsitektur Ganda (Hybrid)**: Memandu integrasi modern **Laravel Components** (`illuminate/*`) dan fondasi teruji **CodeIgniter 3** (`donjo-app`).
- 📜 **Layanan Surat & TTE**: Kamus lengkap kode variabel isian kependudukan dokumen ODT (LibreOffice) / RTF dan integrasi tanda tangan elektronik.
- 👥 **Kamus Database Kependudukan**: Relasi master tabel `tweb_penduduk`, `tweb_keluarga`, `tweb_wil_clusterdesa`, log surat, dan konfigurasi profil desa.

---

## 🎨 3 Tema Dasar Resmi Siap Pakai

Telah disediakan 3 tema dasar pengembangan dengan arsitektur resmi Laravel Blade (`resources/views/`, `config.json`, `composer.json`, `theme::` namespace):

| Tema | Nuansa Desain | Berkas ZIP Siap Unggah |
| :--- | :--- | :--- |
| **🌾 Pedesaan Klasik** | Kearifan lokal, agraris, palet hangat hijau daun & kayu, ramah warga lansia | `themes_output/tema-pedesaan-klasik.zip` |
| **🏛️ Desa Modern** | Pemerintahan bersih, elegan, kartu soft shadow, tata kelola transparan | `themes_output/tema-desa-modern.zip` |
| **⚡ Desa Digital** | *Smart Village* futuristik, live counter statistik, kartu *glassmorphism*, neon cyan | `themes_output/tema-desa-digital.zip` |

---

## 📂 Struktur Repositori

```text
skill-opensid/
├── .agents/skills/opensid/           # Paket Skill Utama Antigravity AI
│   ├── SKILL.md                      # Prompt utama & panduan aktivasi agen
│   ├── data/
│   │   └── opensid_latest_info.json  # Cache data rilis & stack OpenSID terkini
│   ├── references/                   # Dokumentasi teknis terperinci
│   │   ├── arsitektur-tema-opensid.md # Bedah arsitektur resmi tema Blade (Esensi & Natra)
│   │   ├── opensid-version-info.md   # Info rilis resmi GitHub, PHP & stack
│   │   ├── themes-and-views.md       # Panduan tema & katalog 3 tema dasar
│   │   ├── architecture.md           # Arsitektur sistem (Laravel + CI + folder desa/)
│   │   ├── modules-development.md    # Pembuatan modul, controller, model, migration
│   │   ├── surat-dan-pelayanan.md    # Kamus kode variabel surat ODT & alur TTE
│   │   ├── database-kependudukan.md  # Relasi tabel kependudukan & wilayah
│   │   └── deployment-troubleshooting.md # Instalasi (Laragon/Linux), error umum, permission
│   ├── scripts/
│   │   ├── fetch_opensid_info.py     # Pengambil data rilis GitHub API
│   │   ├── build_three_themes.py     # Builder 3 tema dasar resmi
│   │   └── theme_manager.py          # Generator & packager ZIP tema
│   └── examples/
│       ├── contoh-modul.md           # Contoh modul starter
│       └── template-surat-keterangan.md # Contoh kode isian template ODT
├── themes_output/                    # FOLDER KHUSUS OUTPUT PEMBUATAN TEMA
│   ├── tema-pedesaan-klasik/         # Kode sumber tema pedesaan klasik
│   ├── tema-pedesaan-klasik.zip      # Paket ZIP siap pasang (8.4 KB)
│   ├── tema-desa-modern/             # Kode sumber tema desa modern
│   ├── tema-desa-modern.zip          # Paket ZIP siap pasang (7.7 KB)
│   ├── tema-desa-digital/            # Kode sumber tema smart village
│   ├── tema-desa-digital.zip         # Paket ZIP siap pasang (8.3 KB)
│   └── tema-starter-minsel/          # Tema starter
├── standard/                         # Repositori acuan tema standar bawaan (Esensi & Natra)
├── update-opensid-info.ps1           # Shortcut update data versi GitHub
├── manage-theme.ps1                  # Shortcut generator & packager tema
├── release.ps1                       # Skrip otomatisasi versi TAG & RELEASE
├── README.md                         # Dokumentasi utama proyek
└── CHANGELOG.md                      # Log riwayat seluruh versi
```

---

## 🔄 Fitur 1: Informasi Versi OpenSID dari GitHub

```powershell
.\update-opensid-info.ps1
```
- **Versi Rilis Terkini**: `v2607.0.1` (Rilis Publik)
- **Persyaratan PHP**: `^8.1` (Rekomendasi: PHP 8.2)
- **Ekstensi PHP Wajib**: `curl`, `gd`, `intl`, `mbstring`, `mysqli`, `pdo_mysql`, `zip`, `fileinfo`, `xml`, `bcmath`, `exif`.

---

## 🎨 Fitur 2: Folder Khusus Output Pembuatan Tema

Semua hasil pembuatan tema web desa ditampung secara terpusat di folder `themes_output/`.

### Perintah Cepat Pengelola Tema (`manage-theme.ps1`):
```powershell
# 1. Buat kerangka tema baru
.\manage-theme.ps1 new -Name "nama-tema" -Title "Judul Tema"

# 2. Kemas tema ke format ZIP siap unggah
.\manage-theme.ps1 package -Name "nama-tema"

# 3. Lihat daftar tema yang tersedia
.\manage-theme.ps1 list

# 4. Sinkronkan langsung ke OpenSID lokal (Laragon/XAMPP)
.\manage-theme.ps1 deploy -Name "nama-tema" -Target "D:\laragon\www\opensid"
```

---

## 🏷️ Sistem Penomoran Versi (TAG & RELEASE)

Format versi: **`v[TAG].[RELEASE]`** (Contoh: `v2610.004`)
- **`TAG` (YYMM)**: 4 digit tahun dan bulan (`2610` = Oktober 2026).
- **`RELEASE` (XXX)**: 3 digit nomor urut rilis berurutan pada periode bulan tersebut (`001`, `002`, dst).

---

## 🚀 Skrip Otomatisasi Release

```powershell
.\release.ps1 -Message "Catatan perubahan rilis..."
```

---

## 💻 Cara Pemasangan Instan di Antigravity

Paket siap instalasi tersedia di folder `skill_package/`. Cukup jalankan skrip instalasi otomatis:

```powershell
# Jalankan installer otomatis (otomatis pasang ke Global ~/.gemini/config/skills/ dan Workspace)
.\install-skill.ps1
```

Atau jika menggunakan Linux / macOS / WSL:
```bash
chmod +x ./skill_package/install-skill.sh
./skill_package/install-skill.sh
```

Buku panduan lengkap dan contoh-contoh prompt perintah tersedia di [skill_package/PANDUAN_PENGGUNAAN.md](file:///d:/project_opensid/skill_package/PANDUAN_PENGGUNAAN.md).


---

## 📝 Riwayat Perubahan (Changelog)

### [v2610.004] - 2026-10-26
- **TAG**: `2610` | **RELEASE**: `004`
- **Added**:
  - Pembangunan 3 tema dasar baru siap pakai di `themes_output/`:
    1. **`tema-pedesaan-klasik`** (`themes_output/tema-pedesaan-klasik.zip`): Kearifan lokal, agraris, ramah warga.
    2. **`tema-desa-modern`** (`themes_output/tema-desa-modern.zip`): Tata kelola pemerintahan bersih, sleek, elegan.
    3. **`tema-desa-digital`** (`themes_output/tema-desa-digital.zip`): Smart village, live stats counter, glassmorphism, neon cyan.
  - Skrip builder otomatis `build_three_themes.py`.
  - Pembaruan dokumentasi katalog tema di `references/themes-and-views.md`.

### [v2610.003] - 2026-10-26
- Bedah arsitektur resmi tema OpenSID dari tema default `esensi` dan `natra` di folder `standard/`.
- Dokumentasi teknis `references/arsitektur-tema-opensid.md` (Laravel Blade, `theme::` namespace, `config.json`, `composer.json`).
- Standardisasi generator `theme_manager.py` ke Laravel Blade.

### [v2610.002] - 2026-10-26
- Penambahan Fitur 1 (Update Versi GitHub) dan Fitur 2 (Folder Output Tema `themes_output/`).

### [v2610.001] - 2026-10-26
- Inisialisasi awal repositori `skill-opensid`.
