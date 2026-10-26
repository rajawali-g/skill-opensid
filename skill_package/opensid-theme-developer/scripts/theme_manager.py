#!/usr/bin/env python3
"""
theme_manager.py
Pengelola tema OpenSID berstandar arsitektur resmi (Laravel Blade):
- New: Menghasilkan struktur tema lengkap sesuai standar tema resmi (Esensi & Natra):
       config.json, composer.json, assets/, resources/views/ (template, commons, layouts, partials, widgets)
- Package: Mengompresi tema ke themes_output/<nama_tema>.zip siap unggah ke admin OpenSID
- Deploy: Menyalin tema ke folder target instalasi OpenSID (desa/themes/<nama_tema>/)
- List: Menampilkan daftar tema di themes_output/
"""

import os
import sys
import json
import shutil
import zipfile
import argparse
from datetime import datetime

def get_workspace_root():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    curr = script_dir
    for _ in range(4):
        curr = os.path.dirname(curr)
    return curr

def cmd_list(output_dir):
    print("=============================================")
    print("  Daftar Tema di themes_output/              ")
    print("=============================================")
    if not os.path.exists(output_dir):
        print("Folder themes_output/ belum ada.")
        return

    items = [d for d in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, d))]
    if not items:
        print("Belum ada tema di folder themes_output/.")
        return

    for name in sorted(items):
        zip_file = os.path.join(output_dir, f"{name}.zip")
        if os.path.exists(zip_file):
            size_kb = round(os.path.getsize(zip_file) / 1024, 1)
            status = f"[ZIP Tersedia: {size_kb} KB]"
        else:
            status = "[Belum di-package]"
        print(f"[*] {name} {status}")

