# Workflow: Revoke License (Fitur 6 & 7)

Prosedur pencabutan lisensi:

1. Admin server memeriksa pelanggaran ketentuan penggunaan atau refund.
2. Ubah status kunci menjadi `revoked` di database license server.
3. Saat validasi berikutnya, klien tema menerima status pencabutan dan menampilkan pemberitahuan aktivasi ulang.
