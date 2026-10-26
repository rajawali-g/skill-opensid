# Panduan Kustomisasi Tema Publik & Tampilan Web Desa

OpenSID memiliki portal web publik yang diakses oleh warga masyarakat untuk membaca berita desa, melihat transparansi APBDes, statistik kependudukan, produk UMKM/Lapak Desa, dan layanan mandiri.

---

## 1. Struktur Tema Web Desa

Tema diletakkan di dalam folder `desa/themes/<nama_tema>/`:

```text
desa/themes/minsel-modern/
├── assets/
│   ├── css/
│   │   └── custom.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── layouts/
│   ├── header.php (atau header.blade.php)
│   ├── footer.php
│   └── sidebar.php
├── partials/
│   ├── artikel.php
│   ├── aparatur_desa.php
│   ├── apbdes.php
│   └── peta_wilayah.php
├── template.php
└── theme.json
```

---

## 2. File Konfigurasi `theme.json`

Setiap tema harus memiliki metadata di `theme.json`:

```json
{
    "name": "Minsel Modern Theme",
    "version": "1.0.0",
    "author": "Diskominfo / Komunitas Desa",
    "description": "Tema modern responsif dengan integrasi peta WebGIS desa dan widget APBDes",
    "parent": "natra",
    "screenshots": "assets/images/screenshot.png"
}
```

---

## 3. Komponen Penting Web Desa

### a. Widget APBDes (Transparansi Keuangan)
Gunakan helper OpenSID untuk merender ringkasan APBDes:
- Pendapatan Desa
- Belanja Desa
- Pembiayaan Desa

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

### c. Widget Layanan Mandiri
Tautan login warga desa ke portal layanan mandiri (`/layanan-mandiri`) untuk mengecek bantuan sosial, status KK, dan permohonan surat online.
