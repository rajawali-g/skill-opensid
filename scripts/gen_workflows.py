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
# 2. WORKFLOWS
# ==========================================

# Fitur 1
write_file("workflows/check-latest-release.md", """# Workflow: Check Latest Release (Fitur 1)

Prosedur verifikasi rilis terbaru OpenSID Free:

1. **Jalankan Script Fetcher**:
   Jalankan `python scripts/fetch_opensid_info.py` atau periksa langsung API GitHub `https://api.github.com/repos/OpenSID/OpenSID/releases`.
2. **Filter Rilis Komunitas**:
   Pastikan rilis berasal dari branch `umum` atau rilis Free publik.
3. **Catat Rincian**:
   Simpan versi, tag, tanggal rilis, dan URL rilis ke `data/opensid_latest_info.json`.
4. **Verifikasi Kebutuhan Sistem**:
   Catat versi minimum PHP yang dipersyaratkan.
5. **Keluaran**:
   Informasi rilis mutakhir yang terverifikasi untuk digunakan oleh Fitur 2 dan 3.
""")

# Fitur 2
write_file("workflows/analyze-release-history.md", """# Workflow: Analyze Release History (Fitur 2)

Prosedur analisis riwayat rilis OpenSID:

1. **Ambil Data Tag & Changelog**: Kumpulkan riwayat tag rilis OpenSID dari GitHub.
2. **Petakan Perubahan Arsitektur**:
   - Identifikasi kapan Blade view engine mulai digunakan.
   - Periksa perubahan helper web (misal helper slider, artikel, agenda).
3. **Klasifikasikan Perubahan**:
   Gunakan klasifikasi pada `references/release-change-classification.md`.
4. **Simpan Basis Pengetahuan**: Catat hasil di `knowledge/releases/version-matrix.md`.
""")

write_file("workflows/inspect-standard-theme.md", """# Workflow: Inspect Standard Theme (Fitur 2)

Prosedur inspeksi tema default:

1. Periksa berkas ZIP tema standar di folder `standard/` (`esensi.zip`, `natra.zip`).
2. Bedah struktur direktori, layout, partials, dan widgets.
3. Ekstrak schema variabel view dari `@include` dan pemanggilan Blade.
4. Periksa `config.json` untuk melihat opsi kustomisasi admin bawaan.
5. Perbarui `references/standard-theme-architecture.md` bila ditemukan pola baru.
""")

write_file("workflows/compare-theme-architecture.md", """# Workflow: Compare Theme Architecture (Fitur 2 & 5)

Prosedur membandingkan arsitektur tema:

1. Bandingkan struktur tema target dengan arsitektur standar OpenSID.
2. Identifikasi file yang hilang (misal `widgets/` yang belum lengkap).
3. Periksa kesesuaian namespace `theme::`.
4. Buat daftar ketidaksesuaian (gap analysis) untuk perbaikan.
""")

# Fitur 3
write_file("workflows/create-new-theme.md", """# Workflow: Create New Theme (Fitur 3)

Prosedur pembuatan tema baru:

1. Tentukan target versi OpenSID dan identitas tema (nama, slug, deskripsi).
2. Buat struktur direktori tema sesuai standar di `themes_output/<nama_tema>/`.
3. Buat manifest tema: `config.json`, `composer.json`, `catatan_rilis.md`, `index.html`.
4. Implementasikan resources Blade:
   - `commons/` (`header`, `footer`, `meta`, `navbar`)
   - `layouts/` (`index`)
   - `partials/` (`artikel`, `slider`, `pagination`)
   - `widgets/` (widget dinamis OpenSID)
   - `template.blade.php`
5. Buat stylesheet dan aset mandiri di `assets/`.
6. Kemas tema ke dalam ZIP dengan nama `<nama_tema>.zip`.
7. Catat tema di katalog.
""")

write_file("workflows/develop-catalog-theme.md", """# Workflow: Develop Catalog Theme (Fitur 3 & 5)

Prosedur pengembangan tema yang ada di katalog:

1. Muat kode sumber tema dari `themes_output/<nama_tema>/`.
2. Periksa dokumentasi tema di `catalog/products/<nama_tema>.md`.
3. Lakukan modifikasi fitur atau perbaikan bug secara terisolasi.
4. Uji fungsi dan tampilannya.
5. Perbarui nomor versi dan kemas ulang ZIP.
""")

# Fitur 4
write_file("workflows/interview-theme-requirements.md", """# Workflow: Interview Theme Requirements (Fitur 4)

Prosedur wawancara kebutuhan desain:

1. **Identitas**: Tanyakan nama tema, konsep, dan sasaran desa.
2. **Karakter Visual**: Klasik pedesaan, modern elegan, atau digital futuristik.
3. **Palet Warna & Tipografi**: Warna identitas lokal desa, font judul & badan teks.
4. **Struktur Halaman**: Susunan hero banner, widget prioritas, berita utama, dan footer.
5. **Fitur Khas**: Fitur peta potensi, galeri produk UMKM desa, agenda kegiatan, dsb.
6. **Rangkuman**: Susun ringkasan sebelum pembuatan kode dimulai.
""")

