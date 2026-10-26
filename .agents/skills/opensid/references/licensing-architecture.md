# 2-Layer Licensing Architecture

Sistem perlindungan dan lisensi tema OpenSID:

## Lapis 1: Integrasi Tema (Client-side / Template Component)
- Tema memiliki identifier unik produk (`product_id`, `version`).
- Memiliki handler status lisensi yang anggun (graceful).
- Jika lisensi belum aktif / invalid, tampilkan notice aktivasi di admin atau banner yang informatif.
- **DILARANG MERUSAK SITUS PENGGUNA**: Jangan membuat layout crash atau loop freeze.

## Lapis 2: License Server & Database API
- Endpoint server lisensi memvalidasi token hak penggunaan.
- Database mencatat:
  - `product_id`
  - `license_key`
  - `domain_bound` (URL/domain instalasi OpenSID)
  - `status` (`active`, `expired`, `revoked`, `suspended`)
  - `activated_at` & `audit_logs`
- Kunci terikat per domain/instalasi resmi.
- Mendukung mekanisme transfer domain resmi (re-binding) dengan otorisasi.
