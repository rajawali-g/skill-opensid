# -*- coding: utf-8 -*-
import os
import sys

BASE_SKILL_DIR = r"d:\project_opensid\.agents\skills\opensid"

def write_file(rel_path, content):
    full_path = os.path.join(BASE_SKILL_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {rel_path}")

# ==========================================
# 1. REFERENCES
# ==========================================

write_file("references/opensid-sources.md", """# OpenSID Official Sources & Repositories

Dokumen ini mencatat sumber resmi dan titik verifikasi untuk OpenSID Free (non-Premium).

## Sumber Utama
1. **Repository Utama**: [GitHub OpenSID/OpenSID](https://github.com/OpenSID/OpenSID)
2. **Releases**: [GitHub Releases](https://github.com/OpenSID/OpenSID/releases)
3. **Tags**: [GitHub Tags](https://github.com/OpenSID/OpenSID/tags)
4. **Branch Umum (Free/Community)**: [GitHub Tree umum](https://github.com/OpenSID/OpenSID/tree/umum)
5. **README Branch Umum**: [README.md Branch umum](https://github.com/OpenSID/OpenSID/blob/umum/README.md)
6. **Dokumentasi Resmi**: [Panduan OpenDesa](https://panduan.opendesa.id/id/opensid/dokumentasi)

## Aturan Verifikasi
- OpenSID Free menggunakan branch `umum`.
- Jangan berasumsi fitur OpenSID Premium ada pada OpenSID Free.
- Tag rilis OpenSID Free menggunakan format rilis bulanan/tahun (misal `v2408.0.0`).
""")

write_file("references/release-information.md", """# OpenSID Release Information Schema

Schema informasi yang harus dikumpulkan saat melakukan Release Discovery (Fitur 1).

## Format Data Rilis
Setiap rilis yang terverifikasi dicatat dengan atribut:
- `tag_name`: String (contoh: `v2408.0.0`)
- `published_at`: ISO 8601 Timestamp
- `is_prerelease`: Boolean
- `target_commitish`: Branch atau commit SHA
- `requirements`:
  - `php_min`: Versi minimum PHP (misal PHP 8.1 / 8.2)
  - `php_extensions`: List ekstensi yang wajib (intl, mbstring, curl, gd, mysqli/pdo_mysql, zip, bcmath)
  - `database`: MariaDB / MySQL version
  - `web_server`: Apache 2.4+ / Nginx
- `theme_engine`: Laravel Blade (`theme::` namespace)
- `release_notes_url`: URL release notes GitHub
- `verification_status`: `verified` | `partially_verified` | `unverified`
""")

write_file("references/release-change-classification.md", """# Release Change Classification

Klasifikasi dampak perubahan rilis OpenSID terhadap siklus hidup tema:

1. **Requirement Change**: Perubahan versi minimum PHP, ekstensi, web server.
2. **Architecture Change**: Perubahan direktori tema atau mekanisme pemuatan view.
3. **Template Contract Change**: Perubahan variabel bawaan controller (misal `$artikel`, `$desa`, `$menu`), helper, atau direktif Blade.
4. **Frontend Change**: Pembaruan bootstrap, fontawesome, jquery, atau penghapusan CSS/JS legacy.
5. **Feature Change**: Fitur modul baru di OpenSID (misal IDM, SDGs, APBDes, Peta GeoJSON).
6. **Breaking Change**: Perubahan yang menyebabkan error fatal jika tema lama dijalankan di OpenSID baru.
7. **Security Change**: Aturan sanitasi XSS (`e()`, htmlspecialchars) dan token CSRF.
""")

write_file("references/standard-theme-architecture.md", """# Arsitektur Tema Standar OpenSID (Free / Non-Premium)

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
""")

write_file("references/theme-development-rules.md", """# Theme Development Rules

Aturan baku pengembangan tema OpenSID:

1. **Gunakan Namespace `theme::`**: Semua `@include` wajib menggunakan prefix `theme::`.
2. **Panggilan Aset Mandiri**: Gunakan helper `asset()` atau helper URL OpenSID `base_url("themes/{nama_tema}/assets/...")`.
3. **Dukungan Widget Dinamis**: Wajib memuat widget dengan syntax:
   `@includeIf("theme::widgets.{$widget['isi']}", $judul_widget)`
4. **Sanitasi Output**: Jangan gunakan `{!! $var !!}` tanpa sanitasi untuk data publik pengguna. Gunakan `{{ $var }}` default Blade.
5. **Responsif & Ringan**: Desain wajib mobile-first, zero horizontal overflow, dan tidak bergantung pada CDN eksternal berat tanpa fallback.
""")

write_file("references/compatibility-rules.md", """# Compatibility Rules

Aturan pemeliharaan kompatibilitas tema:

1. **Prinsip Preserve-First**: Jangan menghapus fitur yang sudah ada pada tema katalog saat upgrade.
2. **Fallback Handling**: Pastikan variabel yang mungkin tidak dikirimkan controller memiliki fallback (contoh: `$desa['nama_desa'] ?? 'Nama Desa'`).
3. **Kompatibilitas Versi PHP**: Sintaks tema harus kompatibel dengan versi PHP target OpenSID (PHP 8.1 - 8.3). Hindari fungsi deprecated.
4. **Isolasi Modul**: Jangan mengubah file core OpenSID. Semua modifikasi harus berada di dalam folder tema.
""")

write_file("references/theme-quality-standards.md", """# Theme Quality Standards (QA)

Standar penilaian kualitas tema sebelum rilis:

## 1. Visual & UI/UX
- Mobile responsiveness (320px, 375px, 768px, 1024px, 1440px).
- Keterbacaan kontras teks (WCAG AA).
- Konsistensi font, spacing, dan design tokens.
- Kerapian navigasi dropdown dan burger menu seluler.

## 2. Teknis & Performa
- Bebas error sintaks PHP dan Blade compile error.
- Bebas error console JavaScript.
- Waktu muat awal cepat, lazy loading gambar.
- Struktur HTML5 semantik (`<header>`, `<nav>`, `<main>`, `<article>`, `<footer>`).

## 3. Integrasi OpenSID
- Semua widget default OpenSID (agenda, aparatur, statistik, arsip berita, komentar, galeri) ter-render rapi.
- Navigasi menu dinamis (menu bertingkat / dropdown) berfungsi dengan baik.
- Tampilan artikel statis dan dinamis rapi.
""")

write_file("references/release-acceptance-criteria.md", """# Release Acceptance Criteria & Gates

Kriteria kelulusan tema untuk masuk ke status `ready_to_publish` / `published`:

1. **Gate 1: Compatibility Pass**: 100% kompatibel dengan versi target OpenSID Free.
2. **Gate 2: Functional Test Pass**: Semua skenario halaman (beranda, artikel, galeri, peta, widget) terverifikasi.
3. **Gate 3: Visual QA Pass**: Lolos uji multi-resolusi tanpa layout breaking.
4. **Gate 4: Security & Cleanliness**: Tidak ada kredensial atau debug dump (`var_dump`, `dd()`, console.log).
5. **Gate 5: Licensing Architecture Ready**: Terintegrasi dengan sistem lisensi dua lapis.
6. **Gate 6: Package Completeness**: Memiliki ZIP valid, `catatan_rilis.md`, `config.json`, dan dokumentasi instalasi.
""")

write_file("references/licensing-architecture.md", """# 2-Layer Licensing Architecture

Sistem perlindungan dan lisensi tema OpenSID:

## Lapis 1: Integrasi Tema (Client-side / Template Component)
- Tema memiliki identifier unik produk (`product_id`, `version`).
- Memiliki handler status lisensi yang anggun (graceful).
- Jika lisensi belum aktif / invalid, tampilkan notice aktivasi di admin atau banner yang informatif.
- **DILARANG MERUSAK SITUS PENGGUNA**: Jangan membuat layout crash atau loop freeze.

## Lapis 2: License Server & Database API
- Endpoint server lisensi memvalidasi token hak penggunaan.
- Database mencatat:
  - `product_id`
  - `license_key`
  - `domain_bound` (URL/domain instalasi OpenSID)
  - `status` (`active`, `expired`, `revoked`, `suspended`)
  - `activated_at` & `audit_logs`
- Kunci terikat per domain/instalasi resmi.
- Mendukung mekanisme transfer domain resmi (re-binding) dengan otorisasi.
""")

print("References completed.")
