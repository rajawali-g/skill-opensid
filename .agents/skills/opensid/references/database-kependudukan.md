# Kamus Data Database Kependudukan OpenSID

Database OpenSID menggunakan MySQL / MariaDB dengan engine InnoDB dan collation `utf8mb4_unicode_ci`.

---

## 1. Tabel Utama Kependudukan

### `tweb_penduduk` (Master Data Penduduk)
Tabel induk seluruh warga desa yang terdaftar:
- `id` (int, PK): ID unik penduduk.
- `nik` (varchar(16)): Nomor Induk Kependudukan (Unique).
- `nama` (varchar(100)): Nama lengkap sesuai KTP.
- `id_kk` (int): Foreign key ke tabel `tweb_keluarga`.
- `kk_level` (int): Hubungan dalam keluarga (1=Kepala Keluarga, 2=Suami, 3=Istri, 4=Anak, dst).
- `sex` (tinyint): Jenis kelamin (1=Laki-laki, 2=Perempuan).
- `tempatlahir` (varchar(100)): Tempat lahir.
- `tanggallahir` (date): Tanggal lahir.
- `agama_id` (int): Relasi ke tabel `tweb_penduduk_agama`.
- `status_kawin` (int): Status perkawinan (1=Belum Kawin, 2=Kawin, 3=Cerai Hidup, 4=Cerai Mati).
- `pekerjaan_id` (int): Relasi ke tabel `tweb_penduduk_pekerjaan`.
- `status_dasar` (tinyint): Status hidup penduduk (1=Hidup, 2=Mati, 3=Pindah, 4=Hilang, 5=Pergi).
- `id_cluster` (int): Relasi ke tabel `tweb_wil_clusterdesa` (Wilayah RT/RW/Dusun).

### `tweb_keluarga` (Master Data Kartu Keluarga)
- `id` (int, PK): ID keluarga.
- `no_kk` (varchar(16)): Nomor Kartu Keluarga.
- `nik_kepala` (int): ID penduduk kepala keluarga.
- `tgl_cetak_kk` (date): Tanggal pencetakan KK.
- `alamat` (varchar(200)): Alamat tempat tinggal keluarga.

### `tweb_wil_clusterdesa` (Struktur Wilayah Dusun, RW, RT)
- `id` (int, PK): ID wilayah.
- `dusun` (varchar(50)): Nama Dusun / Lingkungan.
- `rw` (varchar(10)): Nomor RW.
- `rt` (varchar(10)): Nomor RT.

---

## 2. Tabel Layanan Surat & Log

### `log_surat`
Menyimpan riwayat seluruh surat yang diterbitkan:
- `id` (int, PK)
- `id_format_surat` (int): Relasi ke jenis surat.
- `id_penduduk` (int): Pemohon surat.
- `id_pamong` (int): Aparatur desa yang menandatangani.
- `no_surat` (varchar(100)): Nomor surat yang dicetak.
- `tanggal` (timestamp): Waktu penerbitan.
- `keterangan` (text): Keterangan / keperluan surat.
- `lampiran` (varchar(255)): Berkas lampiran jika ada.

### `config` (Identitas & Pengaturan Desa)
Berisi profil desa: nama desa, kode desa (Kemendagri), kode pos, nama kepala desa, logo desa, koordinat kantor desa, dan batas wilayah.
