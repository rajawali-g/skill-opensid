# Arsitektur Resmi Tema OpenSID (Hasil Bedah Tema Default: Esensi & Natra)

Dokumen ini disusun berdasarkan analisis langsung terhadap 2 tema resmi standar OpenSID (**Esensi** & **Natra**) yang berada di folder `standard/`.

---

## 1. Struktur Pustaka & Direktori Tema Standar

Setiap tema OpenSID dikemas dalam sebuah folder induk (yang juga menjadi nama paket ZIP):

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
│       ├── commons/                  # Komponen umum & pemanggil asset pihak ketiga
│       ├── layouts/                  # Layout turunan (full-content, left/right sidebar)
│       ├── partials/                 # Partial halaman & modul-modul OpenSID
│       └── widgets/                  # Seluruh widget sidebar dinamis OpenSID
├── config.json                       # Konfigurasi opsi tema di Web Admin OpenSID
├── composer.json                     # Metadata library Composer tema
├── catatan_rilis.md                  # Log perubahan & catatan rilis tema
└── index.html                        # Berkas proteksi direktori (Silence is Golden)
```

---

## 2. Berkas Konfigurasi Manifes

### A. `config.json`
Berkas ini mendefinisikan opsi kustomisasi yang otomatis tampil di menu **Admin OpenSID > Pengaturan Web > Tema**:
```json
[
    {
        "judul": "Warna Dasar Tema",
        "key": "warna_dasar",
        "value": "#2563eb",
        "type": "color-picker",
        "keterangan": "Warna Dasar Tema yang akan digunakan pada website",
        "options": null,
        "readonly": false,
        "group": "Umum"
    },
    {
        "judul": "Jumlah Pembangunan Perhalaman",
        "key": "jumlah_pembangunan_perhalaman",
        "value": 10,
        "type": "input-number",
        "keterangan": "Jumlah pembangunan yang ditampilkan dalam satu halaman",
        "attributes": { "min": 1, "max": 50, "step": 1 },
        "readonly": false,
        "link": true,
        "group": "Pembangunan"
    }
]
```
Tipe input yang didukung OpenSID:
- `color-picker`: Pemilih warna heksadesimal.
- `select`: Dropdown pilihan (`options: {"1": "Ya", "0": "Tidak"}`).
- `input-number`: Angka dengan batasan `min`, `max`, `step`.
- `unggah`: Upload berkas/gambar kustom tema.

### B. `composer.json`
```json
{
    "name": "themes/<nama_tema>",
    "type": "library",
    "description": "Tema OpenSID",
    "license": "GPL-3.0-or-later",
    "keywords": ["Themes", "OpenSID"]
}
```

---

## 3. Template Engine & Namespace Blade (`theme::`)

OpenSID mendaftarkan folder `resources/views/` dari tema aktif ke dalam namespace Blade **`theme::`**.

### Master Entrypoint: `resources/views/template.blade.php`
```blade
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    @include('theme::commons.meta')
    @include('theme::commons.source_css')
    <title>@yield('title')</title>
    @stack('styles')
</head>
<body class="bg-gray-100">
    @include('theme::commons.loading_screen')
    @include('theme::commons.header')

    {{-- Konten layout dinamis dirender di sini --}}
    @yield('layout')

    @include('theme::commons.footer')

    <script src="{{ theme_asset('js/script.min.js') }}"></script>
    @stack('scripts')
</body>
</html>
```

---

## 4. Hirarki Tiga Folder Utama di `resources/views/`

### A. Folder `commons/` (Komponen Pembantu & Head/Foot)
- `meta.blade.php`: Tag meta SEO, Open Graph, deskripsi, favicon desa.
- `header.blade.php`: Bagian kepala website (identitas desa, logo, teks berjalan).
- `footer.blade.php`: Bagian kaki website, copyright, statistik desa, tautan.
- `main_menu.blade.php` & `mobile_menu.blade.php`: Menu navigasi publik desa.
- `pagination.blade.php`: Paginasi artikel dan tabel publik.
- `asset_peta.blade.php`: Pemuatan Leaflet.js CSS & JS untuk WebGIS.
- `asset_highcharts.blade.php`: Pemuatan grafik statistik penduduk.
- `asset_select2.blade.php` & `asset_sweetalert.blade.php`: Library pendukung form publik.

### B. Folder `layouts/` (Struktur Kolom)
Menentukan apakah halaman memakai sidebar atau satu kolom penuh:
- `full-content.blade.php`: Konten penuh tanpa sidebar.
- `right-sidebar.blade.php`: Kolom konten di kiri (66%), sidebar widget di kanan (33%).
- `left-sidebar.blade.php`: Sidebar widget di kiri, kolom konten di kanan.

Contoh `right-sidebar.blade.php`:
```blade
@extends('theme::template')

