# PANDUAN PENGGUNAAN & INSTALASI
# AI SKILL: OPENSID THEME DEVELOPER
### Untuk Google Antigravity IDE, Antigravity CLI, dan Agent AI

---

## 1. Tentang Skill Ini

**OpenSID Theme Developer** (`opensid-theme-developer`) adalah keahlian kecerdasan buatan (AI Skill) mandiri lintas platform yang dirancang untuk membimbing AI Assistant (seperti Antigravity) dalam menguasai seluruh siklus hidup pengembangan tema **OpenSID Free / Non-Premium**.

### Kemampuan 7 Fitur Utama:
1. **Fitur 1 (Release Discovery)**: Memeriksa dan memverifikasi rilis OpenSID Free terbaru dari GitHub resmi secara aktual.
2. **Fitur 2 (Architecture Analyzer)**: Menganalisis arsitektur tema standar (Laravel Blade, namespace `theme::`, kontrak view, dan helper).
3. **Fitur 3 (Theme Builder)**: Membangun tema baru atau mengembangkan tema katalog dengan struktur baku dan pengemasan ZIP otomatis.
4. **Fitur 4 (Interactive Designer & Semantic Versioning)**: Memandu wawancara interaktif kebutuhan visual, warna, tipografi, dan mengelola nomor versi tema (`MAJOR.MINOR.PATCH`).
5. **Fitur 5 (Catalog Updater & Enhancement)**: Memperbarui kompatibilitas tema terhadap versi OpenSID baru dengan prinsip *preserve-first* (tidak merusak fitur khas yang sudah ada).
6. **Fitur 6 (Quality Assurance & Licensing Lapis 1-2)**: Melakukan linter/inspeksi kelayakan teknis sebelum rilis dan mengelola arsitektur lisensi 2 lapis.
7. **Fitur 7 (Catalog Publishing & Distribution)**: Mengelola katalog tema dan menyiapkan paket rilis siap pakai.

---

## 2. Cara Pemasangan di Google Antigravity

Pilihlah salah satu cara pemasangan berikut yang paling mudah bagi Anda:

### Opsi A: Instalasi Otomatis (Direkomendasikan)
Di dalam folder ini sudah tersedia skrip installer otomatis:

- **Pengguna Windows (PowerShell)**:
  Buka terminal di folder ini, lalu jalankan:
  ```powershell
  .\install-skill.ps1
  ```
  *Skrip akan otomatis menyalin skill ke konfigurasi Global Antigravity (`~/.gemini/config/skills/`) dan Workspace aktif.*

- **Pengguna Linux / macOS / WSL (Bash)**:
  Buka terminal di folder ini, lalu jalankan:
  ```bash
  chmod +x install-skill.sh
  ./install-skill.sh
  ```

---

### Opsi B: Instalasi Manual (Copy Folder)
Jika ingin menyalin sendiri foldernya:

1. **Untuk Berlaku di Seluruh Antigravity (Global)**:
   Salin folder `opensid-theme-developer` ke:
   ```text
   Windows : C:\Users\<Nama_User>\.gemini\config\skills\opensid-theme-developer\
   Linux   : ~/.gemini/config/skills/opensid-theme-developer/
   ```

2. **Untuk Berlaku pada Satu Project/Workspace Tertentu**:
   Salin folder `opensid-theme-developer` ke dalam folder proyek Anda di:
   ```text
   <folder_project>/.agents/skills/opensid-theme-developer/
   ```

---

### Opsi C: Dari Berkas Arsip ZIP
Jika Anda mengunduh berkas `opensid-theme-developer.zip`:
1. Ekstrak berkas `opensid-theme-developer.zip`.
2. Tempatkan folder hasil ekstrak ke salah satu direktori target pada **Opsi B** di atas.

---

## 3. Cara Menggunakan Skill di Antigravity

Setelah terpasang, Antigravity akan secara otomatis mengenali skill ini ketika Anda berinteraksi seputar tema OpenSID.

### Contoh Prompt / Perintah Siap Pakai:

#### 1. Memeriksa Informasi Rilis OpenSID
> *"Antigravity, tolong periksa versi rilis OpenSID Free terbaru dari GitHub resmi dan periksa apakah ada perubahan arsitektur tema."*

#### 2. Merancang Tema Baru Secara Interaktif (Fitur 4)
> *"Saya ingin merancang tema baru untuk website desa. Tolong lakukan wawancara bertahap untuk menggali kebutuhan desain, warna, tata letak hero, dan struktur halamannya."*

#### 3. Membuat Kode Tema Baru (Fitur 3)
> *"Buatkan tema OpenSID baru dengan nama 'tema-desa-wisata' berbasis Laravel Blade dengan tata letak full-width dan warna dominan hijau toska."*

