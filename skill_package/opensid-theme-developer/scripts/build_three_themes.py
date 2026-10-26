#!/usr/bin/env python3
"""
build_three_themes.py
Membangun 3 tema dasar OpenSID berstandar resmi Laravel Blade:
1. tema-pedesaan-klasik (Nuansa hangat, kearifan lokal, agraris, bersahabat)
2. tema-desa-modern    (Clean, profesional, tata kelola rapi, corporate-gov)
3. tema-desa-digital   (Smart village, futuristik, glassmorphism, data-driven)
"""

import os
import json
import zipfile

WORKSPACE_ROOT = r"d:\project_opensid"
OUTPUT_DIR = os.path.join(WORKSPACE_ROOT, "themes_output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

SILENCE_HTML = "<!DOCTYPE html><html><head><title>403 Forbidden</title></head><body><p>Directory access is forbidden.</p></body></html>"

def create_theme_files(slug, title, author, description, config_items, theme_css, theme_js, extra_views=None):
    theme_folder = os.path.join(OUTPUT_DIR, slug)
    print(f"[*] Meracik tema: {title} ({slug})...")

    # Folder struktur resmi
    subdirs = [
        "assets/css",
        "assets/js",
        "assets/images",
        "assets/thumbnail",
        "resources/views/commons",
        "resources/views/layouts",
        "resources/views/partials/artikel",
        "resources/views/partials/peta",
        "resources/views/widgets"
    ]
    for sub in subdirs:
        os.makedirs(os.path.join(theme_folder, sub), exist_ok=True)

    # 1. config.json
    with open(os.path.join(theme_folder, "config.json"), "w", encoding="utf-8") as f:
        json.dump(config_items, f, indent=4, ensure_ascii=False)

    # 2. composer.json
    composer_json = {
        "name": f"themes/{slug}",
        "type": "library",
        "description": f"{title} untuk OpenSID",
        "license": "GPL-3.0-or-later",
        "keywords": ["Themes", "OpenSID", slug],
        "authors": [{"name": author, "email": "desa@minselkab.go.id"}]
    }
    with open(os.path.join(theme_folder, "composer.json"), "w", encoding="utf-8") as f:
        json.dump(composer_json, f, indent=4, ensure_ascii=False)

    # 3. catatan_rilis.md
    with open(os.path.join(theme_folder, "catatan_rilis.md"), "w", encoding="utf-8") as f:
        f.write(f"Catatan Rilis v1.0.0 ({title}) :\n\n### TEKNIS :\n1. Inisialisasi arsitektur Laravel Blade OpenSID.\n2. Styling tema khusus: {description}.\n3. Mendukung namespace theme:: dan widget aktif dinamis.\n")

    # 4. index.html
    with open(os.path.join(theme_folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(SILENCE_HTML)
    with open(os.path.join(theme_folder, "assets", "index.html"), "w", encoding="utf-8") as f:
        f.write(SILENCE_HTML)

    # 5. assets/css/style.css & assets/js/script.js
    with open(os.path.join(theme_folder, "assets", "css", "style.css"), "w", encoding="utf-8") as f:
        f.write(theme_css)
    with open(os.path.join(theme_folder, "assets", "js", "script.js"), "w", encoding="utf-8") as f:
        f.write(theme_js)

    # 6. resources/views/
    views = extra_views or {}
    for rel_path, content in views.items():
        full_p = os.path.join(theme_folder, "resources", "views", rel_path)
        os.makedirs(os.path.dirname(full_p), exist_ok=True)
        with open(full_p, "w", encoding="utf-8") as f:
            f.write(content)

    # 7. Package ke ZIP
    zip_path = os.path.join(OUTPUT_DIR, f"{slug}.zip")
    if os.path.exists(zip_path):
        os.remove(zip_path)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(theme_folder):
            for file in files:
                abs_f = os.path.join(root, file)
                rel_f = os.path.relpath(abs_f, theme_folder)
                zf.write(abs_f, os.path.join(slug, rel_f))
    size_kb = round(os.path.getsize(zip_path) / 1024, 1)
    print(f"[+] Selesai! Berkas ZIP: {zip_path} ({size_kb} KB)\n")

# ==============================================================================
# TEMA 1: PEDESAAN KLASIK
# ==============================================================================
def build_tema_pedesaan():
    slug = "tema-pedesaan-klasik"
    title = "Tema Pedesaan Klasik"
    author = "Diskominfo - Tim Budaya Desa"
    description = "Tema pedesaan bernuansa hangat, agraris, ramah warga, dan menjunjung kearifan lokal"

    config_items = [
        {
            "judul": "Warna Aksen Alam",
            "key": "warna_aksen",
            "value": "#15803d",
            "type": "color-picker",
            "keterangan": "Warna aksen hijau daun / alam pedesaan",
            "group": "Umum"
        },
        {
            "judul": "Salam Sambutan Kepala Desa",
            "key": "salam_kades",
            "value": "Tabea! Selamat datang di website resmi desa kami. Mari bersama membangun desa yang tenteram, rukun, dan sejahtera.",
            "type": "text",
            "keterangan": "Teks sambutan hangat di bagian atas website",
            "group": "Sambutan"
        },
        {
            "judul": "Jumlah Berita Per Halaman",
            "key": "jumlah_berita_perhalaman",
            "value": 6,
            "type": "input-number",
            "attributes": {"min": 3, "max": 18, "step": 3},
            "group": "Berita"
        }
    ]

    css = """/* ==============================================================
   Tema Pedesaan Klasik - OpenSID
   Palet: Warm Earth, Forest Green, Cream Sand, Warm Wood
============================================================== */
:root {
    --color-primary: #15803d;       /* Hijau Daun Alami */
    --color-wood: #78350f;          /* Cokelat Kayu */
    --color-wood-dark: #451a03;
    --color-cream: #fefce8;         /* Krem Jerami */
    --color-bg: #fcfbf7;            /* Latar Belakang Hangat */
    --color-surface: #ffffff;
    --color-text: #292524;          /* Warm Charcoal */
    --color-muted: #78716c;
    --color-border: #e7e5e4;
}

body {
    background-color: var(--color-bg);
    color: var(--color-text);
    font-family: 'Segoe UI', Georgia, serif;
    margin: 0;
    line-height: 1.7;
}

.top-bar-pedesaan {
    background: linear-gradient(to right, #451a03, #78350f);
    color: #fef08a;
    font-size: 0.85rem;
    padding: 6px 0;
    border-bottom: 2px solid #b45309;
}

.header-pedesaan {
    background: #ffffff url('data:image/svg+xml;utf8,<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><g fill="%23f5f5f4" fill-opacity="0.6" fill-rule="evenodd"><path d="M0 40L40 0H20L0 20M40 40V20L20 40"/></g></svg>');
    border-bottom: 3px double var(--color-wood);
}

.logo-frame {
    border: 3px solid #d97706;
    border-radius: 50%;
    padding: 3px;
    background: #ffffff;
}

.navbar-pedesaan {
    background: var(--color-primary);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.nav-item-pedesaan {
    color: #f0fdf4;
    text-decoration: none;
    padding: 10px 18px;
    font-weight: 600;
    font-size: 0.95rem;
    border-radius: 6px;
    transition: background-color 0.2s;
}
.nav-item-pedesaan:hover {
    background-color: #166534;
    color: #ffffff;
}

.card-klasik {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-top: 4px solid var(--color-wood);
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.04);
}

.card-title-klasik {
    color: var(--color-wood-dark);
    font-family: Georgia, serif;
    border-bottom: 1px dashed var(--color-border);
    padding-bottom: 8px;
    margin-bottom: 12px;
}

.btn-mandiri-klasik {
    background: linear-gradient(135deg, #d97706, #b45309);
    color: #ffffff !important;
    padding: 8px 18px;
    border-radius: 6px;
    font-weight: bold;
    text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    box-shadow: 0 2px 4px rgba(0,0,0,0.15);
}
.btn-mandiri-klasik:hover {
    background: linear-gradient(135deg, #b45309, #92400e);
}
"""

    js = """document.addEventListener('DOMContentLoaded', function() {
    console.log('[Tema Pedesaan Klasik] Diaktifkan.');
    var petaElem = document.getElementById('peta-desa-klasik');
    if (petaElem && typeof L !== 'undefined') {
        var map = L.map('peta-desa-klasik').setView([-1.2, 124.8], 12);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);
    }
});
"""

    views = {
        "template.blade.php": """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    @include('theme::commons.meta')
    @include('theme::commons.source_css')
    <title>@yield('title', $heading ?? $desa['nama_desa']) - Website Resmi Desa</title>
    @stack('styles')
</head>
<body>
    @include('theme::commons.header')

    <div class="container mx-auto px-4 my-6">
        @yield('layout')
    </div>

    @include('theme::commons.footer')
    <script src="{{ theme_asset('js/script.js') }}"></script>
    @stack('scripts')
</body>
</html>
""",
        "commons/meta.blade.php": """<meta name="description" content="Website Desa <?= $desa['nama_desa']; ?> bernuansa kearifan lokal pedesaan.">
<link rel="shortcut icon" href="<?= gambar_desa($desa['logo']); ?>">
""",
        "commons/source_css.blade.php": """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
<link rel="stylesheet" href="{{ theme_asset('css/style.css') }}">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>
""",
        "commons/header.blade.php": """<!-- Top Bar Sambutan Desa -->
<div class="top-bar-pedesaan">
    <div class="container mx-auto px-4 flex justify-between items-center">
        <span>🌾 Kearifan Lokal & Guyub Rukun Warga</span>
        <span><?= date('l, d F Y'); ?></span>
    </div>
</div>

<!-- Header Identitas Desa -->
<header class="header-pedesaan py-5">
    <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-4">
        <div class="flex items-center space-x-4">
            <img src="<?= gambar_desa($desa['logo']); ?>" alt="Logo Desa" class="h-16 w-16 logo-frame">
            <div>
                <span class="text-xs font-bold uppercase tracking-wider text-green-800">Pemerintah Desa</span>
                <h1 class="text-2xl font-bold text-yellow-900 leading-tight"><?= $desa['nama_desa']; ?></h1>
                <p class="text-sm text-gray-600">Kecamatan <?= $desa['nama_kecamatan']; ?>, Kabupaten <?= $desa['nama_kabupaten']; ?></p>
            </div>
        </div>
        <div class="text-right hidden lg:block italic text-sm text-yellow-950 bg-yellow-50 p-3 rounded border border-yellow-200 max-w-md">
            "<?= $salam_kades ?? 'Tabea! Bersama Membangun Desa yang Berbudaya, Rukun, dan Sejahtera.'; ?>"
        </div>
    </div>
</header>

<!-- Navigasi Utama -->
<nav class="navbar-pedesaan">
    <div class="container mx-auto px-4 flex justify-between items-center py-2">
        <div class="flex space-x-2">
            <a href="<?= site_url(); ?>" class="nav-item-pedesaan">Beranda</a>
            <a href="<?= site_url('profil-desa'); ?>" class="nav-item-pedesaan">Profil Desa</a>
            <a href="<?= site_url('artikel'); ?>" class="nav-item-pedesaan">Kabar Desa</a>
            <a href="<?= site_url('peta'); ?>" class="nav-item-pedesaan">Peta Wilayah</a>
        </div>
        <div>
            <a href="<?= site_url('layanan-mandiri'); ?>" class="btn-mandiri-klasik">Pelayanan Warga Online</a>
        </div>
    </div>
</nav>
""",
        "commons/footer.blade.php": """<footer class="bg-yellow-950 text-yellow-100 py-10 mt-12 border-t-4 border-yellow-600">
    <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8 text-sm">
        <div>
            <h3 class="font-bold text-yellow-400 text-base mb-2">Kantor Pemerintah Desa <?= $desa['nama_desa']; ?></h3>
            <p><?= $desa['alamat_kantor']; ?></p>
            <p>Kode Pos: <?= $desa['kode_pos']; ?></p>
            <p class="mt-2 text-xs text-yellow-300">Gotong royong membangun lumbung desa mandiri.</p>
        </div>
        <div>
            <h3 class="font-bold text-yellow-400 text-base mb-2">Kontak Kerukunan Warga</h3>
            <p>Telepon Kantor: <?= $desa['telepon']; ?></p>
            <p>Surel Resmi: <?= $desa['email_desa']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-yellow-400 text-base mb-2">Sistem Informasi Desa</h3>
            <p>Tema Pedesaan Klasik &bullet; Ditenagai OpenSID</p>
        </div>
    </div>
</footer>
""",
        "layouts/right-sidebar.blade.php": """@extends('theme::template')

@section('layout')
    <div class="flex flex-col lg:flex-row gap-6">
        <main class="lg:w-2/3 w-full space-y-6">
            @yield('content')
        </main>
        <aside class="lg:w-1/3 w-full space-y-6">
            @include('theme::partials.sidebar')
        </aside>
    </div>
@endsection
""",
        "partials/sidebar.blade.php": """<div class="space-y-6">
    <div class="card-klasik p-5">
        @include('theme::widgets.aparatur_desa', ['judul_widget' => 'Pamong & Kepala Desa'])
    </div>
    <div class="card-klasik p-5">
        @include('theme::widgets.keuangan', ['judul_widget' => 'Laporan APBDes Terbuka'])
    </div>
    <div class="card-klasik p-5">
        @include('theme::widgets.peta_wilayah_desa', ['judul_widget' => 'Batas Wilayah Agraris'])
    </div>
</div>
""",
        "widgets/aparatur_desa.blade.php": """<h3 class="card-title-klasik font-bold text-base"><?= $judul_widget ?? 'Pamong Desa'; ?></h3>
<div class="text-center">
    <img src="<?= gambar_pamong($desa['foto_kepala_desa']); ?>" alt="Kepala Desa" class="w-28 h-28 object-cover rounded-full mx-auto mb-3 shadow border-4 border-yellow-700">
    <h4 class="font-bold text-yellow-900"><?= $desa['nama_kepala_desa']; ?></h4>
    <p class="text-xs text-green-800 font-semibold">Kepala Desa <?= $desa['nama_desa']; ?></p>
    <p class="text-xs text-gray-500 mt-1 italic">"Melayani warga dengan tulus dan bijaksana."</p>
</div>
""",
        "widgets/keuangan.blade.php": """<h3 class="card-title-klasik font-bold text-base flex justify-between items-center">
    <span><?= $judul_widget ?? 'APBDes Desa'; ?></span>
    <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-0.5 rounded font-mono"><?= date('Y'); ?></span>
</h3>
<div class="space-y-3 text-xs">
    <div>
        <div class="flex justify-between font-semibold mb-1">
            <span class="text-gray-700">Pendapatan Asli & Dana Desa</span>
            <span class="text-green-700">Rp <?= number_format($transparansi['pendapatan'] ?? 1250000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-200 h-2.5 rounded-full overflow-hidden">
            <div class="bg-green-600 h-full rounded-full" style="width: 82%"></div>
        </div>
    </div>
    <div>
        <div class="flex justify-between font-semibold mb-1">
            <span class="text-gray-700">Belanja Pembangunan & Warga</span>
            <span class="text-amber-700">Rp <?= number_format($transparansi['belanja'] ?? 1180000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-200 h-2.5 rounded-full overflow-hidden">
            <div class="bg-amber-600 h-full rounded-full" style="width: 76%"></div>
        </div>
    </div>
</div>
""",
        "widgets/peta_wilayah_desa.blade.php": """<h3 class="card-title-klasik font-bold text-base"><?= $judul_widget ?? 'Peta Wilayah'; ?></h3>
<div id="peta-desa-klasik" style="height: 220px;" class="rounded border border-yellow-800 overflow-hidden"></div>
"""
    }

    create_theme_files(slug, title, author, description, config_items, css, js, views)

# ==============================================================================
# TEMA 2: DESA MODERN
# ==============================================================================
def build_tema_modern():
    slug = "tema-desa-modern"
    title = "Tema Desa Modern"
    author = "Diskominfo - Tata Kelola Desa"
    description = "Tema pemerintahan desa modern yang bersih, sleek, transparan, dan profesional"

    config_items = [
        {
            "judul": "Warna Primer Brand",
            "key": "warna_primer",
            "value": "#1e40af",
            "type": "color-picker",
            "keterangan": "Warna biru profesional instansi pemerintah",
            "group": "Umum"
        },
        {
            "judul": "Layout Sidebar",
            "key": "posisi_sidebar",
            "value": "kanan",
            "type": "select",
            "options": {"kanan": "Sidebar Kanan", "kiri": "Sidebar Kiri"},
            "group": "Tampilan"
        },
        {
            "judul": "Jumlah Berita Per Halaman",
            "key": "jumlah_berita_perhalaman",
            "value": 8,
            "type": "input-number",
            "attributes": {"min": 4, "max": 24, "step": 4},
            "group": "Berita"
        }
    ]

    css = """/* ==============================================================
   Tema Desa Modern - OpenSID
   Palet: Royal Blue, Slate Dark, Crisp White, Soft Drop Shadow
============================================================== */
:root {
    --primary: #1e40af;
    --primary-hover: #1d4ed8;
    --secondary: #0284c7;
    --bg-main: #f8fafc;
    --surface: #ffffff;
    --text-primary: #0f172a;
    --text-secondary: #475569;
    --border: #e2e8f0;
}

body {
    background-color: var(--bg-main);
    color: var(--text-primary);
    font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    margin: 0;
    line-height: 1.6;
}

.modern-topbar {
    background: #0f172a;
    color: #94a3b8;
    font-size: 0.8rem;
    padding: 6px 0;
}

.modern-navbar {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(8px);
    border-bottom: 1px solid var(--border);
}

.modern-nav-link {
    color: var(--text-secondary);
    font-weight: 500;
    font-size: 0.9rem;
    padding: 6px 12px;
    border-radius: 8px;
    transition: all 0.2s;
    text-decoration: none;
}
.modern-nav-link:hover {
    color: var(--primary);
    background-color: #eff6ff;
}

.btn-mandiri-modern {
    background-color: var(--primary);
    color: #ffffff !important;
    padding: 8px 16px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.875rem;
    box-shadow: 0 4px 6px -1px rgba(30, 64, 175, 0.2);
    transition: all 0.2s;
    text-decoration: none;
}
.btn-mandiri-modern:hover {
    background-color: var(--primary-hover);
    box-shadow: 0 6px 10px -1px rgba(30, 64, 175, 0.3);
}

.card-modern {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
    transition: transform 0.2s, box-shadow 0.2s;
}
.card-modern:hover {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
}
"""

    js = """document.addEventListener('DOMContentLoaded', function() {
    console.log('[Tema Desa Modern] Aktif.');
    var petaElem = document.getElementById('peta-desa-modern');
    if (petaElem && typeof L !== 'undefined') {
        var map = L.map('peta-desa-modern').setView([-1.2, 124.8], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);
    }
});
"""

    views = {
        "template.blade.php": """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    @include('theme::commons.meta')
    @include('theme::commons.source_css')
    <title>@yield('title', $heading ?? $desa['nama_desa']) - Portal Resmi Desa</title>
    @stack('styles')
</head>
<body>
    @include('theme::commons.header')

    <div class="container mx-auto px-4 my-8">
        @yield('layout')
    </div>

    @include('theme::commons.footer')
    <script src="{{ theme_asset('js/script.js') }}"></script>
    @stack('scripts')
</body>
</html>
""",
        "commons/meta.blade.php": """<meta name="description" content="Portal Resmi Pemerintahan Desa <?= $desa['nama_desa']; ?>. Transparan, Akuntabel, dan Melayani.">
<link rel="shortcut icon" href="<?= gambar_desa($desa['logo']); ?>">
""",
        "commons/source_css.blade.php": """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
<link rel="stylesheet" href="{{ theme_asset('css/style.css') }}">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>
""",
        "commons/header.blade.php": """<div class="modern-topbar">
    <div class="container mx-auto px-4 flex justify-between items-center">
        <span>🏛️ Portal Resmi Pemerintahan Desa <?= $desa['nama_desa']; ?></span>
        <span class="flex items-center space-x-4">
            <span>Email: <?= $desa['email_desa']; ?></span>
            <span>Telp: <?= $desa['telepon']; ?></span>
        </span>
    </div>
</div>

<header class="modern-navbar sticky top-0 z-40">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <div class="flex items-center space-x-3">
            <img src="<?= gambar_desa($desa['logo']); ?>" alt="Logo Desa" class="h-11 w-auto">
            <div>
                <h1 class="text-lg font-bold text-slate-900 tracking-tight leading-tight"><?= $desa['nama_desa']; ?></h1>
                <p class="text-xs text-slate-500">Kec. <?= $desa['nama_kecamatan']; ?>, Kab. <?= $desa['nama_kabupaten']; ?></p>
            </div>
        </div>
        <nav class="hidden md:flex items-center space-x-4">
            <a href="<?= site_url(); ?>" class="modern-nav-link">Beranda</a>
            <a href="<?= site_url('profil-desa'); ?>" class="modern-nav-link">Profil</a>
            <a href="<?= site_url('artikel'); ?>" class="modern-nav-link">Berita & Pengumuman</a>
            <a href="<?= site_url('peta'); ?>" class="modern-nav-link">Peta WebGIS</a>
            <a href="<?= site_url('layanan-mandiri'); ?>" class="btn-mandiri-modern">Portal Warga</a>
        </nav>
    </div>
</header>
""",
        "commons/footer.blade.php": """<footer class="bg-slate-900 text-slate-300 py-12 mt-16 border-t border-slate-800 text-sm">
    <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
            <h3 class="font-bold text-white text-base mb-3">Pemerintah Desa <?= $desa['nama_desa']; ?></h3>
            <p class="text-slate-400"><?= $desa['alamat_kantor']; ?></p>
            <p class="text-slate-400">Kode Pos <?= $desa['kode_pos']; ?></p>
            <p class="mt-4 text-xs text-slate-500">Pelayanan publik berbasis tata kelola pemerintahan yang bersih dan akuntabel.</p>
        </div>
        <div>
            <h3 class="font-bold text-white text-base mb-3">Saluran Informasi</h3>
            <p class="text-slate-400">Surat Elektronik: <?= $desa['email_desa']; ?></p>
            <p class="text-slate-400">Telepon Layanan: <?= $desa['telepon']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white text-base mb-3">Infrastruktur Digital</h3>
            <p class="text-slate-400">Ditenagai oleh Ekosistem OpenSID.</p>
            <p class="text-xs text-slate-500 mt-2">&copy; <?= date('Y'); ?> Pemerintah Desa <?= $desa['nama_desa']; ?>. Hak cipta dilindungi.</p>
        </div>
    </div>
</footer>
""",
        "layouts/right-sidebar.blade.php": """@extends('theme::template')

@section('layout')
    <div class="flex flex-col lg:flex-row gap-8">
        <main class="lg:w-2/3 w-full space-y-6">
            @yield('content')
        </main>
        <aside class="lg:w-1/3 w-full space-y-6">
            @include('theme::partials.sidebar')
        </aside>
    </div>
@endsection
""",
        "partials/sidebar.blade.php": """<div class="space-y-6">
    <div class="card-modern p-6">
        @include('theme::widgets.aparatur_desa', ['judul_widget' => 'Pimpinan Desa'])
    </div>
    <div class="card-modern p-6">
        @include('theme::widgets.keuangan', ['judul_widget' => 'Transparansi APBDes'])
    </div>
    <div class="card-modern p-6">
        @include('theme::widgets.peta_wilayah_desa', ['judul_widget' => 'Peta Spasial Desa'])
    </div>
</div>
""",
        "widgets/aparatur_desa.blade.php": """<h3 class="text-base font-bold text-slate-900 mb-4 border-b pb-2"><?= $judul_widget ?? 'Aparatur Desa'; ?></h3>
<div class="flex items-center space-x-4">
    <img src="<?= gambar_pamong($desa['foto_kepala_desa']); ?>" alt="Kepala Desa" class="w-16 h-16 rounded-full object-cover border-2 border-blue-600 shadow">
    <div>
        <h4 class="font-bold text-slate-900 text-sm"><?= $desa['nama_kepala_desa']; ?></h4>
        <span class="text-xs bg-blue-50 text-blue-700 px-2 py-0.5 rounded font-medium">Kepala Desa</span>
        <p class="text-xs text-slate-400 mt-1">Periode Aktif</p>
    </div>
</div>
""",
        "widgets/keuangan.blade.php": """<h3 class="text-base font-bold text-slate-900 mb-4 flex justify-between items-center border-b pb-2">
    <span><?= $judul_widget ?? 'Transparansi Anggaran'; ?></span>
    <span class="text-xs bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-semibold">T.A. <?= date('Y'); ?></span>
</h3>
<div class="space-y-4 text-xs">
    <div>
        <div class="flex justify-between mb-1.5 font-medium">
            <span class="text-slate-600">Realisasi Pendapatan</span>
            <span class="font-bold text-emerald-600">Rp <?= number_format($transparansi['pendapatan'] ?? 1250000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
            <div class="bg-emerald-500 h-full rounded-full" style="width: 86%"></div>
        </div>
    </div>
    <div>
        <div class="flex justify-between mb-1.5 font-medium">
            <span class="text-slate-600">Realisasi Belanja</span>
            <span class="font-bold text-blue-600">Rp <?= number_format($transparansi['belanja'] ?? 1180000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
            <div class="bg-blue-600 h-full rounded-full" style="width: 79%"></div>
        </div>
    </div>
</div>
""",
        "widgets/peta_wilayah_desa.blade.php": """<h3 class="text-base font-bold text-slate-900 mb-3 border-b pb-2"><?= $judul_widget ?? 'Peta Wilayah'; ?></h3>
<div id="peta-desa-modern" style="height: 220px;" class="rounded-lg border border-slate-200 overflow-hidden"></div>
"""
    }

    create_theme_files(slug, title, author, description, config_items, css, js, views)

# ==============================================================================
# TEMA 3: DESA DIGITAL (SMART VILLAGE)
# ==============================================================================
def build_tema_digital():
    slug = "tema-desa-digital"
    title = "Tema Desa Digital"
    author = "Diskominfo - Smart Village Center"
    description = "Tema Smart Village futuristik dengan live stats counter, glassmorphism, dan integrasi layanan online"

    config_items = [
        {
            "judul": "Warna Aksen Neon",
            "key": "warna_neon",
            "value": "#06b6d4",
            "type": "color-picker",
            "keterangan": "Warna aksen digital cyan/electric blue",
            "group": "Desain"
        },
        {
            "judul": "Tampilkan Live Counter Statistik",
            "key": "show_live_counter",
            "value": "1",
            "type": "select",
            "options": {"1": "Ya", "0": "Tidak"},
            "group": "Fitur Cerdas"
        },
        {
            "judul": "Jumlah Berita Per Halaman",
            "key": "jumlah_berita_perhalaman",
            "value": 6,
            "type": "input-number",
            "attributes": {"min": 3, "max": 18, "step": 3},
            "group": "Data"
        }
    ]

    css = """/* ==============================================================
   Tema Desa Digital (Smart Village) - OpenSID
   Palet: Cyber Dark, Cyan Neon, Purple Glow, Glassmorphism
============================================================== */
:root {
    --cyber-dark: #090d16;
    --cyber-card: rgba(15, 23, 42, 0.75);
    --cyan-glow: #06b6d4;
    --cyan-glow-hover: #0891b2;
    --purple-accent: #8b5cf6;
    --text-white: #f8fafc;
    --text-dim: #94a3b8;
    --border-glass: rgba(255, 255, 255, 0.1);
}

body {
    background-color: var(--cyber-dark);
    color: var(--text-white);
    font-family: 'Inter', system-ui, sans-serif;
    margin: 0;
    line-height: 1.6;
    background-image: radial-gradient(circle at 15% 15%, rgba(6, 182, 212, 0.08) 0%, transparent 40%),
                      radial-gradient(circle at 85% 85%, rgba(139, 92, 246, 0.08) 0%, transparent 40%);
    background-attachment: fixed;
}

.digital-header {
    background: rgba(9, 13, 22, 0.85);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border-glass);
}

.glass-box {
    background: var(--cyber-card);
    backdrop-filter: blur(12px);
    border: 1px solid var(--border-glass);
    border-radius: 16px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}

.badge-glow {
    background: rgba(6, 182, 212, 0.15);
    border: 1px solid var(--cyan-glow);
    color: var(--cyan-glow);
    box-shadow: 0 0 12px rgba(6, 182, 212, 0.3);
}

.btn-mandiri-digital {
    background: linear-gradient(135deg, #06b6d4, #3b82f6);
    color: #ffffff !important;
    padding: 8px 18px;
    border-radius: 10px;
    font-weight: 600;
    font-size: 0.875rem;
    box-shadow: 0 0 16px rgba(6, 182, 212, 0.4);
    transition: all 0.3s;
    text-decoration: none;
}
.btn-mandiri-digital:hover {
    box-shadow: 0 0 24px rgba(6, 182, 212, 0.7);
    transform: translateY(-1px);
}

.stat-counter-box {
    background: linear-gradient(180deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.9) 100%);
    border: 1px solid var(--border-glass);
    border-radius: 14px;
    padding: 16px;
    text-align: center;
}
"""

    js = """document.addEventListener('DOMContentLoaded', function() {
    console.log('[Tema Desa Digital] Smart Village System Loaded.');
    var petaElem = document.getElementById('peta-desa-digital');
    if (petaElem && typeof L !== 'undefined') {
        var map = L.map('peta-desa-digital').setView([-1.2, 124.8], 13);
        L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; CartoDB & OpenStreetMap'
        }).addTo(map);
    }
});
"""

    views = {
        "template.blade.php": """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    @include('theme::commons.meta')
    @include('theme::commons.source_css')
    <title>@yield('title', $heading ?? $desa['nama_desa']) - Smart Village</title>
    @stack('styles')
</head>
<body>
    @include('theme::commons.header')

    <div class="container mx-auto px-4 my-8">
        @yield('layout')
    </div>

    @include('theme::commons.footer')
    <script src="{{ theme_asset('js/script.js') }}"></script>
    @stack('scripts')
</body>
</html>
""",
        "commons/meta.blade.php": """<meta name="description" content="Portal Smart Village Desa <?= $desa['nama_desa']; ?>. Pelayanan Digital Cepat, Akurat, dan Transparan.">
<link rel="shortcut icon" href="<?= gambar_desa($desa['logo']); ?>">
""",
        "commons/source_css.blade.php": """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
<link rel="stylesheet" href="{{ theme_asset('css/style.css') }}">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>
""",
        "commons/header.blade.php": """<header class="digital-header sticky top-0 z-50">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <div class="flex items-center space-x-3">
            <img src="<?= gambar_desa($desa['logo']); ?>" alt="Logo Desa" class="h-10 w-auto filter drop-shadow">
            <div>
                <div class="flex items-center space-x-2">
                    <h1 class="text-lg font-bold text-white tracking-wide"><?= $desa['nama_desa']; ?></h1>
                    <span class="badge-glow text-xs px-2 py-0.5 rounded-full font-mono uppercase">Smart Village</span>
                </div>
                <p class="text-xs text-gray-400">Kec. <?= $desa['nama_kecamatan']; ?>, Kab. <?= $desa['nama_kabupaten']; ?></p>
            </div>
        </div>
        <nav class="hidden md:flex items-center space-x-6 text-sm font-medium">
            <a href="<?= site_url(); ?>" class="text-gray-300 hover:text-cyan-400 transition">Dashboard</a>
            <a href="<?= site_url('profil-desa'); ?>" class="text-gray-300 hover:text-cyan-400 transition">Profil</a>
            <a href="<?= site_url('artikel'); ?>" class="text-gray-300 hover:text-cyan-400 transition">Warta Digital</a>
            <a href="<?= site_url('peta'); ?>" class="text-gray-300 hover:text-cyan-400 transition">Geo-Portal</a>
            <a href="<?= site_url('layanan-mandiri'); ?>" class="btn-mandiri-digital">Layanan Mandiri Online</a>
        </nav>
    </div>
</header>

<!-- Live Stats Bar (Smart Village Indicator) -->
<div class="container mx-auto px-4 mt-6">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="stat-counter-box">
            <span class="text-xs text-gray-400 block mb-1">Total Penduduk</span>
            <span class="text-xl font-bold text-cyan-400"><?= number_format($total_penduduk ?? 3420); ?></span>
        </div>
        <div class="stat-counter-box">
            <span class="text-xs text-gray-400 block mb-1">Kepala Keluarga</span>
            <span class="text-xl font-bold text-purple-400"><?= number_format($total_kk ?? 980); ?></span>
        </div>
        <div class="stat-counter-box">
            <span class="text-xs text-gray-400 block mb-1">Surat Online Terbit</span>
            <span class="text-xl font-bold text-emerald-400"><?= number_format($total_surat ?? 1250); ?></span>
        </div>
        <div class="stat-counter-box">
            <span class="text-xs text-gray-400 block mb-1">Status Indeks Desa</span>
            <span class="text-xl font-bold text-amber-400">Desa Mandiri</span>
        </div>
    </div>
</div>
""",
        "commons/footer.blade.php": """<footer class="bg-gray-950 text-gray-400 py-12 mt-16 border-t border-gray-800 text-sm">
    <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
            <h3 class="font-bold text-white text-base mb-3 flex items-center space-x-2">
                <span>Pusat Layanan Digital</span>
                <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
            </h3>
            <p><?= $desa['alamat_kantor']; ?></p>
            <p>Kode Pos <?= $desa['kode_pos']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white text-base mb-3">Integrasi SPBE & OpenSID</h3>
            <p>Pemerintahan Cerdas berbasis satu data desa terpadu.</p>
            <p class="mt-2 text-cyan-400 text-xs">Email: <?= $desa['email_desa']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white text-base mb-3">Keamanan & Keandalan</h3>
            <p>Didukung Enkripsi SSL & Validasi TTE.</p>
            <p class="text-xs text-gray-600 mt-2">&copy; <?= date('Y'); ?> Smart Village <?= $desa['nama_desa']; ?>.</p>
        </div>
    </div>
</footer>
""",
        "layouts/right-sidebar.blade.php": """@extends('theme::template')

@section('layout')
    <div class="flex flex-col lg:flex-row gap-8">
        <main class="lg:w-2/3 w-full space-y-6">
            @yield('content')
        </main>
        <aside class="lg:w-1/3 w-full space-y-6">
            @include('theme::partials.sidebar')
        </aside>
    </div>
@endsection
""",
        "partials/sidebar.blade.php": """<div class="space-y-6">
    <div class="glass-box p-6">
        @include('theme::widgets.aparatur_desa', ['judul_widget' => 'Pimpinan Pemerintahan'])
    </div>
    <div class="glass-box p-6">
        @include('theme::widgets.keuangan', ['judul_widget' => 'Transparansi Real-Time APBDes'])
    </div>
    <div class="glass-box p-6">
        @include('theme::widgets.peta_wilayah_desa', ['judul_widget' => 'Sistem Informasi Geospasial'])
    </div>
</div>
""",
        "widgets/aparatur_desa.blade.php": """<h3 class="text-base font-bold text-white mb-4 border-b border-gray-800 pb-2 flex items-center justify-between">
    <span><?= $judul_widget ?? 'Aparatur'; ?></span>
    <span class="text-xs text-cyan-400 font-mono">Digital Signature Ready</span>
</h3>
<div class="text-center">
    <div class="relative w-24 h-24 mx-auto mb-3">
        <img src="<?= gambar_pamong($desa['foto_kepala_desa']); ?>" alt="Kepala Desa" class="w-full h-full object-cover rounded-full border-2 border-cyan-400 shadow">
        <span class="absolute bottom-0 right-0 w-4 h-4 bg-emerald-500 border-2 border-gray-900 rounded-full" title="Online"></span>
    </div>
    <h4 class="font-bold text-white text-sm"><?= $desa['nama_kepala_desa']; ?></h4>
    <p class="text-xs text-cyan-400">Kepala Desa <?= $desa['nama_desa']; ?></p>
</div>
""",
        "widgets/keuangan.blade.php": """<h3 class="text-base font-bold text-white mb-4 flex justify-between items-center border-b border-gray-800 pb-2">
    <span><?= $judul_widget ?? 'APBDes Data'; ?></span>
    <span class="text-xs bg-cyan-950 text-cyan-400 border border-cyan-800 px-2 py-0.5 rounded font-mono"><?= date('Y'); ?></span>
</h3>
<div class="space-y-4 text-xs">
    <div>
        <div class="flex justify-between mb-1">
            <span class="text-gray-400">Target Pendapatan</span>
            <span class="font-bold text-cyan-400">Rp <?= number_format($transparansi['pendapatan'] ?? 1250000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-800 h-2 rounded-full overflow-hidden">
            <div class="bg-gradient-to-r from-cyan-500 to-blue-500 h-full rounded-full" style="width: 88%"></div>
        </div>
    </div>
    <div>
        <div class="flex justify-between mb-1">
            <span class="text-gray-400">Realisasi Belanja</span>
            <span class="font-bold text-purple-400">Rp <?= number_format($transparansi['belanja'] ?? 1180000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-800 h-2 rounded-full overflow-hidden">
            <div class="bg-gradient-to-r from-purple-500 to-pink-500 h-full rounded-full" style="width: 80%"></div>
        </div>
    </div>
</div>
""",
        "widgets/peta_wilayah_desa.blade.php": """<h3 class="text-base font-bold text-white mb-3 border-b border-gray-800 pb-2"><?= $judul_widget ?? 'WebGIS'; ?></h3>
<div id="peta-desa-digital" style="height: 220px;" class="rounded-xl border border-gray-800 overflow-hidden"></div>
"""
    }

    create_theme_files(slug, title, author, description, config_items, css, js, views)

def main():
    print("=============================================================")
    print("  MEMBANGUN 3 TEMA RESMI OPENSSL (BLADE ARCHITECTURE)       ")
    print("=============================================================\n")
    build_tema_pedesaan()
    build_tema_modern()
    build_tema_digital()
    print("Semua 3 tema berhasil dibangun dan dikemas ke themes_output/!")

if __name__ == "__main__":
    main()
