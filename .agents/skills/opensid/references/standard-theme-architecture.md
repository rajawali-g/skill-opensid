# Arsitektur Tema Standar OpenSID (Free / Non-Premium)

Berdasarkan analisis tema default `natra` dan `esensi`:

## 1. Engine & Direktori
- **Engine View**: Laravel Blade (`*.blade.php`).
- **Namespace View**: `theme::`
- **Lokasi Tema**: `themes/<nama_tema>/`
- **Override Pengguna**: `desa/themes/<nama_tema>/`

## 2. Struktur Direktori Standar
```text
<nama_tema>/
├── assets/
│   ├── css/
│   ├── js/
│   └── images/
├── resources/
│   └── views/
│       ├── commons/
│       │   ├── header.blade.php
│       │   ├── footer.blade.php
│       │   ├── meta.blade.php
│       │   └── navbar.blade.php
│       ├── layouts/
│       │   └── index.blade.php
│       ├── partials/
│       │   ├── artikel.blade.php
│       │   ├── slider.blade.php
│       │   └── pagination.blade.php
│       ├── widgets/
│       └── template.blade.php
├── config.json
├── composer.json
├── catatan_rilis.md
└── index.html
```

## 3. Metadata Tema
- `config.json`: Konfigurasi opsi kustomisasi di Admin Web OpenSID.
- `composer.json`: Type `opensid-theme` atau `library`.
