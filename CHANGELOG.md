# Changelog - Skill OpenSID

Format pencatatan perubahan berpedoman pada sistem **TAG & RELEASE**:
- **Format Versi**: `v[TAG].[RELEASE]` (Contoh: `v2610.004`)
- **TAG**: Tahun (2 digit) + Bulan (2 digit) -> `2610` (Oktober 2026)
- **RELEASE**: Nomor urut rilis berurutan 3 digit di bulan tersebut (`001`, `002`, `003`...)

---

## [v2610.004] - 2026-10-26

### Added
- Pembangunan 3 tema dasar resmi siap pakai di folder `themes_output/`:
  1. **`tema-pedesaan-klasik`** (`themes_output/tema-pedesaan-klasik.zip`): Kearifan lokal, agraris, palet hangat hijau daun & kayu, ramah warga lansia.
  2. **`tema-desa-modern`** (`themes_output/tema-desa-modern.zip`): Tata kelola pemerintahan bersih, sleek, elegan, kartu soft drop shadows.
  3. **`tema-desa-digital`** (`themes_output/tema-desa-digital.zip`): Smart village, live stats counter bar, kartu glassmorphism, aksen neon cyan.
- Skrip builder otomatis `build_three_themes.py`.
- Pembaruan dokumen panduan tema di `references/themes-and-views.md`.

---

## [v2610.003] - 2026-10-26

### Added
- Bedah arsitektur resmi tema OpenSID dari tema default `esensi` dan `natra` di folder `standard/`.
- Dokumentasi teknis `references/arsitektur-tema-opensid.md` (Laravel Blade, `theme::` namespace, `config.json`, `composer.json`, `commons/`, `layouts/`, `partials/`, `widgets/`).
- Standardisasi generator `theme_manager.py` ke Laravel Blade.

---

## [v2610.002] - 2026-10-26

### Added
- **Fitur 1 (Update Informasi Versi OpenSID dari GitHub)**:
  - Skrip pengambil rilis GitHub API: `fetch_opensid_info.py`.
  - Berkas data terstruktur `data/opensid_latest_info.json`.
  - Dokumen referensi dinamis `references/opensid-version-info.md` yang memuat spesifikasi rilis terkini (`v2607.0.1`), PHP `^8.1`, ekstensi wajib, backend Laravel + CI, dan frontend AdminLTE + Leaflet.
  - Shortcut terminal di root workspace: `update-opensid-info.ps1`.
- **Fitur 2 (Folder Khusus Output Pembuatan Tema & Packager ZIP)**:
  - Folder khusus hasil kreasi tema: `themes_output/`.
  - Skrip utilitas generator, ZIP packager, dan deployer tema: `theme_manager.py` dan `manage-theme.ps1`.
  - Contoh tema starter: `themes_output/tema-starter-minsel` beserta paket kompresi siap pasang `themes_output/tema-starter-minsel.zip`.
  - Panduan lengkap arsitektur tema dan cara unggah via panel admin OpenSID di `references/themes-and-views.md`.

---

## [v2610.001] - 2026-10-26

### Added
- Inisialisasi struktur repositori resmi `skill-opensid` di GitHub.
- Berkas instruksi utama AI: `.agents/skills/opensid/SKILL.md`.
- Modul referensi teknis:
  - `architecture.md`: Struktur folder OpenSID Modern Laravel + CodeIgniter, aturan folder `desa/`.
  - `modules-development.md`: Panduan membuat modul kustom OpenSID (`Modules/<NamaModul>`).
  - `themes-and-views.md`: Panduan membuat dan override tema publik (Natra / Esensi).
  - `surat-dan-pelayanan.md`: Kamus lengkap kode isian surat ODT/RTF kependudukan & alur TTE.
  - `database-kependudukan.md`: Relasi tabel kependudukan, wilayah cluster desa, dan konfigurasi.
  - `deployment-troubleshooting.md`: Konfigurasi server (Laragon/Linux), PHP 8.1/8.2, penanganan permission.
- Skrip otomatisasi versi & release: `release.ps1`.
- Berkas contoh implementasi:
  - `examples/contoh-modul.md`
  - `examples/template-surat-keterangan.md`
