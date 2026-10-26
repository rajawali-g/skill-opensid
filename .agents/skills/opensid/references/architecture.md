# Arsitektur & Struktur Folder OpenSID

OpenSID menggunakan arsitektur modern berbasis komponen Laravel (pada rilis 24.x ke atas) yang diintegrasikan dengan fondasi CodeIgniter untuk menjaga kompatibilitas fitur-fitur desa yang telah matang.

---

## 1. Peta Direktori Utama

```text
opensid/
├── app/                        # Core Application (Laravel Services, Enums, Casts, Console)
├── Modules/                    # Modul-modul fitur mandiri (Analisis, Kehadiran, Lapak, dll)
├── donjo-app/                  # Core sistem warisan (Controllers, Models, Views Legacy)
├── desa/                       # WILAYAH KUSTOMISASI DESA (Jangan ditimpa saat update!)
│   ├── config/                 # Konfigurasi spesifik desa (database, mail, sensus)
│   ├── themes/                 # Tema publik kustom milik desa
│   ├── surat/                  # Template surat ODT/RTF kustom
│   └── upload/                 # Berkas unggahan (foto penduduk, dokumen surat, galeri)
├── themes/                     # Tema publik bawaan sistem (Natra, Esensi)
├── public/                     # Document root web (index.php, assets, storage link)
└── vendor/                     # Dependensi Composer (Laravel & library pihak ketiga)
```

---

## 2. Aturan Kustomisasi Desa (`desa/`)

Folder `desa/` dirancang agar pengelola desa dapat melakukan modifikasi tanpa khawatir hilang saat melakukan pembaruan kode inti OpenSID.

### Override Hierarki:
1. **Konfigurasi Database**:
   Sistem akan membaca `desa/config/database.php` terlebih dahulu sebelum membaca konfigurasi default.
2. **Template Surat**:
   Jika terdapat file template surat di `desa/surat/<kode_surat>/`, sistem akan memprioritaskan template tersebut dibandingkan template bawaan di `donjo-app/views/surat/`.
3. **Tema Web Desa**:
   Tema yang diletakkan di `desa/themes/<nama_tema>/` akan otomatis terdeteksi pada menu **Admin > Pengaturan Web > Tema**.

---

## 3. Komponen Inti Modern (Laravel Components)

- **Enums (`app/Enums/`)**:
  Mendefinisikan tipe data statis desa (contoh: `AgamaEnum`, `CacatEnum`, `CaraKBEnum`, `DerajatSuratEnum`, `StatusDasarEnum`).
- **Casts (`app/Casts/`)**:
  Menangani konversi data otomatis pada model Eloquent (contoh: `Sebutan`, `Path`, `Zoom`).
- **Modular routing (`Modules/*/Routes/`)**:
  Setiap modul memiliki isolasi rute sendiri untuk web dan API.
