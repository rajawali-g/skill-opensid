#!/usr/bin/env python3
"""
theme_manager.py
Pengelola tema OpenSID:
- New: Menghasilkan struktur tema lengkap di themes_output/<nama_tema>/
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
    # script_dir: .../.agents/skills/opensid/scripts
    # naik 4 level ke project root
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
    print(f"[*] Membuat kerangka tema baru: {slug}")
    print(f"    Path: {theme_folder}")

    # Sub-direktori
    for sub in ["assets/css", "assets/js", "assets/images", "layouts", "partials", "widgets"]:
        os.makedirs(os.path.join(theme_folder, sub), exist_ok=True)

    # 1. theme.json
    theme_json = {
        "name": title,
        "slug": slug,
        "version": "1.0.0",
        "author": author,
        "description": "Tema web desa modern responsif dengan integrasi WebGIS Leaflet dan transparansi APBDes",
        "parent": "natra",
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }
    with open(os.path.join(theme_folder, "theme.json"), "w", encoding="utf-8") as f:
        json.dump(theme_json, f, indent=4, ensure_ascii=False)

    # 2. template.php
    template_php = """<?php defined('BASEPATH') || exit('No direct script access allowed'); ?>
<!DOCTYPE html>
<html lang="id">
<head>
    <?php include(__DIR__ . '/layouts/header.php'); ?>
</head>
<body class="bg-gray-50 text-gray-800">
    <!-- Header / Navigasi Desa -->
    <header class="desa-header shadow-sm">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <img src="<?= gambar_desa($desa['logo']); ?>" alt="Logo Desa" class="h-12 w-auto">
                <div>
                    <h1 class="text-xl font-bold text-gray-900"><?= $desa['nama_desa']; ?></h1>
                    <p class="text-sm text-gray-500">Kec. <?= $desa['nama_kecamatan']; ?>, Kab. <?= $desa['nama_kabupaten']; ?></p>
                </div>
            </div>
            <nav class="hidden md:flex space-x-6 text-sm font-medium items-center">
                <a href="<?= site_url(); ?>" class="nav-link">Beranda</a>
                <a href="<?= site_url('profil-desa'); ?>" class="nav-link">Profil</a>
                <a href="<?= site_url('artikel'); ?>" class="nav-link">Kabar Desa</a>
                <a href="<?= site_url('layanan-mandiri'); ?>" class="btn-mandiri">Layanan Mandiri</a>
            </nav>
        </div>
    </header>

    <!-- Konten Utama -->
    <main class="container mx-auto px-4 py-8 grid grid-cols-1 lg:grid-cols-3 gap-8">
        <section class="lg:col-span-2 space-y-6">
            <?php include(__DIR__ . '/partials/artikel.php'); ?>
            <?php include(__DIR__ . '/partials/apbdes.php'); ?>
            <?php include(__DIR__ . '/partials/peta.php'); ?>
        </section>

        <aside class="space-y-6">
            <?php include(__DIR__ . '/layouts/sidebar.php'); ?>
        </aside>
    </main>

    <!-- Footer -->
    <?php include(__DIR__ . '/layouts/footer.php'); ?>
    <script src="<?= base_url("desa/themes/""" + slug + """/assets/js/theme.js"); ?>"></script>
