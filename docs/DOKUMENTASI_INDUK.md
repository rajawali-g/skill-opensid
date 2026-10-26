# DOKUMENTASI INDUK
# OPENSID THEME DEVELOPER
## AI Skill untuk Analisis Versi, Pengembangan Tema, Quality Assurance, Lisensi, dan Publikasi Katalog

**Versi dokumen:** 1.0  
**Status:** Rancangan arsitektur dan spesifikasi fungsional  
**Target aplikasi:** OpenSID Free/non-Premium  
**Jenis sistem:** AI Skill mandiri lintas AI agent  
**Cakupan:** Fitur 1–7

---

# BAB I. PENDAHULUAN

## 1.1 Latar Belakang
Pengembangan tema OpenSID membutuhkan pemahaman terhadap versi aplikasi, arsitektur tema standar, kontrak template, helper, route, dependensi frontend, serta perubahan kode dari satu versi ke versi berikutnya.

Tema yang terlihat menarik belum tentu kompatibel dengan versi OpenSID yang digunakan. Sebaliknya, tema yang secara teknis dapat dijalankan belum tentu memenuhi standar responsivitas, kualitas visual, aksesibilitas, dan kelayakan distribusi.

OpenSID Theme Developer dirancang sebagai AI Skill yang mendukung seluruh siklus hidup tema, mulai dari identifikasi rilis OpenSID, pembelajaran riwayat perubahan, pengembangan tema, pengelolaan versi, pengujian, penerapan lisensi, hingga publikasi produk dalam katalog.

Sistem ini juga menyediakan alur pengembangan bagi tema yang sudah tersedia dalam katalog, termasuk tema yang masih beta, belum dipublikasikan, atau sedang dalam pengujian.

## 1.2 Tujuan
1. Mengidentifikasi rilis OpenSID Free terbaru berdasarkan sumber yang dapat diverifikasi.
2. Mengumpulkan dan menganalisis riwayat perubahan OpenSID secara berkelanjutan.
3. Mempelajari arsitektur tema standar untuk setiap versi OpenSID.
4. Membuat tema baru atau mengembangkan tema yang telah tersedia.
5. Menggali kebutuhan desain tema melalui percakapan interaktif dengan pengguna.
6. Mengelola versi tema secara sistematis dan otomatis.
7. Memperbarui kompatibilitas tema katalog terhadap versi OpenSID target.
8. Memeriksa kualitas teknis dan visual sebelum tema dipublikasikan.
9. Mengelola lisensi penggunaan tema melalui sistem validasi berlapis.
10. Mempublikasikan tema yang telah memenuhi persyaratan rilis ke katalog produk.

## 1.3 Prinsip Dasar
### A. Berorientasi pada OpenSID Free/non-Premium
Seluruh analisis dan pengembangan harus mengacu pada distribusi OpenSID Free/non-Premium. Fitur, kode, atau mekanisme khusus Premium tidak boleh diasumsikan tersedia pada distribusi Free.

### B. Berbasis bukti
Informasi mengenai versi, struktur direktori, helper, route, template, dependensi, dan persyaratan sistem harus didukung oleh dokumentasi resmi atau pemeriksaan kode sumber yang relevan.

### C. Memperhatikan versi
Setiap pengembangan harus memiliki target versi OpenSID yang jelas. Arsitektur tema pada satu versi tidak boleh otomatis dianggap sama dengan arsitektur versi lainnya.

### D. Mempertahankan fungsi yang ada
Pengembangan tema katalog harus mengutamakan pemeliharaan fungsi yang masih valid. Penghapusan atau perubahan perilaku harus berdasarkan kebutuhan yang jelas.

### E. Memisahkan pengembangan dan publikasi
Tema yang selesai dibuat tidak otomatis siap dipublikasikan. Tema harus melalui pemeriksaan teknis, visual, kompatibilitas, dokumentasi, dan persetujuan rilis.

### F. Lisensi yang dapat diverifikasi
Status lisensi harus diperiksa oleh layanan yang berwenang. Kegagalan validasi tidak boleh ditutupi dengan menganggap lisensi valid.

### G. Portabilitas AI Skill
Struktur skill harus dapat diadaptasi untuk berbagai AI agent yang mendukung instruksi, referensi, workflow, dan akses terhadap berkas proyek.

---

# BAB II. ARSITEKTUR UMUM

## 2.1 Gambaran Sistem
OpenSID Theme Developer memiliki tujuh fitur utama:
1. Release Discovery.
2. Release History & Standard Theme Architecture Analyzer.
3. Theme Builder.
4. Interactive Theme Designer & Automatic Versioning.
5. Catalog Theme Updater & Enhancement.
6. Theme Quality Assurance, Release Certification & Licensing.
7. Theme Catalog Publishing & Licensed Distribution.

Ketujuh fitur berbagi pengetahuan, tetapi memiliki tanggung jawab yang berbeda.

## 2.2 Hubungan Antarfitur
Alur utamanya:
**Fitur 1 → Fitur 2 → Fitur 3/4/5 → Fitur 6 → Fitur 7**

---

# BAB III. FITUR 1 — RELEASE DISCOVERY
Mengidentifikasi rilis OpenSID Free/non-Premium terbaru berdasarkan sumber GitHub resmi (Releases, Tags, branch umum).

---

# BAB IV. FITUR 2 — RELEASE HISTORY & STANDARD THEME ARCHITECTURE ANALYZER
Membangun basis pengetahuan teknis historis OpenSID dan mempelajari arsitektur tema standar sesuai versi.

---

# BAB V. FITUR 3 — THEME BUILDER
Membuat tema baru atau mengembangkan tema katalog sesuai arsitektur OpenSID target.

---

# BAB VI. FITUR 4 — INTERACTIVE THEME DESIGNER & AUTOMATIC VERSIONING
Wawancara bertahap kebutuhan desain tema baru, perancangan spesifikasi, design tokens, dan versioning semantik (MAJOR.MINOR.PATCH).

---

# BAB VII. FITUR 5 — CATALOG THEME UPDATER & ENHANCEMENT
Memperbarui kompatibilitas dan mengembangkan tema yang sudah terdaftar dalam katalog dengan prinsip preserve-first.

---

# BAB VIII. FITUR 6 — THEME QUALITY ASSURANCE, RELEASE CERTIFICATION & LICENSING
Pengujian teknis, evaluasi visual, persetujuan kelayakan rilis, dan validasi lisensi dua lapis (tema + server lisensi).

---

# BAB IX. FITUR 7 — THEME CATALOG PUBLISHING & LICENSED DISTRIBUTION
Publikasi produk ke katalog, persiapan paket rilis, checksum, dan alur aktivasi lisensi.

---

# BAB X. STRUKTUR DIREKTORI SKILL
Mengintegrasikan seluruh referensi teknis, workflow operasional, templates, dan katalog tema.
