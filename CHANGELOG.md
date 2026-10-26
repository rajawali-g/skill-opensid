# Changelog - Skill OpenSID

Format pencatatan perubahan berpedoman pada sistem **TAG & RELEASE**:
- **Format Versi**: `v[TAG].[RELEASE]` (Contoh: `v2610.001`)
- **TAG**: Tahun (2 digit) + Bulan (2 digit) -> `2610` (Oktober 2026)
- **RELEASE**: Nomor urut rilis berurutan 3 digit di bulan tersebut (`001`, `002`, `003`...)

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
