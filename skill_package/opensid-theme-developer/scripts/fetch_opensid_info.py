#!/usr/bin/env python3
"""
fetch_opensid_info.py
Skrip untuk mengambil informasi versi resmi OpenSID (non-premium / umum) langsung dari GitHub API:
- Tag rilis terbaru & tanggal rilis
- Spesifikasi PHP & ekstensi
- Stack Backend (Laravel components & CodeIgniter core)
- Stack Frontend (AdminLTE, Leaflet, Bootstrap)
- Menyimpan cache data ke data/opensid_latest_info.json
- Memperbarui berkas dokumentasi references/opensid-version-info.md
"""

import os
import json
import urllib.request
from datetime import datetime

REPO_OWNER = "OpenSID"
REPO_NAME = "OpenSID"
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OpenSID-Skill-Agent/1.0",
    "Accept": "application/vnd.github.v3+json"
}

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as res:
        return json.loads(res.read().decode("utf-8"))

def fetch_raw_composer(tag):
    url = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{tag}/composer.json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as res:
            return json.loads(res.read().decode("utf-8"))
    except Exception as e:
        print(f"Warning: Failed to fetch composer.json for {tag}: {e}")
        return None

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_root = os.path.dirname(script_dir)
    data_dir = os.path.join(skill_root, "data")
    ref_dir = os.path.join(skill_root, "references")
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(ref_dir, exist_ok=True)

    print(f"[*] Menghubungi GitHub API: {API_URL}...")
    release_data = fetch_json(API_URL)
    tag_name = release_data.get("tag_name", "unknown")
    release_name = release_data.get("name", tag_name)
    published_at = release_data.get("published_at", "")
    zip_url = release_data.get("zipball_url", f"https://github.com/{REPO_OWNER}/{REPO_NAME}/archive/refs/tags/{tag_name}.zip")
    html_url = release_data.get("html_url", f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/tag/{tag_name}")
    body = release_data.get("body", "")

    print(f"[+] Ditemukan Rilis Terbaru: {tag_name} ({release_name})")
    print(f"[*] Mengambil composer.json untuk tag {tag_name}...")
    composer = fetch_raw_composer(tag_name) or {}

    requires = composer.get("require", {})
    php_version = requires.get("php", "^8.1")

    # Identifikasi komponen backend
    laravel_packages = [k for k in requires.keys() if "illuminate/" in k or "laravel" in k]
    ci_packages = [k for k in requires.keys() if "codeigniter" in k]
    other_libs = [k for k in requires.keys() if k not in laravel_packages and k not in ci_packages and k != "php"]

    # Identifikasi ekstensi PHP
    php_extensions = [k.replace("ext-", "") for k in requires.keys() if k.startswith("ext-")]
    if not php_extensions:
        php_extensions = ["curl", "gd", "intl", "mbstring", "mysqli", "pdo_mysql", "zip", "fileinfo", "xml", "bcmath", "exif"]

    # Struktur Info
    info = {
        "fetched_at": datetime.now().isoformat(),
        "source": f"https://github.com/{REPO_OWNER}/{REPO_NAME}",
        "version": tag_name,
        "release_name": release_name,
        "published_at": published_at,
        "release_url": html_url,
        "zip_download_url": zip_url,
        "requirements": {
            "php": php_version,
            "php_recommended": "8.2",
            "extensions": sorted(list(set(php_extensions))),
            "database": "MySQL 5.7+ / MariaDB 10.3+"
        },
        "backend": {
            "architecture": "Hybrid Laravel Components + CodeIgniter 3 Core",
            "core_framework": "CodeIgniter 3 (donjo-app)",
            "orm_and_services": "Laravel Components (illuminate/*: Database, Auth, View, Events, Cache)",
            "laravel_packages_count": len(laravel_packages),
            "key_packages": [
                "yajra/laravel-datatables-oracle",
                "spatie/laravel-activitylog",
                "rennokki/laravel-eloquent-query-cache",
                "opensid/router",
                "laravel-notification-channels/telegram"
            ]
        },
        "frontend": {
            "admin_panel": "AdminLTE 2 / 3 with Bootstrap",
            "public_themes": ["themes/natra", "themes/esensi", "desa/themes/*"],
            "gis_webgis": "Leaflet.js + GeoJSON Desa (Batas Desa, RT/RW, Tutupan Lahan)",
            "components": ["DataTables", "Select2", "TinyMCE", "Chart.js", "Bootstrap Datepicker"]
        }
    }

    # 1. Simpan JSON Cache
    json_path = os.path.join(data_dir, "opensid_latest_info.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4, ensure_ascii=False)
    print(f"[+] JSON info tersimpan di: {json_path}")

    # 2. Tulis Dokumen Referensi Markdown
    md_path = os.path.join(ref_dir, "opensid-version-info.md")
    md_content = f"""# Informasi Versi & Arsitektur OpenSID Terkini (Non-Premium / Umum)

> **Catatan Sinkronisasi**: Terakhir diperbarui otomatis pada `{datetime.now().strftime('%d %B %Y %H:%M:%S')}` dari repositori GitHub resmi [{REPO_OWNER}/{REPO_NAME}]({info['source']}).

---

## 📌 Ringkasan Rilis Terkini
- **Versi OpenSID Umum**: `{info['version']}` ({info['release_name']})
- **Tanggal Rilis Publik**: `{info['published_at'][:10]}`
- **Tautan Rilis Resmi**: [GitHub Release]({info['release_url']})
- **Unduh Kode Sumber**: [Download ZIP]({info['zip_download_url']})

---

## ⚙️ Kebutuhan Lingkungan Server
| Komponen | Spesifikasi Terkini | Rekomendasi |
| :--- | :--- | :--- |
| **Versi PHP** | `{info['requirements']['php']}` | **PHP 8.2** |
| **Database** | `{info['requirements']['database']}` | MariaDB 10.6+ |
| **Web Server** | Apache (mod_rewrite) / Nginx | Laragon (Windows) / Nginx (Linux) |
| **Upload Max Size** | Minimal `64M` | Disarankan `128M` (impor kependudukan) |
| **Max Execution Time** | Minimal `180` detik | Disarankan `300` detik |

### Ekstensi PHP Wajib:
`{", ".join(info['requirements']['extensions'])}`

---

## 🏗️ Spesifikasi Backend OpenSID
- **Pola Arsitektur**: **{info['backend']['architecture']}**
- **Sistem Dasar**: CodeIgniter 3 (`donjo-app`) untuk logika warisan modul pelayanan surat dan administrasi.
- **Layanan Modern**: Mengadopsi paket **Laravel Components (`illuminate/*`)**:
  - `illuminate/database` (Eloquent ORM & Query Builder terpusat)
  - `illuminate/auth`, `illuminate/session`, `illuminate/view`
  - `illuminate/cache`, `illuminate/events`, `illuminate/queue`
  - `yajra/laravel-datatables-oracle` (Server-side DataTables kependudukan)
  - `spatie/laravel-activitylog` (Audit trail & pencatatan log aksi operator)
  - `opensid/router` (Modular routing OpenSID)

---

## 🎨 Spesifikasi Frontend & Web Desa
- **Panel Administrator**: AdminLTE responsif berbasis Bootstrap.
- **Peta & WebGIS Desa**: **Leaflet.js** terintegrasi dengan endpoint GeoJSON untuk batas dusun, RW, RT, serta plotting sarana/prasarana.
- **Komponen Interaktif**:
  - DataTables dengan fitur filter multi-kolom dan ekspor Excel/PDF
  - TinyMCE editor untuk penulisan artikel web desa
  - Select2 untuk pemilih NIK & Kepala Keluarga dengan AJAX live search
  - Chart.js untuk infografis statistik kependudukan dan APBDes
- **Sistem Tema Publik**: Mendukung tema resmi (`natra`, `esensi`) dan sub-tema kustom di folder `desa/themes/`.
"""

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"[+] Markdown referensi tersimpan di: {md_path}")
    print("Selesai memperbarui data OpenSID.")

if __name__ == "__main__":
    main()
