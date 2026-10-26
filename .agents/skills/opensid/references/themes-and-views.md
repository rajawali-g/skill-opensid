# Panduan Kustomisasi Tema Publik & Katalog 3 Tema Dasar OpenSID

OpenSID memiliki portal web publik yang diakses oleh warga masyarakat untuk membaca berita desa, melihat transparansi APBDes, statistik kependudukan, produk UMKM/Lapak Desa, dan layanan mandiri.

---

## 🎨 1. Tiga Tema Dasar Siap Pakai di `themes_output/`

Repositori ini menyediakan **3 tema dasar resmi** dengan karakter desain yang berbeda untuk disesuaikan dengan kebutuhan dan profil desa:

| Nama Tema | Slug / Folder | Konsep Desain | Karakteristik Utama |
| :--- | :--- | :--- | :--- |
| **Pedesaan Klasik** | `tema-pedesaan-klasik` | Kearifan Lokal & Agraris | Palet hangat (*warm earth*, hijau daun `#15803d`, kayu `#78350f`), salam santun kepala desa, ornamen klasik, bersahabat untuk warga lansia. |
| **Desa Modern** | `tema-desa-modern` | Pemerintahan Bersih & Elegan | Palet biru instansi (`#1e40af`, `#0284c7`), kartu berbayang lembut (*soft drop shadows*), tata kelola transparan, progres APBDes rapi. |
| **Desa Digital** | `tema-desa-digital` | *Smart Village* Futuristik | Palet cyber dark (`#090d16`), aksen neon cyan (`#06b6d4`), kartu *glassmorphism*, live counter statistik, spotlight layanan mandiri online. |

---

## 📂 2. Struktur Folder Output (`themes_output/`)

Semua tema hasil kreasi ditampung di `themes_output/`:
```text
themes_output/
├── tema-pedesaan-klasik/           # Folder sumber kode Blade tema pedesaan klasik
├── tema-pedesaan-klasik.zip        # Paket ZIP siap pasang (8.4 KB)
├── tema-desa-modern/               # Folder sumber kode Blade tema desa modern
├── tema-desa-modern.zip            # Paket ZIP siap pasang (7.7 KB)
├── tema-desa-digital/              # Folder sumber kode Blade tema desa digital
├── tema-desa-digital.zip           # Paket ZIP siap pasang (8.3 KB)
└── tema-starter-minsel/            # Tema starter bawaan
```

---

## ⚙️ 3. Perintah Cepat Pengelola Tema (`manage-theme.ps1`)

```powershell
# Melihat daftar tema yang telah dibangun
.\manage-theme.ps1 list

# Mengemas ulang salah satu tema ke ZIP
.\manage-theme.ps1 package -Name "tema-desa-digital"

# Menyinkronkan langsung ke instalasi OpenSID lokal (Laragon/XAMPP)
.\manage-theme.ps1 deploy -Name "tema-desa-digital" -Target "D:\laragon\www\opensid"
```

---

## 💻 4. Cara Memasang Tema di OpenSID Web Admin

1. Buka halaman Web Admin OpenSID Anda (contoh: `http://localhost/opensid/siteman`).
2. Buka menu navigasi: **Pengaturan Web > Tema**.
3. Klik tombol **Unggah Tema** (Upload Theme).
4. Pilih salah satu berkas arsip dari:
   - `themes_output/tema-pedesaan-klasik.zip`
   - `themes_output/tema-desa-modern.zip`
   - `themes_output/tema-desa-digital.zip`
5. Klik **Unggah**, lalu klik **Aktifkan** pada tema yang baru dipasang.