def cmd_new(output_dir, theme_name, title, author):
    slug = "".join([c if c.isalnum() or c in "_-" else "-" for c in theme_name.lower()]).strip("-")
    theme_folder = os.path.join(output_dir, slug)
    print(f"[*] Membuat kerangka tema berstandar resmi: {slug}")
    print(f"    Path: {theme_folder}")

    # Sub-direktori sesuai arsitektur resmi OpenSID
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

    # 1. config.json (Manifes opsi tema Web Admin OpenSID)
    config_json = [
        {
            "judul": "Warna Dasar Tema",
            "key": "warna_dasar",
            "value": "#2563eb",
            "type": "color-picker",
            "keterangan": "Warna dasar utama tema website desa",
            "options": None,
            "readonly": False,
            "group": "Umum"
        },
        {
            "judul": "Tampilkan Peta Wilayah",
            "key": "tampilkan_peta",
            "value": "1",
            "type": "select",
            "keterangan": "Tampilkan widget peta desa di beranda",
            "options": {"1": "Ya", "0": "Tidak"},
            "readonly": False,
            "group": "Umum"
        },
        {
            "judul": "Jumlah Berita Per Halaman",
            "key": "jumlah_berita_perhalaman",
            "value": 6,
            "type": "input-number",
            "keterangan": "Jumlah berita yang ditampilkan per halaman",
            "attributes": {"min": 3, "max": 24, "step": 3},
            "readonly": False,
            "link": True,
            "group": "Berita"
        }
    ]
    with open(os.path.join(theme_folder, "config.json"), "w", encoding="utf-8") as f:
        json.dump(config_json, f, indent=4, ensure_ascii=False)

    # 2. composer.json
    composer_json = {
        "name": f"themes/{slug}",
        "type": "library",
        "description": f"{title} untuk OpenSID",
        "license": "GPL-3.0-or-later",
        "keywords": ["Themes", "OpenSID"],
        "authors": [
            {
                "name": author,
                "email": "desa@minselkab.go.id"
            }
        ]
    }
    with open(os.path.join(theme_folder, "composer.json"), "w", encoding="utf-8") as f:
        json.dump(composer_json, f, indent=4, ensure_ascii=False)

    # 3. catatan_rilis.md
    with open(os.path.join(theme_folder, "catatan_rilis.md"), "w", encoding="utf-8") as f:
        f.write(f"Catatan Rilis v1.0.0 ({slug}) :\n\n### TEKNIS :\n1. Inisialisasi arsitektur resmi Laravel Blade OpenSID.\n2. Integrasi tema dengan namespace theme:: dan widget dinamis.\n")

    # 4. index.html (Silence is Golden)
    silence = "<!DOCTYPE html><html><head><title>403 Forbidden</title></head><body><p>Directory access is forbidden.</p></body></html>"
    with open(os.path.join(theme_folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(silence)
    with open(os.path.join(theme_folder, "assets", "index.html"), "w", encoding="utf-8") as f:
        f.write(silence)

    # 5. resources/views/template.blade.php (Master Blade Layout)
    template_blade = """@php
    $themeVersion = 'v1.0.0';
@endphp
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    @include('theme::commons.meta')
    @include('theme::commons.source_css')
    <title>@yield('title', $heading ?? $desa['nama_desa'])</title>
    @stack('styles')
</head>
<body class="bg-gray-50 text-gray-800 font-sans">
    @include('theme::commons.header')

    {{-- Konten layout (full-content atau right-sidebar) --}}
    @yield('layout')

    @include('theme::commons.footer')

    <script src="{{ theme_asset('js/script.js') }}"></script>
    @stack('scripts')
</body>
</html>
"""
    with open(os.path.join(theme_folder, "resources", "views", "template.blade.php"), "w", encoding="utf-8") as f:
        f.write(template_blade)

    # 6. resources/views/commons/meta.blade.php
    meta_blade = """<meta name="description" content="Website Resmi Pemerintah Desa <?= $desa['nama_desa']; ?>, Kec. <?= $desa['nama_kecamatan']; ?>, Kab. <?= $desa['nama_kabupaten']; ?>">
<link rel="shortcut icon" href="<?= gambar_desa($desa['logo']); ?>">
"""
    with open(os.path.join(theme_folder, "resources", "views", "commons", "meta.blade.php"), "w", encoding="utf-8") as f:
        f.write(meta_blade)

    # 7. resources/views/commons/source_css.blade.php
    source_css_blade = """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css">
<link rel="stylesheet" href="{{ theme_asset('css/style.css') }}">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>
"""
    with open(os.path.join(theme_folder, "resources", "views", "commons", "source_css.blade.php"), "w", encoding="utf-8") as f:
        f.write(source_css_blade)

    # 8. resources/views/commons/header.blade.php
    header_blade = """<header class="bg-white border-b border-gray-200 sticky top-0 z-50 shadow-sm">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <div class="flex items-center space-x-3">
            <img src="<?= gambar_desa($desa['logo']); ?>" alt="Logo Desa" class="h-12 w-auto">
            <div>
                <h1 class="text-lg font-bold text-gray-900"><?= $desa['nama_desa']; ?></h1>
                <p class="text-xs text-gray-500">Kec. <?= $desa['nama_kecamatan']; ?>, Kab. <?= $desa['nama_kabupaten']; ?></p>
            </div>
        </div>
        <nav class="hidden md:flex space-x-6 text-sm font-medium items-center">
            <a href="<?= site_url(); ?>" class="text-gray-700 hover:text-blue-600">Beranda</a>
            <a href="<?= site_url('profil-desa'); ?>" class="text-gray-700 hover:text-blue-600">Profil</a>
            <a href="<?= site_url('artikel'); ?>" class="text-gray-700 hover:text-blue-600">Kabar Desa</a>
            <a href="<?= site_url('layanan-mandiri'); ?>" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">Layanan Mandiri</a>
        </nav>
    </div>
</header>
"""
    with open(os.path.join(theme_folder, "resources", "views", "commons", "header.blade.php"), "w", encoding="utf-8") as f:
        f.write(header_blade)

    # 9. resources/views/commons/footer.blade.php
    footer_blade = """<footer class="bg-gray-900 text-gray-300 py-10 mt-12 text-sm">
    <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
            <h3 class="font-bold text-white mb-3">Pemerintah Desa <?= $desa['nama_desa']; ?></h3>
            <p><?= $desa['alamat_kantor']; ?></p>
            <p>Kode Pos: <?= $desa['kode_pos']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white mb-3">Kontak Pelayanan</h3>
            <p>Email: <?= $desa['email_desa']; ?></p>
            <p>Telepon: <?= $desa['telepon']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white mb-3">Sistem Informasi Desa</h3>
            <p>Ditenagai oleh OpenSID. Dikelola oleh Tim Publikasi Desa.</p>
        </div>
    </div>
</footer>
"""
    with open(os.path.join(theme_folder, "resources", "views", "commons", "footer.blade.php"), "w", encoding="utf-8") as f:
        f.write(footer_blade)

    # 10. resources/views/layouts/right-sidebar.blade.php
    right_sidebar_blade = """@extends('theme::template')

@section('layout')
    <div class="container mx-auto px-4 my-6 flex flex-col lg:flex-row gap-6">
        <main class="lg:w-2/3 w-full bg-white rounded-xl p-6 shadow-sm border border-gray-100">
            @yield('content')
        </main>
        <aside class="lg:w-1/3 w-full space-y-6">
            @include('theme::partials.sidebar')
        </aside>
    </div>
@endsection
"""
    with open(os.path.join(theme_folder, "resources", "views", "layouts", "right-sidebar.blade.php"), "w", encoding="utf-8") as f:
        f.write(right_sidebar_blade)

    # 11. resources/views/partials/sidebar.blade.php (Dynamic Widget Includer)
    sidebar_blade = """<div class="space-y-6">
    @if ($widgetAktif ?? false)
        @foreach ($widgetAktif as $widget)
            @php
                $judul_widget = [
                    'judul_widget' => str_replace('Desa', ucwords(setting('sebutan_desa')), strip_tags($widget['judul'])),
                ];
            @endphp
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-5 overflow-hidden">
                @includeIf("theme::widgets.{$widget['isi']}", $judul_widget)
            </div>
        @endforeach
    @else
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
            @include('theme::widgets.aparatur_desa', ['judul_widget' => 'Aparatur Desa'])
        </div>
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
            @include('theme::widgets.keuangan', ['judul_widget' => 'Transparansi APBDes'])
        </div>
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
            @include('theme::widgets.peta_wilayah_desa', ['judul_widget' => 'Peta Wilayah Desa'])
        </div>
    @endif
</div>
"""
    with open(os.path.join(theme_folder, "resources", "views", "partials", "sidebar.blade.php"), "w", encoding="utf-8") as f:
        f.write(sidebar_blade)

    # 12. resources/views/widgets/aparatur_desa.blade.php
    aparatur_widget = """<h3 class="text-base font-bold text-gray-900 mb-4 border-b pb-2"><?= $judul_widget ?? 'Aparatur Desa'; ?></h3>
<div class="text-center">
    <img src="<?= gambar_pamong($desa['foto_kepala_desa']); ?>" alt="Kepala Desa" class="w-24 h-24 object-cover rounded-full mx-auto mb-3 shadow border-2 border-blue-500">
    <h4 class="font-bold text-gray-800 text-sm"><?= $desa['nama_kepala_desa']; ?></h4>
    <p class="text-xs text-gray-500">Kepala Desa <?= $desa['nama_desa']; ?></p>
</div>
"""
    with open(os.path.join(theme_folder, "resources", "views", "widgets", "aparatur_desa.blade.php"), "w", encoding="utf-8") as f:
        f.write(aparatur_widget)

    # 13. resources/views/widgets/keuangan.blade.php
    keuangan_widget = """<h3 class="text-base font-bold text-gray-900 mb-4 flex justify-between items-center border-b pb-2">
    <span><?= $judul_widget ?? 'APBDes'; ?></span>
    <span class="text-xs text-blue-600 bg-blue-50 px-2 py-1 rounded">Tahun <?= date('Y'); ?></span>
</h3>
<div class="space-y-3 text-xs">
    <div>
        <div class="flex justify-between mb-1">
            <span class="text-gray-600">Pendapatan</span>
            <span class="font-bold text-green-600">Rp <?= number_format($transparansi['pendapatan'] ?? 1250000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-200 h-2 rounded-full overflow-hidden">
            <div class="bg-green-500 h-2 rounded-full" style="width: 85%"></div>
        </div>
    </div>
    <div>
        <div class="flex justify-between mb-1">
            <span class="text-gray-600">Belanja</span>
            <span class="font-bold text-orange-600">Rp <?= number_format($transparansi['belanja'] ?? 1180000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-200 h-2 rounded-full overflow-hidden">
            <div class="bg-orange-500 h-2 rounded-full" style="width: 78%"></div>
        </div>
    </div>
</div>
"""
    with open(os.path.join(theme_folder, "resources", "views", "widgets", "keuangan.blade.php"), "w", encoding="utf-8") as f:
        f.write(keuangan_widget)

    # 14. resources/views/widgets/peta_wilayah_desa.blade.php
    peta_widget = """<h3 class="text-base font-bold text-gray-900 mb-3 border-b pb-2"><?= $judul_widget ?? 'Peta Wilayah'; ?></h3>
<div id="peta-desa-widget" style="height: 220px;" class="rounded-lg overflow-hidden border border-gray-200"></div>
"""
    with open(os.path.join(theme_folder, "resources", "views", "widgets", "peta_wilayah_desa.blade.php"), "w", encoding="utf-8") as f:
        f.write(peta_widget)

    # 15. assets/css/style.css
    style_css = """/* Stylesheet Tema Resmi OpenSID */
:root {
    --primary: #2563eb;
    --primary-hover: #1d4ed8;
    --text-main: #1f2937;
    --bg-main: #f8fafc;
}

body {
    background-color: var(--bg-main);
    color: var(--text-main);
    line-height: 1.6;
}

.nav-link {
    transition: color 0.2s ease-in-out;
}
"""
    with open(os.path.join(theme_folder, "assets", "css", "style.css"), "w", encoding="utf-8") as f:
        f.write(style_css)

    # 16. assets/js/script.js
    script_js = """document.addEventListener('DOMContentLoaded', function() {
    var petaElem = document.getElementById('peta-desa-widget');
    if (petaElem && typeof L !== 'undefined') {
        var map = L.map('peta-desa-widget').setView([-1.2, 124.8], 12);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);
    }
});
"""
    with open(os.path.join(theme_folder, "assets", "js", "script.js"), "w", encoding="utf-8") as f:
        f.write(script_js)

    print(f"[+] Kerangka tema berstandar resmi '{slug}' berhasil dibuat di: {theme_folder}")

def cmd_package(output_dir, theme_name):
    slug = "".join([c if c.isalnum() or c in "_-" else "-" for c in theme_name.lower()]).strip("-")
    theme_folder = os.path.join(output_dir, slug)
    if not os.path.exists(theme_folder):
        print(f"Error: Folder tema tidak ditemukan: {theme_folder}")
        sys.exit(1)

    zip_path = os.path.join(output_dir, f"{slug}.zip")
    if os.path.exists(zip_path):
        os.remove(zip_path)

    print(f"[*] Mengemas tema '{slug}' ke: {zip_path}...")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(theme_folder):
            for file in files:
                abs_file = os.path.join(root, file)
                rel_path = os.path.relpath(abs_file, theme_folder)
                # Standar OpenSID: nama folder tema di dalam zip
                arcname = os.path.join(slug, rel_path)
                zf.write(abs_file, arcname)

    size_kb = round(os.path.getsize(zip_path) / 1024, 1)
    print(f"[+] Berkas ZIP berhasil dibuat: {zip_path} ({size_kb} KB)")
    print("[*] Siap diunggah ke menu admin OpenSID: Pengaturan Web > Tema > Unggah Tema")

def cmd_deploy(output_dir, theme_name, target_opensid):
    slug = "".join([c if c.isalnum() or c in "_-" else "-" for c in theme_name.lower()]).strip("-")
    source_theme = os.path.join(output_dir, slug)
    if not os.path.exists(source_theme):
        print(f"Error: Folder tema tidak ditemukan: {source_theme}")
        sys.exit(1)

    dest_theme = os.path.join(target_opensid, "desa", "themes", slug)
    print(f"[*] Menyinkronkan tema '{slug}' ke: {dest_theme}...")
    os.makedirs(dest_theme, exist_ok=True)
    shutil.copytree(source_theme, dest_theme, dirs_exist_ok=True)
    print("[+] Tema berhasil disinkronkan ke instalasi OpenSID!")

def main():
    parser = argparse.ArgumentParser(description="OpenSID Theme Manager")
    parser.add_argument("action", choices=["new", "package", "deploy", "list"])
    parser.add_argument("--name", help="Nama tema (slug)")
    parser.add_argument("--title", default="Tema Desa Modern", help="Judul tema")
    parser.add_argument("--author", default="Tim Pengembang Desa", help="Pembuat tema")
    parser.add_argument("--target", help="Folder instalasi OpenSID (untuk deploy)")

    args = parser.parse_args()
    workspace_root = get_workspace_root()
    output_dir = os.path.join(workspace_root, "themes_output")
    os.makedirs(output_dir, exist_ok=True)

    if args.action == "list":
        cmd_list(output_dir)
    elif args.action == "new":
        if not args.name:
            print("Error: Argumen --name diperlukan untuk aksi 'new'.")
            sys.exit(1)
        cmd_new(output_dir, args.name, args.title, args.author)
    elif args.action == "package":
        if not args.name:
            print("Error: Argumen --name diperlukan untuk aksi 'package'.")
            sys.exit(1)
        cmd_package(output_dir, args.name)
    elif args.action == "deploy":
        if not args.name or not args.target:
            print("Error: Argumen --name dan --target diperlukan untuk aksi 'deploy'.")
            sys.exit(1)
        cmd_deploy(output_dir, args.name, args.target)

if __name__ == "__main__":
    main()
