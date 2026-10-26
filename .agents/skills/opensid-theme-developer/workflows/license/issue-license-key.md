# Workflow: Issue License Key (Fitur 7)

Prosedur penerbitan kunci lisensi:

1. Terima identitas pemesan/desa dan nomor transaksi.
2. Generate token kunci unik (kombinasi SHA-256 + cryptographic random string).
3. Simpan record di database server lisensi:
   `product_id`, `license_key_hash`, `order_ref`, `status: issued`.
4. Kirimkan lisensi kepada pengguna beserta petunjuk aktivasi.