#### 4. Menjalankan Quality Assurance & Validasi Tema (Fitur 6)
> *"Tolong jalankan pengujian QA dan validasi linter untuk tema di folder themes_output/tema-desa-modern."*
*(AI akan menjalankan skrip `validate_theme.py` dan mengecek seluruh berkas manifes, sintaks Blade, serta namespace `theme::`).*

#### 5. Menerbitkan Kunci Lisensi & Domain Binding (Fitur 6 & 7)
> *"Terbitkan kunci lisensi untuk 'tema-desa-modern' yang terikat pada domain 'desa-sukamaju.desa.id'."*
*(AI akan menjalankan skrip `license_tool.py` dan menghasilkan token lisensi resmi beserta parameter auditnya).*

#### 6. Memperbarui Tema Katalog (Fitur 5)
> *"Perbarui tema katalog 'tema-pedesaan-klasik' agar kompatibel dengan OpenSID rilis terbaru tanpa mengubah tampilan khasnya (preserve-first)."*

---

## 4. Struktur Berkas di Dalam Paket Skill

```text
opensid-theme-developer/
├── SKILL.md                          # Instruksi Induk & Logika Pengambilan Keputusan AI
│
├── references/                       # 9 Berkas Baku Standar OpenSID
│   ├── compatibility-rules.md        # Aturan kompatibilitas & preserve-first
│   ├── licensing-architecture.md     # Arsitektur lisensi 2 lapis
│   ├── opensid-sources.md            # Sumber resmi GitHub OpenSID Free
│   ├── release-acceptance-criteria.md# Standar kriteria kelulusan rilis (Gates 1-6)
│   ├── release-change-classification.md # Klasifikasi dampak perubahan rilis
│   ├── release-information.md        # Schema data rilis
│   ├── standard-theme-architecture.md# Bedah struktur tema default (Natra & Esensi)
│   ├── theme-development-rules.md    # Aturan koding Blade & pemanggilan aset
│   └── theme-quality-standards.md    # Standar kualitas visual, kontras, dan UI/UX
│
├── workflows/                        # 20 SOP Prosedur Kerja + 6 Sub-Workflow Lisensi
│   ├── check-latest-release.md       # SOP Fitur 1
│   ├── analyze-release-history.md    # SOP Fitur 2
│   ├── create-new-theme.md           # SOP Fitur 3
│   ├── interview-theme-requirements.md # SOP Fitur 4
│   ├── manage-theme-version.md       # SOP Semantic Versioning
│   ├── update-catalog-theme.md       # SOP Fitur 5
│   ├── validate-theme.md             # SOP Fitur 6
│   ├── publish-theme-catalog-entry.md# SOP Fitur 7
│   └── license/                      # 6 SOP Lisensi (Issue, Validate, Revoke, Transfer)
│
├── knowledge/                        # Basis Pengetahuan Riwayat Rilis & Arsitektur
│   ├── releases/                     # Indeks rilis v22, v23, v24, dan matriks kompatibilitas
│   └── standard-architectures/       # Peta arsitektur standar per versi OpenSID
│
├── catalog/                          # Katalog Produk Tema
│   ├── catalog-index.md              # Daftar seluruh tema terdaftar
│   └── products/                     # Dokumentasi produk per tema
│
├── templates/                        # 10 Template Dokumen Resmi
│   ├── theme-specification.md        # Template spesifikasi kebutuhan tema
│   ├── design-tokens.md              # Template token warna, font, dan spacing
│   ├── version-history.md            # Template catatan rilis changelog
│   ├── compatibility-report.md       # Template laporan kompatibilitas
│   ├── theme-test-report.md          # Template laporan hasil pengujian
│   ├── theme-quality-report.md       # Template laporan skor mutu visual
│   ├── theme-release-approval.md     # Template sertifikat persetujuan rilis
│   ├── catalog-product-page.md       # Template halaman produk katalog
│   ├── publication-checklist.md      # Template checklist pra-publikasi
│   └── release-manifest.md           # Template manifest rilis JSON
│
└── scripts/                          # Kakas Otomasi Operasional Python & PowerShell
    ├── fetch_opensid_info.py         # Skrip pengambil data rilis GitHub OpenSID
    ├── theme_manager.py              # Skrip pembuat struktur tema & pengemas ZIP
    ├── validate_theme.py             # Skrip linter & QA kelayakan rilis tema
    └── license_tool.py               # Skrip penerbit & validator lisensi 2 lapis
```

---

## 5. Dukungan & Pembaruan
Skill ini dikembangkan untuk komunitas desa Indonesia dan ekosistem OpenSID.
- **Repository Resmi**: [https://github.com/rajawali-g/skill-opensid](https://github.com/rajawali-g/skill-opensid)
- **Lisensi**: Open Source (GPL-3.0 / MIT Compliant)
