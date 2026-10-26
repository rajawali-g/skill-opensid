---
name: opensid
description: >-
  Use this skill when developing, customizing, or troubleshooting OpenSID
  (Sistem Informasi Desa). Covers checking latest OpenSID version from GitHub,
  creating custom themes into themes_output/ with ZIP packager, Laravel modular
  architecture, CodeIgniter legacy patterns, folder desa/ overrides, custom modules,
  web themes (Natra, Esensi), ODT/RTF letter templates, and population database schemas.
---

# OpenSID Expert Skill

Skill ini membekali agen AI dengan panduan lengkap untuk ekosistem OpenSID (Sistem Informasi Desa).
OpenSID mendukung arsitektur modern berbasis Laravel (OpenSID versi 24.x ke atas) serta kompatibilitas dengan arsitektur CodeIgniter 3 (`donjo-app`).

## Prinsip Utama Pengembangan OpenSID

1. **Informasi Versi Resmi**:
   Selalu rujuk versi resmi OpenSID umum (non-premium) terkini di [references/opensid-version-info.md](references/opensid-version-info.md). Data ini dapat disinkronkan langsung dari GitHub via skrip `fetch_opensid_info.py`.
2. **Folder Output Pembuatan Tema (`themes_output/`)**:
   Setiap pembuatan tema kustom web desa harus ditempatkan di folder `themes_output/<nama_tema>/` dan dikemas menjadi berkas ZIP siap unggah di `themes_output/<nama_tema>.zip`.
3. **Folder `desa/` adalah Wilayah Suci**:
   Jangan pernah mengubah langsung file inti sistem jika bisa di-override melalui folder `desa/` (seperti `desa/config/`, `desa/themes/`, `desa/upload/`, `desa/surat/`). Ini memastikan kustomisasi tidak hilang saat aplikasi di-update ke versi rilis terbaru.
4. **Modular Architecture**:
   Fitur baru harus dibangun sebagai modul tersendiri di dalam folder `Modules/<NamaModul>/` mengikuti standar Laravel Modules.
5. **Format Layanan Surat**:
   Template surat menggunakan format dokumen ODT (LibreOffice) atau RTF dengan variabel pengganti kependudukan standar seperti `[nama]`, `[nik]`, dsb.
6. **Privasi & Keamanan Kependudukan**:
   Data penduduk (NIK, No KK) adalah data sensitif. Selalu gunakan hashing, sanitasi input, dan proteksi hak akses berbasis peran (Admin, Operator, Layanan Mandiri).

---

## Navigasi Referensi Teknis

Buka file referensi berikut sesuai dengan kebutuhan tugas Anda:

| Topik / Kebutuhan | File Referensi |
| :--- | :--- |
| **Info Versi & Stack Resmi (GitHub)** | [references/opensid-version-info.md](references/opensid-version-info.md) |
| **Arsitektur Resmi Tema (Esensi & Natra)** | [references/arsitektur-tema-opensid.md](references/arsitektur-tema-opensid.md) |
| **Tema Publik & Folder `themes_output/`** | [references/themes-and-views.md](references/themes-and-views.md) |
| **Arsitektur & Struktur Folder Sistem** | [references/architecture.md](references/architecture.md) |
| **Pembuatan Modul Kustom** | [references/modules-development.md](references/modules-development.md) |
| **Layanan Surat & Variabel ODT/RTF** | [references/surat-dan-pelayanan.md](references/surat-dan-pelayanan.md) |
| **Kamus Database Kependudukan** | [references/database-kependudukan.md](references/database-kependudukan.md) |
| **Instalasi, Permission, & Solusi Error** | [references/deployment-troubleshooting.md](references/deployment-troubleshooting.md) |

---

## Alur Kerja Utama

### 1. Memeriksa / Memperbarui Info Versi OpenSID
Jika pengguna bertanya seputar versi OpenSID, spesifikasi backend/frontend, atau ingin memperbarui data:
1. Baca file [references/opensid-version-info.md](references/opensid-version-info.md) atau data JSON di [data/opensid_latest_info.json](data/opensid_latest_info.json).
2. Jika perlu sinkronisasi langsung dari GitHub API:
   ```powershell
   python .agents/skills/opensid/scripts/fetch_opensid_info.py
   # atau via shortcut di root workspace:
   .\update-opensid-info.ps1
   ```

### 2. Membuat Tema Baru ke Folder `themes_output/`
Jika pengguna meminta membuat atau memodifikasi tema:
1. Gunakan skrip generator tema:
   ```powershell
   .\manage-theme.ps1 new -Name "nama-tema" -Title "Judul Tema Desa"
   ```
2. Modifikasi file di `themes_output/<nama-tema>/` (layouts, css, partials artikel, apbdes, peta).
3. Kemas ke file ZIP siap upload:
   ```powershell
   .\manage-theme.ps1 package -Name "nama-tema"
   ```
4. Berkas `themes_output/<nama-tema>.zip` siap diunggah melalui menu admin OpenSID: **Pengaturan Web > Tema > Unggah Tema**.

### 3. Membuat Fitur Baru sebagai Modul
1. Pelajari spesifikasi modul di [modules-development.md](references/modules-development.md).
2. Buat struktur modul di `Modules/<NamaModul>/` lengkap dengan Controller, Model, Migration, dan Routes.

### 4. Membuat Template Surat Baru
1. Periksa daftar kode isian di [surat-dan-pelayanan.md](references/surat-dan-pelayanan.md).
2. Siapkan file template ODT dengan variabel format `[nama_variabel]`.
