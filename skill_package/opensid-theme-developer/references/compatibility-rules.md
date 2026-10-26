# Compatibility Rules

Aturan pemeliharaan kompatibilitas tema:

1. **Prinsip Preserve-First**: Jangan menghapus fitur yang sudah ada pada tema katalog saat upgrade.
2. **Fallback Handling**: Pastikan variabel yang mungkin tidak dikirimkan controller memiliki fallback (contoh: `$desa['nama_desa'] ?? 'Nama Desa'`).
3. **Kompatibilitas Versi PHP**: Sintaks tema harus kompatibel dengan versi PHP target OpenSID (PHP 8.1 - 8.3). Hindari fungsi deprecated.
4. **Isolasi Modul**: Jangan mengubah file core OpenSID. Semua modifikasi harus berada di dalam folder tema.