</body>
</html>
"""
    with open(os.path.join(theme_folder, "template.php"), "w", encoding="utf-8") as f:
        f.write(template_php)

    # 3. layouts/header.php
    header_php = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title><?= $heading ?? $desa['nama_desa']; ?> - Website Resmi Desa</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css">
<link rel="stylesheet" href="<?= base_url("desa/themes/""" + slug + """/assets/css/theme.css"); ?>">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>
"""
    with open(os.path.join(theme_folder, "layouts", "header.php"), "w", encoding="utf-8") as f:
        f.write(header_php)

    # 4. layouts/footer.php
    footer_php = """<footer class="desa-footer bg-gray-900 text-gray-300 py-8 mt-12">
    <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">
        <div>
            <h3 class="font-bold text-white mb-2">Pemerintah Desa <?= $desa['nama_desa']; ?></h3>
            <p><?= $desa['alamat_kantor']; ?></p>
            <p>Kode Pos: <?= $desa['kode_pos']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white mb-2">Kontak Pelayanan</h3>
            <p>Email: <?= $desa['email_desa']; ?></p>
            <p>Telepon: <?= $desa['telepon']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white mb-2">Sistem Informasi Desa</h3>
            <p>Ditenagai oleh OpenSID &bullet; Tema Resmi Desa</p>
        </div>
    </div>
</footer>
"""
    with open(os.path.join(theme_folder, "layouts", "footer.php"), "w", encoding="utf-8") as f:
        f.write(footer_php)

    # 5. layouts/sidebar.php
    sidebar_php = """<div class="widget-box bg-white p-6 rounded-xl shadow-sm border border-gray-100 text-center">
    <h3 class="text-base font-bold text-gray-900 mb-4 border-b pb-2 text-left">Kepala Desa</h3>
    <img src="<?= gambar_pamong($desa['foto_kepala_desa']); ?>" alt="Kepala Desa" class="w-28 h-28 object-cover rounded-full mx-auto mb-3 shadow">
    <h4 class="font-bold text-gray-800"><?= $desa['nama_kepala_desa']; ?></h4>
    <p class="text-xs text-gray-500">Kepala Desa <?= $desa['nama_desa']; ?></p>
</div>
"""
    with open(os.path.join(theme_folder, "layouts", "sidebar.php"), "w", encoding="utf-8") as f:
        f.write(sidebar_php)

    # 6. partials/apbdes.php
    apbdes_php = """<div class="widget-box bg-white p-6 rounded-xl shadow-sm border border-gray-100">
    <h3 class="text-base font-bold text-gray-900 mb-4 flex items-center justify-between border-b pb-2">
        <span>Transparansi APBDes</span>
        <span class="text-xs text-blue-600 bg-blue-50 px-2 py-1 rounded">Tahun <?= date('Y'); ?></span>
    </h3>
    <div class="space-y-4">
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="font-medium text-gray-600">Pendapatan Desa</span>
                <span class="font-bold text-green-600">Rp <?= number_format($transparansi['pendapatan'] ?? 1250000000, 0, ',', '.'); ?></span>
            </div>
            <div class="w-full bg-gray-200 h-2 rounded-full overflow-hidden">
                <div class="bg-green-500 h-2 rounded-full" style="width: 85%"></div>
            </div>
        </div>
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="font-medium text-gray-600">Belanja Desa</span>
                <span class="font-bold text-orange-600">Rp <?= number_format($transparansi['belanja'] ?? 1180000000, 0, ',', '.'); ?></span>
            </div>
            <div class="w-full bg-gray-200 h-2 rounded-full overflow-hidden">
                <div class="bg-orange-500 h-2 rounded-full" style="width: 78%"></div>
            </div>
        </div>
    </div>
</div>
"""
    with open(os.path.join(theme_folder, "partials", "apbdes.php"), "w", encoding="utf-8") as f:
        f.write(apbdes_php)

    # 7. partials/peta.php
    peta_php = """<div class="widget-box bg-white p-6 rounded-xl shadow-sm border border-gray-100">
    <h3 class="text-base font-bold text-gray-900 mb-4 border-b pb-2">Peta Wilayah Desa</h3>
    <div id="peta-desa" style="height: 320px;" class="rounded-lg overflow-hidden border border-gray-200"></div>
</div>
"""
    with open(os.path.join(theme_folder, "partials", "peta.php"), "w", encoding="utf-8") as f:
        f.write(peta_php)

    # 8. partials/artikel.php
    artikel_php = """<div class="widget-box bg-white p-6 rounded-xl shadow-sm border border-gray-100">
    <h3 class="text-base font-bold text-gray-900 mb-4 border-b pb-2">Kabar Desa Terbaru</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <article class="border border-gray-100 rounded-lg p-3 hover:shadow-md transition">
            <div class="h-32 bg-gray-100 rounded mb-2 overflow-hidden flex items-center justify-center text-gray-400">
                <span>Foto Berita</span>
            </div>
            <span class="text-xs text-blue-600 font-semibold">Pembangunan</span>
            <h4 class="font-bold text-sm text-gray-800 line-clamp-2 mt-1">Penyaluran Bantuan Langsung Tunai (BLT) Berjalan Tertib</h4>
            <span class="text-xs text-gray-400 mt-2 block"><?= date('d M Y'); ?></span>
        </article>
    </div>
</div>
"""
    with open(os.path.join(theme_folder, "partials", "artikel.php"), "w", encoding="utf-8") as f:
        f.write(artikel_php)

    # 9. assets/css/theme.css
    css_content = """/* Tema OpenSID Modern */
:root {
    --primary: #2563eb;
    --primary-hover: #1d4ed8;
    --bg-surface: #ffffff;
    --text-main: #1f2937;
    --border-color: #e5e7eb;
}

body {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: #f8fafc;
    color: var(--text-main);
    margin: 0;
}

.desa-header {
    background: #ffffff;
    border-bottom: 1px solid var(--border-color);
}

.nav-link {
    color: #4b5563;
    text-decoration: none;
    transition: color 0.2s;
}
.nav-link:hover { color: var(--primary); }

.btn-mandiri {
    background-color: var(--primary);
    color: #ffffff;
    padding: 6px 14px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
}
.btn-mandiri:hover { background-color: var(--primary-hover); }

.widget-box {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: 12px;
}
"""
    with open(os.path.join(theme_folder, "assets", "css", "theme.css"), "w", encoding="utf-8") as f:
        f.write(css_content)

    # 10. assets/js/theme.js
    js_content = """document.addEventListener('DOMContentLoaded', function() {
    var petaElem = document.getElementById('peta-desa');
    if (petaElem && typeof L !== 'undefined') {
        var map = L.map('peta-desa').setView([-1.2, 124.8], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);
    }
});
"""
    with open(os.path.join(theme_folder, "assets", "js", "theme.js"), "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"[+] Kerangka tema '{slug}' berhasil dibuat di: {theme_folder}")

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