@section('layout')
    <div class="container mx-auto flex flex-col lg:flex-row gap-5 my-5">
        <main class="lg:w-2/3 w-full bg-white rounded-lg p-5 shadow">
            @yield('content')
        </main>
        <aside class="lg:w-1/3 w-full">
            @include('theme::partials.sidebar')
        </aside>
    </div>
@endsection
```

### C. Folder `partials/` (Modul-Modul Halaman OpenSID)
OpenSID secara otomatis merender view modul sesuai rute URL:
- `apbdesa.blade.php`: Tampilan grafik APBDes transparansi keuangan.
- `article.blade.php` & `artikel/`: Daftar artikel berita, headline, komentar, arsip.
- `slider.blade.php`: Carousel banner/foto berita utama.
- `sidebar.blade.php`: Loop widget dinamis.
- Sub-folder modul:
  - `peta/`: Halaman penuh peta WebGIS desa.
  - `galeri/`: Album foto & video kegiatan desa.
  - `lapak/`: Produk UMKM / Lapak pasar warga desa.
  - `pemerintah/` & `sotk/`: Struktur Organisasi dan Tata Kerja aparatur desa.
  - `pembangunan/`: Daftar proyek pembangunan fisik desa beserta anggaran.
  - `inventaris/`: Aset tanah, gedung, jalan, dan peralatan milik desa.
  - `kesehatan/`: Skor dan chart stunting posyandu desa.
  - `idm/` & `sdgs/`: Indeks Desa Membangun dan capaian SDGs desa.
  - `statistik/`: Grafik statistik umur, pekerjaan, agama, jenis kelamin.
  - `pengaduan/`: Form & daftar aspirasi warga masyarakat.
  - `surat/` & `surat_dinas/`: Layanan mandiri permohonan surat warga.

### D. Folder `widgets/` (Widget Dinamis Sidebar)
Diloop secara dinamis di `partials/sidebar.blade.php` melalui:
```blade
@foreach ($widgetAktif as $widget)
    @includeIf("theme::widgets.{$widget['isi']}", $judul_widget)
@endforeach
```
Daftar berkas widget standar:
1. `aparatur_desa.blade.php` (Foto pamong & jabatan desa)
2. `keuangan.blade.php` (Ringkasan APBDes)
3. `peta_wilayah_desa.blade.php` (Peta kecil lokasi desa)
4. `peta_lokasi_kantor.blade.php` (Titik kantor desa)
5. `agenda.blade.php` (Jadwal kegiatan desa)
6. `galeri.blade.php` (Foto thumbnail kegiatan terbaru)
7. `jam_kerja.blade.php` (Jadwal pelayanan kantor desa)
8. `arsip_artikel.blade.php` (Daftar artikel terpopuler/terbaru)
9. `statistik.blade.php` (Ringkasan jumlah penduduk, KK, bantuan)
10. `statistik_pengunjung.blade.php` (Counter hit pengunjung hari ini & total)
11. `sinergi_program.blade.php` (Banner banner program pemerintah)
12. `media_sosial.blade.php` (Tautan Facebook, Instagram, YouTube desa)
13. `komentar.blade.php` (Komentar terbaru warga)
14. `menu_kategori.blade.php` (Kategori artikel berita)

---

## 5. Helper Function Bawaan OpenSID untuk Tema

| Helper | Fungsi |
| :--- | :--- |
| `theme_asset('path/file')` | Mengambil URL asset tema aktif (`assets/path/file`) |
| `site_url('rute')` | Membentuk URL rute OpenSID |
| `base_url('path')` | URL basis web OpenSID |
| `setting('kunci')` | Mengambil nilai pengaturan OpenSID (`sebutan_desa`, `sebutan_dusun`, dll) |
| `gambar_desa($desa['logo'])` | URL logo desa resmi |
| `gambar_pamong($foto)` | URL foto aparatur / kepala desa |
| `theme_config('kunci')` | Mengambil nilai konfigurasi tema dari `config.json` |
