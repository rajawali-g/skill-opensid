# Matriks Versi & Kompatibilitas OpenSID

Matriks ketergantungan sistem dan kapabilitas tema per versi OpenSID Free:

| Komponen | OpenSID v22.x | OpenSID v23.x | OpenSID v24.x |
|---|---|---|---|
| Framework Backend | CodeIgniter 3 | CI3 / Laravel Hybrid | Laravel / CI Modular |
| Versi PHP Minimum | PHP 7.4 | PHP 8.0 | PHP 8.1 / 8.2 |
| Engine View Tema | Native PHP View | Blade Engine | Blade Engine (`theme::`) |
| Direktori Tema | `themes/` | `themes/` | `themes/` |
| Override Pengguna | `desa/themes/` | `desa/themes/` | `desa/themes/` |
| Format Konfigurasi | `config.json` | `config.json` | `config.json` |
| Dukungan Widget Dinamis | Terbatas | Penuh (`@includeIf`) | Penuh (`@includeIf`) |