write_file("workflows/generate-theme-specification.md", """# Workflow: Generate Theme Specification (Fitur 4)

Prosedur pembuatan spesifikasi tema:

1. Gunakan template `templates/theme-specification.md`.
2. Isi ringkasan identitas, target pengguna, dan fitur utama.
3. Definisikan token desain (warna, font, spacing) di `templates/design-tokens.md`.
4. Petakan struktur halaman publik.
5. Simpan spesifikasi di dokumentasi tema.
""")

write_file("workflows/manage-theme-version.md", """# Workflow: Manage Theme Version (Fitur 4)

Prosedur Semantic Versioning tema (`MAJOR.MINOR.PATCH`):

1. **MAJOR** (x.0.0): Perubahan struktur besar yang tidak kompatibel dengan versi sebelumnya.
2. **MINOR** (0.x.0): Penambahan widget, halaman baru, atau layout baru yang tetap kompatibel.
3. **PATCH** (0.0.x): Perbaikan styling CSS, perbaikan typo, atau perbaikan bug kecil.
4. Update `catatan_rilis.md` di dalam folder tema.
""")

# Fitur 5
write_file("workflows/update-catalog-theme.md", """# Workflow: Update Catalog Theme (Fitur 5)

Prosedur pembaruan tema katalog terhadap versi OpenSID:

1. Tentukan versi OpenSID target.
2. Periksa perubahan breaking change OpenSID.
3. Terapkan prinsip preserve-first (jangan hapus fitur khas tema).
4. Perbarui helper atau kontrak view yang mengalami penyesuaian.
5. Jalankan validasi pengujian.
""")

write_file("workflows/enhance-catalog-theme-design.md", """# Workflow: Enhance Catalog Theme Design (Fitur 5)

Prosedur penyegaran desain tema katalog:

1. Perbarui design tokens (warna, font, kartu, tombol).
2. Perbaiki keterbacaan tipografi dan rasio kontras.
3. Optimalkan layout responsif pada perangkat seluler.
4. Uji estetika visual.
""")

write_file("workflows/add-catalog-theme-feature.md", """# Workflow: Add Catalog Theme Feature (Fitur 5)

Prosedur penambahan fitur baru pada tema katalog:

1. Rancang komponen baru (misal widget transparansi anggaran, direktori aparatur).
2. Buat file view Blade terkait di `resources/views/partials/` atau `widgets/`.
3. Tambahkan konfigurasi di `config.json` jika membutuhkan pengaturan admin.
4. Update dokumentasi fitur di halaman produk katalog.
""")

# Fitur 6
write_file("workflows/validate-theme.md", """# Workflow: Validate Theme (Fitur 6)

Prosedur validasi komprehensif tema:

1. Periksa integritas file: pastikan `template.blade.php`, `config.json`, dan assets tersedia.
2. Periksa sintaks Blade: pastikan tidak ada tag unclosed atau sintaks php fatal.
3. Periksa dependensi asset lokal: tidak ada link asset yang 404.
4. Periksa integrasi widget: pastikan looping widget menggunakan `@includeIf`.
""")

write_file("workflows/review-beta-theme.md", """# Workflow: Review Beta Theme (Fitur 6)

Prosedur peninjauan tema berstatus beta:

1. Saring tema di katalog dengan status `beta` atau `testing`.
2. Jalankan check-list pengujian fungsi dan visual.
3. Catat issue / bug yang ditemukan.
4. Tentukan status baru: `revision_required` atau `approved`.
""")

write_file("workflows/check-opensid-compatibility.md", """# Workflow: Check OpenSID Compatibility (Fitur 6)

Prosedur pengujian kompatibilitas OpenSID:

1. Uji tema terhadap versi OpenSID Free target.
2. Periksa pemanggilan variabel controller publik: `$desa`, `$artikel`, `$slider`, `$menu`.
3. Pastikan tidak ada dependensi fitur OpenSID Premium.
4. Buat laporan kompatibilitas `templates/compatibility-report.md`.
""")

write_file("workflows/run-theme-functional-tests.md", """# Workflow: Run Theme Functional Tests (Fitur 6)

Prosedur pengujian fungsional tema:

1. Uji Beranda: Slider, Berita Terkini, Widget Sidebar, Footer.
2. Uji Halaman Baca Artikel: Judul, konten, meta author, share button, komentar.
3. Uji Navigasi: Menu dinamis, sub-menu dropdown, mobile hamburger menu.
4. Uji Pencarian & Pagination: Tampilan form pencarian dan tombol halaman.
5. Catat hasil di `templates/theme-test-report.md`.
""")

