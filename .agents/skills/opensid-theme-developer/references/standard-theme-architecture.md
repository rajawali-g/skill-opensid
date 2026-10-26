# Arsitektur Tema Standar OpenSID (Free / Non-Premium)

Dokumen ini adalah referensi teknis arsitektur tema resmi OpenSID (berdasarkan analisis tema default **Esensi** & **Natra**).

---

## 1. Engine & Direktori

- **Engine View**: Laravel Blade (`*.blade.php`).
- **Namespace View**: `theme::` (Wajib digunakan di semua `@include` dan `@extends`).
- **Lokasi Tema Sistem**: `themes/<nama_tema>/`
- **Lokasi Override Desa**: `desa/themes/<nama_tema>/`

---

## 2. Struktur Pustaka & Direktori Tema Standar

Setiap tema OpenSID wajib mengikuti struktur direktori berikut (folder induk harus bernama sama dengan slug tema):

```text
<nama_tema>/
├── assets/                           # Seluruh asset statis frontend
│   ├── css/                          # Stylesheet (style.css, custom.css, vendor)
│   ├── js/                           # Javascript (script.js, helper.js, pagination.js)
│   ├── images/                       # Gambar statis, logo placeholder, background
│   └── thumbnail/                    # Preview tema di Web Admin OpenSID
│       └── preview-1.jpg             # Thumbnail wajib (tampil di daftar tema admin)
├── resources/
│   └── views/                        # Seluruh template tampilan berbasis LARAVEL BLADE (*.blade.php)
│       ├── template.blade.php        # MASTER LAYOUT ENTRY POINT
│       ├── menu_not_active.blade.php # Halaman saat modul dinonaktifkan
│       ├── commons/                  # Komponen umum & meta header/footer
│       │   ├── header.blade.php      # Header & meta tags
│       │   ├── footer.blade.php      # Footer & copyright
│       │   ├── meta.blade.php        # OpenGraph, SEO, favicon
│       │   └── navbar.blade.php      # Navigasi & menu bertingkat
│       ├── layouts/                  # Layout turunan
│       │   └── index.blade.php       # Layout default wrapper
│       ├── partials/                 # Komponen parsial konten
│       │   ├── artikel.blade.php     # Template single & list artikel
│       │   ├── slider.blade.php      # Carousel berita / kegiatan
│       │   └── pagination.blade.php  # Paginasi halaman
│       └── widgets/                  # Template widget dinamis OpenSID
│           ├── aparatur_desa.blade.php
│           ├── agenda.blade.php
│           ├── galeri.blade.php
│           ├── statistik.blade.php
│           └── arsip_artikel.blade.php
├── config.json                       # Konfigurasi opsi tema di Web Admin OpenSID
├── composer.json                     # Metadata library Composer tema
├── catatan_rilis.md                  # Log perubahan & catatan rilis tema
└── index.html                        # Berkas proteksi direktori (Silence is Golden)
```

---

## 3. Berkas Manifes Tema

### A. `config.json`
Berkas ini mendefinisikan form opsi kustomisasi yang otomatis tampil di menu **Admin OpenSID > Pengaturan Web > Tema**:
```json
[
    {
        "judul": "Warna Dasar Tema",
        "key": "warna_dasar",
        "value": "#2563eb",
        "type": "color-picker",
        "keterangan": "Warna dasar utama website desa",
        "options": null,
        "readonly": false,
        "group": "Umum"
    },
    {
        "judul": "Tampilkan Slider Beranda",
        "key": "tampilkan_slider",
        "value": "1",
        "type": "select",
        "options": {
            "1": "Ya",
            "0": "Tidak"
        },
        "readonly": false,
        "group": "Beranda"
    }
]
```

Nilai opsi ini dapat diakses di template Blade melalui helper tema OpenSID.

### B. `composer.json`
Mendefinisikan tipe paket tema:
```json
{
    "name": "opensid/<nama-tema>",
    "description": "Tema untuk OpenSID",
    "type": "opensid-theme",
    "license": "GPL-3.0-or-later",
    "authors": [
        {
            "name": "OpenSID Theme Developer",
            "email": "info@opendesa.id"
        }
    ],
    "require": {}
}
```

### C. `catatan_rilis.md`
Mencatat riwayat perubahan dan versi tema:
```markdown
# Catatan Rilis Tema

## v1.0.0
- Rilis perdana tema.
- Implementasi layout responsif mobile-first.
- Integrasi widget aparatur, statistik, dan berita.
```

---

## 4. Pola Pemanggilan Blade & Namespace `theme::`

Semua pemanggilan view wajib menggunakan prefix namespace `theme::`:

1. **Memuat Komponen Header & Navbar**:
   ```blade
   @include('theme::commons.header')
   @include('theme::commons.navbar')
   ```

2. **Memuat Widget Dinamis (Wajib menggunakan `@includeIf`)**:
   ```blade
   @if (!empty($widgets))
       @foreach ($widgets as $widget)
           @php
               $judul_widget = [
                   'judul_widget' => $widget['judul']
               ];
           @endphp
           @includeIf("theme::widgets.{$widget['isi']}", $judul_widget)
       @endforeach
   @endif
   ```

3. **Memuat Aset Statis**:
   ```blade
   <link rel="stylesheet" href="{{ base_url("themes/{$theme}/assets/css/style.css") }}">
   <script src="{{ base_url("themes/{$theme}/assets/js/script.js") }}"></script>
   ```

---

## 5. Standar Pengemasan ZIP
Paket distribusi tema wajib berbentuk ZIP di mana root di dalam ZIP adalah direktori `<nama_tema>/`:
```text
nama-tema.zip
└── nama-tema/
    ├── assets/
    ├── resources/
    ├── config.json
    ├── composer.json
    ├── catatan_rilis.md
    └── index.html
```
Ketika diekstrak ke folder `themes/` pada instalasi OpenSID, file langsung berada di `themes/nama-tema/`.
