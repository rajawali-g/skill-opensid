# Kamus Variabel Template Layanan Surat & TTE

OpenSID menggunakan template berformat **ODT (OpenDocument Text / LibreOffice)** dan RTF untuk menghasilkan dokumen surat kependudukan resmi desa.

---

## 1. Format Penulisan Kode Isian

Dalam file template ODT, gunakan format variabel yang diapit kurung siku `[nama_variabel]`.
Saat surat dicetak, OpenSID secara otomatis mengganti kode tersebut dengan data penduduk dari database.

---

## 2. Kamus Kode Isian Utama

### Data Pemohon / Penduduk:
| Kode Variabel | Keterangan |
| :--- | :--- |
| `[nama]` | Nama lengkap penduduk pemohon |
| `[nik]` | Nomor Induk Kependudukan (16 digit) |
| `[no_kk]` | Nomor Kartu Keluarga |
| `[tempatlahir]` | Tempat lahir penduduk |
| `[tanggallahir]` | Tanggal lahir format Indonesia (contoh: 17 Agustus 1995) |
| `[usia]` | Usia dalam tahun |
| `[sex]` | Jenis kelamin (Laki-laki / Perempuan) |
| `[agama]` | Agama pemohon |
| `[warga_negara]` | Kewarganegaraan (WNI / WNA) |
| `[status]` | Status perkawinan (Kawin / Belum Kawin / Cerai Hidup / Cerai Mati) |
| `[pekerjaan]` | Jenis pekerjaan penduduk |
| `[pendidikan]` | Pendidikan terakhir |
| `[alamat]` | Alamat domisili lengkap (Jalan / Gang / No Rumah) |
| `[dusun]` | Nama dusun / lingkungan |
| `[rt]` | Nomor RT |
| `[rw]` | Nomor RW |

### Data Pemerintah Desa:
| Kode Variabel | Keterangan |
| :--- | :--- |
| `[nama_desa]` | Nama desa / kelurahan |
| `[nama_kecamatan]` | Nama kecamatan |
| `[nama_kabupaten]` | Nama kabupaten / kota |
| `[nama_provinsi]` | Nama provinsi |
| `[kode_pos]` | Kode pos wilayah desa |
| `[alamat_kantor]` | Alamat kantor desa |
| `[email_desa]` | Alamat email resmi desa |
| `[website_desa]` | Alamat website desa |

### Data Penandatangan & Surat:
| Kode Variabel | Keterangan |
| :--- | :--- |
| `[nomor_surat]` | Nomor register surat keluar otomatis |
| `[format_nomor_surat]` | Format penomoran lengkap sesuai klasifikasi |
| `[tgl_surat]` | Tanggal penerbitan surat |
| `[jabatan_penandatangan]` | Jabatan (Kepala Desa / Sekretaris Desa / a.n. Kades) |
| `[nama_penandatangan]` | Nama lengkap pejabat penandatangan |
| `[nip_penandatangan]` | NIP pejabat (jika ASN) |

### Variabel Pasangan / Orang Tua (Jika Diperlukan):
| Kode Variabel | Keterangan |
| :--- | :--- |
| `[nama_ayah]` | Nama ayah kandung |
| `[nik_ayah]` | NIK ayah kandung |
| `[nama_ibu]` | Nama ibu kandung |
| `[nik_ibu]` | NIK ibu kandung |
| `[nama_pasangan]` | Nama suami / istri |

---

## 3. Integrasi Tanda Tangan Elektronik (TTE)

OpenSID mendukung integrasi TTE (BSrE - BSSN / e-Sign Cloud):
1. Pejabat desa menandatangani berkas PDF hasil konversi ODT menggunakan sertifikat elektronik.
2. Template menyisipkan QR Code verifikasi dokumen melalui variabel `[qrcode]`.
3. Validitas dokumen dapat dipindai langsung oleh pihak ketiga via portal verifikasi berkas desa.