write_file("workflows/evaluate-responsive-design.md", """# Workflow: Evaluate Responsive Design (Fitur 6)

Prosedur evaluasi responsivitas:

1. Uji Mobile (320px - 480px): Tidak ada horizontal scrolling, ukuran tap target cukup besar (>= 44px).
2. Uji Tablet (768px - 1024px): Layout kolom beradaptasi rapi.
3. Uji Desktop (1200px+): Grid seimbang dan nyaman dibaca.
""")

write_file("workflows/evaluate-theme-aesthetics.md", """# Workflow: Evaluate Theme Aesthetics (Fitur 6)

Prosedur evaluasi estetika & visual:

1. Harmoni palet warna dan kontras teks.
2. Konsistensi radius, bayangan (shadow), dan spacing.
3. Kualitas tipografi (font pairing judul dan badan teks).
4. Penilaian kelayakan tampilan sesuai karakter desa.
""")

write_file("workflows/certify-theme-release.md", """# Workflow: Certify Theme Release (Fitur 6)

Prosedur sertifikasi kelayakan rilis:

1. Kumpulkan laporan kompatibilitas, laporan fungsi, dan evaluasi visual.
2. Periksa Gate 1 s.d Gate 6.
3. Terbitkan persetujuan sertifikasi rilis (`templates/theme-release-approval.md`).
4. Ubah status tema menjadi `ready_to_publish`.
""")

# Fitur 7
write_file("workflows/publish-theme-catalog-entry.md", """# Workflow: Publish Theme Catalog Entry (Fitur 7)

Prosedur publikasi tema ke katalog:

1. Pastikan tema berstatus `ready_to_publish`.
2. Buat halaman produk di `catalog/products/<nama_tema>.md`.
3. Verifikasi paket ZIP dan checksum di `themes_output/<nama_tema>.zip`.
4. Daftarkan di indeks katalog `catalog/catalog-index.md`.
5. Ubah status rilis menjadi `published`.
""")

# Sub-workflows Licensing
write_file("workflows/license/define-license-policy.md", """# Workflow: Define License Policy (Fitur 6 & 7)

Prosedur penetapan kebijakan lisensi:

1. Tentukan jenis lisensi (Single Domain, Multi Domain, atau Unlimited Desa).
2. Tetapkan aturan aktivasi satu kali per domain terdaftar.
3. Tetapkan masa berlaku dan kebijakan pembaruan.
4. Siapkan ketentuan penanganan lisensi tidak aktif secara graceful.
""")

write_file("workflows/license/issue-license-key.md", """# Workflow: Issue License Key (Fitur 7)

Prosedur penerbitan kunci lisensi:

1. Terima identitas pemesan/desa dan nomor transaksi.
2. Generate token kunci unik (kombinasi SHA-256 + cryptographic random string).
3. Simpan record di database server lisensi:
   `product_id`, `license_key_hash`, `order_ref`, `status: issued`.
4. Kirimkan lisensi kepada pengguna beserta petunjuk aktivasi.
""")

write_file("workflows/license/validate-license.md", """# Workflow: Validate License (Fitur 6 & 7)

Prosedur validasi lisensi:

1. Klien tema mengirimkan handshake terenkripsi ke license server (Domain + Product ID + License Key).
2. Server memvalidasi kecocokan kunci dan status hak penggunaan.
3. Server mengembalikan status `valid` beserta token cache sementara (TTL 24-72 jam).
4. Jika server unreachable, gunakan grace period cache status validasi.
""")

write_file("workflows/license/activate-theme-license.md", """# Workflow: Activate Theme License (Fitur 6 & 7)

Prosedur aktivasi tema di OpenSID:

1. Admin desa memasukkan License Key di menu pengaturan tema.
2. Sistem melakukan request aktivasi pertama kali ke server lisensi.
3. Server mengikat domain desa ke license key (`domain_bound`).
4. Lisensi resmi berstatus `active`.
""")

write_file("workflows/license/revoke-license.md", """# Workflow: Revoke License (Fitur 6 & 7)

Prosedur pencabutan lisensi:

1. Admin server memeriksa pelanggaran ketentuan penggunaan atau refund.
2. Ubah status kunci menjadi `revoked` di database license server.
3. Saat validasi berikutnya, klien tema menerima status pencabutan dan menampilkan pemberitahuan aktivasi ulang.
""")

write_file("workflows/license/handle-license-transfer.md", """# Workflow: Handle License Transfer (Fitur 6 & 7)

Prosedur pemindahan lisensi (Ganti Domain / Server):

1. Pengguna mengajukan transfer domain resmi dengan bukti kepemilikan lisensi.
2. Admin / sistem mereset `domain_bound` lama.
3. Pengguna melakukan aktivasi ulang pada domain baru.
4. Catat riwayat transfer pada audit log server.
""")

print("Workflows completed.")
