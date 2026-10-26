# 🏛️ Skill OpenSID untuk Antigravity AI

[![GitHub Repository](https://img.shields.io/badge/GitHub-rajawali--g%2Fskill--opensid-blue?logo=github)](https://github.com/rajawali-g/skill-opensid)
[![Release Version](https://img.shields.io/badge/Release-v2610.001-brightgreen)](#-riwayat-perubahan-changelog)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Target Platform](https://img.shields.io/badge/Platform-Antigravity%20AI-blueviolet)](https://antigravity.google/)

Paket keahlian (*AI Skill*) terlengkap untuk agen **Antigravity AI** dalam memandu, mengotomasi, dan mempercepat pengembangan ekosistem **OpenSID** (Sistem Informasi Desa berbasis open source terpopuler di Indonesia).

---

## 📌 Daftar Isi
- [Tentang Skill OpenSID](#-tentang-skill-opensid)
- [Struktur & Cakupan Skill](#-struktur--cakupan-skill)
- [Sistem Penomoran Versi (TAG & RELEASE)](#-sistem-penomoran-versi-tag--release)
- [Skrip Otomatisasi Release](#-skrip-otomatisasi-release)
- [Panduan Integrasi ke GitHub](#-panduan-integrasi-ke-github)
- [Cara Pemasangan di Antigravity](#-cara-pemasangan-di-antigravity)
- [Riwayat Perubahan (Changelog)](#-riwayat-perubahan-changelog)

---

## 💡 Tentang Skill OpenSID

Skill ini dirancang khusus untuk memahami arsitektur ganda OpenSID (Modern **Laravel Modular Architecture** dan Legacy **CodeIgniter 3 donjo-app**). Memberikan asisten AI pemahaman presisi mengenai:
- Aturan modifikasi file desa tanpa merusak integritas update sistem (`desa/config`, `desa/themes`, `desa/upload`).
- Pembuatan modul kustom (`Modules/<NamaModul>/`) lengkap dengan Controllers, Eloquent Models, Migrations, dan Routes.
- Kustomisasi template layanan surat desa berformat **ODT / RTF** dengan pemetaan variabel kode isian kependudukan resmi.
- Perancangan & modifikasi tema publik web desa (sub-tema turunan Natra, Esensi, dsb).
- Struktur kamus data database kependudukan (`tweb_penduduk`, `tweb_keluarga`, `tweb_wil_clusterdesa`).

---

## 📂 Struktur & Cakupan Skill

```text
skill-opensid/
├── .agents/skills/opensid/           # Direktori skill utama untuk Antigravity AI
│   ├── SKILL.md                      # Prompt utama & panduan aktivasi agen
│   ├── references/                   # Dokumentasi teknis terperinci
│   │   ├── architecture.md           # Arsitektur sistem (Laravel + CodeIgniter + folder desa/)
│   │   ├── modules-development.md    # Pembuatan modul, controller, model, migration
│   │   ├── themes-and-views.md       # Modifikasi tema publik (Natra, Esensi, layout, widget)
│   │   ├── surat-dan-pelayanan.md    # Kamus kode variabel surat ODT/RTF & alur TTE
│   │   ├── database-kependudukan.md  # Relasi tabel kependudukan, wilayah, dan konfigurasi
│   │   └── deployment-troubleshooting.md # Instalasi (Laragon/Linux), error umum, permission
│   └── examples/
│       ├── contoh-modul.md           # Contoh modul starter
│       └── template-surat-keterangan.md # Contoh kode isian template ODT
├── release.ps1                       # Skrip otomatis penomoran versi TAG & RELEASE
├── README.md                         # Dokumentasi utama proyek & riwayat versi
└── CHANGELOG.md                      # Log detail seluruh perubahan versi
```

---

## 🏷️ Sistem Penomoran Versi (TAG & RELEASE)

Sistem penomoran versi pada repositori ini menggunakan format otomatis berbasis waktu dan nomor urut:

$$\mathbf{v[TAG].[RELEASE]}$$

### 1. Definisi Komponen
- **`TAG` (Tahun & Bulan)**:
  Format 4 digit angka `YYMM` yang menunjukkan tahun dan bulan pembuatan/pembaruan rilis:
  - `26` = Tahun 2026
  - `10` = Bulan Oktober
  - *Hasil TAG:* **`2610`**
- **`RELEASE` (Nomor Urut Versi)**:
  Format 3 digit angka berurutan `001`, `002`, `003`, dst. Nomor ini dihitung dari jumlah rilis yang diterbitkan dalam periode bulan tersebut.

### 2. Contoh Penomoran
| Periode Rilis | Nomor Urut | Hasil TAG & RELEASE | Keterangan |
| :--- | :---: | :---: | :--- |
| Oktober 2026 | Rilis ke-1 | `v2610.001` | Inisialisasi awal repositori & paket skill |
| Oktober 2026 | Rilis ke-2 | `v2610.002` | Penambahan referensi WebGIS & perbaikan template ODT |
| November 2026| Rilis ke-1 | `v2611.001` | Rilis baru di bulan November (nomor urut kembali ke 001) |

---

## 🚀 Skrip Otomatisasi Release

Untuk memudahkan pembaruan tanpa perlu menghitung nomor urut secara manual, gunakan skrip PowerShell `release.ps1` yang disertakan di repositori ini.

### Cara Menjalankan Rilis Baru:
```powershell
# Jalankan rilis otomatis dengan pesan perubahan
.\release.ps1 -Message "Penambahan modul kustom dan kamus database kependudukan"
```

### Yang Dikerjakan Skrip Secara Otomatis:
1. Mendeteksi tanggal saat ini dan membentuk format `TAG` (`YYMM`).
2. Memeriksa Git Tags terakhir untuk menentukan nomor `RELEASE` berikutnya (`001`, `002`, dst).
3. Memperbarui badge versi di [README.md](file:///d:/project_opensid/README.md) dan mencatat entry di [CHANGELOG.md](file:///d:/project_opensid/CHANGELOG.md).
4. Melakukan `git commit` dengan pesan perubahan.
5. Membuat Git Tag resmi (misal `v2610.001`).
6. Melakukan `git push origin main --tags` langsung ke GitHub.

---

## 🔗 Panduan Integrasi ke GitHub

Repositori resmi: [https://github.com/rajawali-g/skill-opensid](https://github.com/rajawali-g/skill-opensid)

### Langkah Inisialisasi Pertama Kali:
```powershell
# 1. Buka folder proyek
cd d:\project_opensid

# 2. Inisialisasi Git
git init
git branch -M main

# 3. Hubungkan ke Remote Repository GitHub
git remote add origin https://github.com/rajawali-g/skill-opensid.git

# 4. Tambahkan seluruh berkas dan commit perdana
git add .
git commit -m "feat: inisialisasi skill opensid v2610.001"

# 5. Buat Tag Perdana
git tag -a v2610.001 -m "Release v2610.001: Inisialisasi Skill OpenSID"

# 6. Push ke GitHub
git push -u origin main --tags
```

---

## 💻 Cara Pemasangan di Antigravity

### 1. Pemasangan per Workspace (Lokal Proyek)
Letakkan folder skill di dalam proyek Anda pada path:
```text
<root_project>/.agents/skills/opensid/
```
Antigravity akan otomatis mendeteksi skill saat proyek dibuka.

### 2. Pemasangan Global (Seluruh Proyek di PC Anda)
Salin folder `opensid` ke direktori konfigurasi global Antigravity:
```powershell
Copy-Item -Recurse -Force ".agents\skills\opensid" "$env:USERPROFILE\.gemini\config\skills\opensid"
```
Setelah disalin, skill akan aktif secara permanen di setiap percakapan dan sesi Antigravity.

---

## 📝 Riwayat Perubahan (Changelog)

### [v2610.001] - 2026-10-26
- **TAG**: `2610` | **RELEASE**: `001`
- **Fitur Utama**:
  - Inisialisasi repositori resmi [rajawali-g/skill-opensid](https://github.com/rajawali-g/skill-opensid).
  - Implementasi struktur Skill Antigravity (`SKILL.md`).
  - Penyusunan panduan referensi arsitektur OpenSID (Laravel Modular & CodeIgniter legacy).
  - Panduan pengembangan modul kustom OpenSID.
  - Kamus kode variabel template surat desa ODT/RTF dan alur TTE.
  - Kamus data tabel kependudukan (`tweb_penduduk`, `tweb_keluarga`, `tweb_wil_clusterdesa`).
  - Panduan kustomisasi tema publik desa (turunan tema Natra / Esensi).
  - Panduan instalasi dan troubleshooting lingkungan web server (Laragon, Linux, PHP 8.1/8.2).
  - Pembuatan skrip otomatisasi release berbasis PowerShell (`release.ps1`).
