---
name: opensid
description: >-
  Use this skill when developing, customizing, or troubleshooting OpenSID
  (Sistem Informasi Desa). Covers Laravel modular architecture, CodeIgniter
  legacy patterns, folder desa/ overrides, custom modules, web themes (Natra,
  Esensi), ODT/RTF letter templates, population database schemas, and deployment.
---

# OpenSID Expert Skill

Skill ini membekali agen AI dengan panduan lengkap untuk ekosistem OpenSID (Sistem Informasi Desa).
OpenSID mendukung arsitektur modern berbasis Laravel (OpenSID versi 24.x ke atas) serta kompatibilitas dengan arsitektur CodeIgniter 3 (`donjo-app`).

## Prinsip Utama Pengembangan OpenSID

1. **Folder `desa/` adalah Wilayah Suci**:
   Jangan pernah mengubah langsung file inti sistem jika bisa di-override melalui folder `desa/` (seperti `desa/config/`, `desa/themes/`, `desa/upload/`, `desa/surat/`). Ini memastikan kustomisasi tidak hilang saat aplikasi di-update ke versi rilis terbaru.
2. **Modular Architecture**:
   Fitur baru harus dibangun sebagai modul tersendiri di dalam folder `Modules/<NamaModul>/` mengikuti standar Laravel Modules.
3. **Format Layanan Surat**:
   Template surat menggunakan format dokumen ODT (LibreOffice) atau RTF dengan variabel pengganti kependudukan standar seperti `[nama]`, `[nik]`, dsb.
4. **Privasi & Keamanan Kependudukan**:
   Data penduduk (NIK, No KK) adalah data sensitif. Selalu gunakan hashing, sanitasi input, dan proteksi hak akses berbasis peran (Admin, Operator, Layanan Mandiri).

---

## Navigasi Referensi Teknis

Buka file referensi berikut sesuai dengan kebutuhan tugas Anda:

| Topik / Kebutuhan | File Referensi |
| :--- | :--- |
| **Arsitektur & Struktur Folder** | [references/architecture.md](references/architecture.md) |
| **Pembuatan Modul Kustom** | [references/modules-development.md](references/modules-development.md) |
| **Tema Publik & Tampilan Web** | [references/themes-and-views.md](references/themes-and-views.md) |
| **Layanan Surat & Variabel ODT/RTF** | [references/surat-dan-pelayanan.md](references/surat-dan-pelayanan.md) |
| **Kamus Database Kependudukan** | [references/database-kependudukan.md](references/database-kependudukan.md) |
| **Instalasi, Permission, & Solusi Error** | [references/deployment-troubleshooting.md](references/deployment-troubleshooting.md) |

---

## Alur Kerja Pengembangan Umum

### 1. Membuat Fitur Baru sebagai Modul
1. Pelajari spesifikasi modul di [modules-development.md](references/modules-development.md).
2. Tentukan nama modul dalam PascalCase (contoh: `AspirasiWarga`).
3. Buat struktur:
   - `Modules/AspirasiWarga/Http/Controllers/`
   - `Modules/AspirasiWarga/Models/`
   - `Modules/AspirasiWarga/Routes/web.php`
   - `Modules/AspirasiWarga/Resources/views/`
   - `Modules/AspirasiWarga/Database/Migrations/`

### 2. Membuat Template Surat Baru
1. Periksa daftar kode isian di [surat-dan-pelayanan.md](references/surat-dan-pelayanan.md).
2. Siapkan file template ODT dengan variabel format `[nama_variabel]`.
3. Daftarkan surat melalui menu admin **Layanan Surat > Pengaturan Surat**.

### 3. Mengubah Tampilan Tema Publik
1. Selalu buat sub-tema di `desa/themes/<nama_sub_tema>/` atau duplikasi dari `themes/natra` / `themes/esensi`.
2. Jangan mengedit file di folder vendor atau root `themes/` secara langsung.
3. Pelajari panduan detail di [themes-and-views.md](references/themes-and-views.md).
