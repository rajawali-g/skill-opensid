# Workflow: Validate License (Fitur 6 & 7)

Prosedur validasi lisensi:

1. Klien tema mengirimkan handshake terenkripsi ke license server (Domain + Product ID + License Key).
2. Server memvalidasi kecocokan kunci dan status hak penggunaan.
3. Server mengembalikan status `valid` beserta token cache sementara (TTL 24-72 jam).
4. Jika server unreachable, gunakan grace period cache status validasi.
