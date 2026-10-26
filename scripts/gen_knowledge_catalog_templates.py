# -*- coding: utf-8 -*-
import os

BASE_SKILL_DIR = r"d:\project_opensid\.agents\skills\opensid"

def write_file(rel_path, content):
    full_path = os.path.join(BASE_SKILL_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {rel_path}")

# ==========================================
# 3. KNOWLEDGE
# ==========================================
write_file("knowledge/releases/README.md", """# OpenSID Releases Knowledge Base

Basis pengetahuan mengenai riwayat rilis OpenSID Free/non-Premium yang diverifikasi.
Mencakup persyaratan sistem, perubahan fitur, arsitektur tema, dan matriks kompatibilitas antarversi.
""")

write_file("knowledge/releases/release-index.md", """# Indeks Riwayat Rilis OpenSID (Free)

Daftar rilis OpenSID Free yang telah diidentifikasi dan diverifikasi:

| Versi / Tag | Tanggal Rilis | Branch / Target | PHP Support | Theme Engine | Status Verifikasi |
|---|---|---|---|---|---|
| `v2408.0.0` | 2024-08 | `umum` | PHP 8.1 - 8.2 | Blade (`theme::`) | Verified |
| `v2308.0.0` | 2023-08 | `umum` | PHP 8.0 - 8.1 | Blade (`theme::`) | Verified |
| `v22.08` | 2022-08 | `umum` | PHP 7.4 - 8.0 | CI3 / Legacy | Verified |

*Catatan: Riwayat diperbarui secara berkala melalui Fitur 1 & 2.*
""")

write_file("knowledge/releases/version-matrix.md", """# Matriks Versi & Kompatibilitas OpenSID

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
""")

write_file("knowledge/standard-architectures/README.md", """# Arsitektur Standar Tema OpenSID

Dokumentasi arsitektur baku tema resmi OpenSID (Natra dan Esensi) yang menjadi referensi utama pengembangan tema.
""")

write_file("knowledge/standard-architectures/versions/v2408-blade.md", """# Arsitektur Tema OpenSID v2408.0.0+ (Blade Engine)

Arsitektur standar yang berlaku untuk rilis OpenSID modern:
- Engine: Laravel Blade
- Namespace: `theme::`
- Mandatory Files:
  - `template.blade.php`: Controller entry view
  - `config.json`: Skema pengaturan tema di Admin Web
  - `composer.json`: Type definition
  - `catatan_rilis.md`: Changelog tema
  - `index.html`: Directory protection
- Partials Structure:
  - `commons/`: header, footer, meta, navbar
  - `layouts/`: index (wrapper utama)
  - `partials/`: komponen artikel, slider, pagination
  - `widgets/`: template widget dinamis
""")

# ==========================================
# 4. CATALOG
# ==========================================
write_file("catalog/catalog-index.md", """# Katalog Tema OpenSID

Katalog resmi tema hasil rancangan OpenSID Theme Developer.

| ID Tema | Nama Tema | Gaya Visual | Versi Tema | Target OpenSID | Status Rilis | Paket Distribusi |
|---|---|---|---|---|---|---|
| `tema-pedesaan-klasik` | Tema Pedesaan Klasik | Tradisional, Hangat, Ramah Warga | 1.0.0 | v2408.0.0+ | `published` | [ZIP](file:///d:/project_opensid/themes_output/tema-pedesaan-klasik.zip) |
| `tema-desa-modern` | Tema Desa Modern | Bersih, Minimalis, Pelayanan Publik | 1.0.0 | v2408.0.0+ | `published` | [ZIP](file:///d:/project_opensid/themes_output/tema-desa-modern.zip) |
| `tema-desa-digital` | Tema Desa Digital | Futuristik, Dark Navy, Data & Transparansi | 1.0.0 | v2408.0.0+ | `published` | [ZIP](file:///d:/project_opensid/themes_output/tema-desa-digital.zip) |
""")

write_file("catalog/products/tema-pedesaan-klasik.md", """# Produk: Tema Pedesaan Klasik

- **ID Produk**: `tema-pedesaan-klasik`
- **Nama Produk**: Tema Pedesaan Klasik
- **Versi**: 1.0.0
- **Kategori**: Desa Tradisional, Wisata, dan Budaya
- **Engine**: Laravel Blade (`theme::`)
- **Status Rilis**: `published`

## Deskripsi
Tema dengan nuansa warna alam yang hangat (hijau sage, cokelat kayu, dan krem), dirancang untuk mencerminkan keramahan pedesaan, keindahan alam, serta kegiatan kebudayaan desa.

## Fitur Utama
1. Banner hero alam pedesaan yang menenangkan.
2. Kartu artikel berita dengan tipografi hangat dan mudah dibaca oleh warga lansia.
3. Integrasi widget statistik warga dan galeri tradisi lokal.
4. Tata letak mobile-first dengan kontras tinggi.

## Spesifikasi Teknis
- Kompatibel: OpenSID Free v2408.0.0+
- Persyaratan PHP: PHP 8.1+
- File Paket: `themes_output/tema-pedesaan-klasik.zip`
""")

write_file("catalog/products/tema-desa-modern.md", """# Produk: Tema Desa Modern

- **ID Produk**: `tema-desa-modern`
- **Nama Produk**: Tema Desa Modern
- **Versi**: 1.0.0
- **Kategori**: Pelayanan Administrasi & Pemerintahan Desa
- **Engine**: Laravel Blade (`theme::`)
- **Status Rilis**: `published`

## Deskripsi
Tema berorientasi birokrasi ramah warga dengan gaya minimalis, bersih, dan mengedepankan kecepatan akses layanan publik desa (surat pengantar, pengaduan, dan agenda kantor desa).

## Fitur Utama
1. Quick Action Shortcut untuk permohonan surat dan layanan online.
2. Tata letak modular dengan visual card elegan dan profesional.
3. Desain kontras tinggi (biru laut dan putih bersih) untuk kenyamanan baca.
4. Kecepatan muat ringan tanpa framework CSS berat.

## Spesifikasi Teknis
- Kompatibel: OpenSID Free v2408.0.0+
- Persyaratan PHP: PHP 8.1+
- File Paket: `themes_output/tema-desa-modern.zip`
""")

write_file("catalog/products/tema-desa-digital.md", """# Produk: Tema Desa Digital

- **ID Produk**: `tema-desa-digital`
- **Nama Produk**: Tema Desa Digital (Smart Village)
- **Versi**: 1.0.0
- **Kategori**: Smart Village, Transparansi Data & SDGs
- **Engine**: Laravel Blade (`theme::`)
- **Status Rilis**: `published`

## Deskripsi
Tema inovatif untuk desa cerdas (Smart Village) dengan tampilan sleek, modern gradient (cyan, emerald, dan deep navy), serta visualisasi metrik data pembangunan desa.

## Fitur Utama
1. Dashboard ringkasan APBDes dan capaian SDGs Desa interaktif.
2. Tampilan modern dark-accented dengan elemen glassmorphism lembut.
3. Quick search berita dan layanan informasi desa instan.
4. Desain responsif optimal untuk perangkat smartphone generasi terbaru.

## Spesifikasi Teknis
- Kompatibel: OpenSID Free v2408.0.0+
- Persyaratan PHP: PHP 8.1+
- File Paket: `themes_output/tema-desa-digital.zip`
""")

# ==========================================
# 5. TEMPLATES
# ==========================================
write_file("templates/theme-specification.md", """# [Template] Theme Specification

## Identitas Tema
- **Nama Tema**: 
- **ID Slug**: 
- **Target Pengguna**: 
- **Konsep Desain**: 

## Arsitektur & Lingkungan
- **Target Versi OpenSID**: Free v2408.0.0+
- **View Engine**: Laravel Blade (`theme::`)
- **PHP Support**: PHP 8.1+

## Struktur Halaman & Layout
- **Header**: 
- **Hero / Banner**: 
- **Konten Utama**: 
- **Sidebar & Widgets**: 
- **Footer**: 
""")

write_file("templates/design-tokens.md", """# [Template] Design Tokens

## Palet Warna
- `--color-primary`: 
- `--color-secondary`: 
- `--color-accent`: 
- `--color-background`: 
- `--color-surface`: 
- `--color-text`: 

## Tipografi
- **Heading Font**: 
- **Body Font**: 
- **Base Size**: 16px / 1rem

## Radius & Spacing
- `--radius-sm`: 4px
- `--radius-md`: 8px
- `--radius-lg`: 16px
- `--space-unit`: 8px
""")

write_file("templates/version-history.md", """# [Template] Version History

Format Semantic Versioning (`MAJOR.MINOR.PATCH`):

## [1.0.0] - YYYY-MM-DD
### Added
- Inisialisasi awal tema.
- Layout responsif beranda, artikel, dan widget.
### Fixed
- Perbaikan styling mobile.
""")

write_file("templates/compatibility-report.md", """# [Template] Compatibility Report

- **Target Tema**: 
- **Versi Tema**: 
- **Versi Target OpenSID**: 

| Komponen Diuji | Hasil Uji | Keterangan |
|---|---|---|
| View Engine Blade | Pass / Fail | Sintaks `@include` |
| Namespace `theme::` | Pass / Fail | Pemanggilan template |
| Variabel `$desa` | Pass / Fail | Fallback data nama desa |
| Variabel `$artikel` | Pass / Fail | List berita dan pagination |
| Widget Dinamis | Pass / Fail | `@includeIf` widgets |
""")

write_file("templates/theme-test-report.md", """# [Template] Theme Test Report

- **Tanggal Pengujian**: 
- **Penguji**: 
- **Status Akhir**: `approved` / `revision_required`

## Ringkasan Hasil
- **Uji Navigasi**: Pass
- **Uji Responsivitas**: Pass
- **Uji Tampilan Artikel**: Pass
- **Uji Widget Sidebar**: Pass
""")

write_file("templates/theme-quality-report.md", """# [Template] Theme Quality Report (QA)

- **Skor Kualitas Visual**: (Skala 1-100)
- **Skor Aksesibilitas (Kontras WCAG AA)**: (Skala 1-100)
- **Skor Responsivitas Multi-Resolusi**: (Skala 1-100)

## Catatan Evaluasi
- Desktop: Tampilan proporsional.
- Tablet: Grid menyesuaikan dengan baik.
- Mobile: Menu burger dan konten utama rapi.
""")

write_file("templates/theme-release-approval.md", """# [Template] Theme Release Approval

- **Nama Produk**: 
- **Versi**: 
- **Status**: `ready_to_publish`
- **Disetujui Oleh**: QA & Certification Gate
- **Tanggal Persetujuan**: 

## Pernyataan Kelayakan
Tema telah melewati seluruh tahap pemeriksaan teknis, kompatibilitas, responsivitas, dan keamanan kode tanpa temuan fatal.
""")

write_file("templates/catalog-product-page.md", """# [Template] Catalog Product Page

- **Nama Tema**: 
- **ID Produk**: 
- **Versi**: 
- **Kompatibilitas**: OpenSID Free v2408.0.0+
- **Harga / Lisensi**: 
- **Tautan Unduh Paket**: 

## Pratinjau Desain
[Lampirkan screenshot desktop dan mobile]

## Panduan Instalasi
1. Unduh file zip tema.
2. Buka Admin OpenSID -> Pengaturan -> Tema.
3. Unggah paket ZIP tema atau letakkan di folder `themes/`.
4. Aktifkan tema.
""")

write_file("templates/publication-checklist.md", """# [Template] Publication Checklist

Sebelum mempublikasikan tema ke katalog:
- [ ] Versi tema sudah Semantic Versioning.
- [ ] Kompatibel dengan OpenSID Free terverifikasi.
- [ ] Berkas ZIP lengkap dan dapat diekstrak rapi.
- [ ] Tidak ada kode rahasia / API key tertanam.
- [ ] Halaman katalog dan deskripsi lengkap.
- [ ] Berstatus `approved` dari Fitur 6.
""")

write_file("templates/release-manifest.md", """# [Template] Release Manifest

```json
{
  "product_id": "nama-tema",
  "name": "Nama Tema",
  "version": "1.0.0",
  "target_opensid": "v2408.0.0+",
  "package_file": "nama-tema.zip",
  "package_checksum_sha256": "",
  "release_date": "YYYY-MM-DD",
  "license_type": "standard",
  "status": "published"
}
```
""")

print("Knowledge, Catalog, and Templates completed.")
