# Panduan Kustomisasi Tema Publik & Folder Output Tema (`themes_output/`)

OpenSID memiliki portal web publik yang diakses oleh warga masyarakat untuk membaca berita desa, melihat transparansi APBDes, statistik kependudukan, produk UMKM/Lapak Desa, dan layanan mandiri.

---

## 1. Standar Folder Output Tema (`themes_output/`)

Untuk menjaga kerapian proyek dan mempermudah distribusi tema kepada pengelola desa, seluruh proses pembuatan tema diarahkan ke folder khusus:

```text
d:\project_opensid\themes_output/
├── <nama_tema>/                  # Folder sumber kode tema lengkap
│   ├── assets/
│   │   ├── css/theme.css
│   │   ├── js/theme.js
│   │   └── images/
│   ├── layouts/
│   │   ├── header.php
│   │   ├── footer.php
│   │   └── sidebar.php
│   ├── partials/
│   │   ├── artikel.php
│   │   ├── apbdes.php
│   │   └── peta.php
│   ├── template.php              # Berkas master template OpenSID
│   └── theme.json                # Manifes identitas tema
└── <nama_tema>.zip               # Paket distribusi ZIP (siap diunggah ke OpenSID)
```

---

## 2. Otomasi Generator & Packager Tema (`manage-theme.ps1`)

Tersedia skrip otomatisasi di root workspace untuk mempermudah alur kerja:

### A. Membuat Kerangka Tema Baru
```powershell
.\manage-theme.ps1 new -Name "minsel-modern" -Title "Tema Minsel Modern" -Author "Diskominfo"
```
Skrip akan membuat seluruh struktur folder dan berkas starter tema di `themes_output/minsel-modern/`.

### B. Mengemas Menjadi Berkas ZIP Siap Unggah
```powershell
.\manage-theme.ps1 package -Name "minsel-modern"
```
Menghasilkan berkas `themes_output/minsel-modern.zip` yang terkompresi dengan struktur hirarki standar OpenSID.

### C. Mengunggah ke OpenSID
1. Buka Web Admin OpenSID.
2. Masuk ke menu **Pengaturan Web > Tema**.
3. Klik tombol **Unggah Tema** (Upload Theme).
4. Pilih berkas ZIP dari `themes_output/<nama_tema>.zip`.
5. Aktifkan tema tersebut.

### D. Sinkronisasi Langsung ke Instalasi Lokal (Opsional)
Jika Anda mengembangkan di lingkungan web server lokal (Laragon/XAMPP):
```powershell
.\manage-theme.ps1 deploy -Name "minsel-modern" -Target "D:\laragon\www\opensid"
```
Tema langsung disalin ke folder `desa/themes/minsel-modern/` pada instalasi OpenSID Anda.

---

## 3. Komponen Utama Tampilan Tema

### a. Widget APBDes (Transparansi Keuangan)
OpenSID menyediakan data transparansi anggaran pendapatan dan belanja desa:
```php
<span class="pendapatan">Rp <?= number_format($transparansi['pendapatan'], 0, ',', '.'); ?></span>
<span class="belanja">Rp <?= number_format($transparansi['belanja'], 0, ',', '.'); ?></span>
```

### b. Peta WebGIS Desa (Leaflet.js)
OpenSID menyediakan endpoint geojson untuk batas desa, dusun, RW/RT, serta sarana/prasarana:
```javascript
// Memuat layer batas wilayah desa
fetch('/api/geojson/desa')
    .then(res => res.json())
    .then(data => {
        L.geoJSON(data, {
            style: { color: '#2563eb', weight: 2, fillOpacity: 0.1 }
        }).addTo(map);
    });
```

### c. Layanan Mandiri Warga
Tautan ke portal layanan mandiri (`/layanan-mandiri`) untuk mengecek status administrasi, bantuan sosial (BLT, PKH, BPNT), dan permohonan surat online.
