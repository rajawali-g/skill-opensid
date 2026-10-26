# Workflow: Check Latest Release (Fitur 1)

Prosedur verifikasi rilis terbaru OpenSID Free:

1. **Jalankan Script Fetcher**:
   Jalankan `python scripts/fetch_opensid_info.py` atau periksa langsung API GitHub `https://api.github.com/repos/OpenSID/OpenSID/releases`.
2. **Filter Rilis Komunitas**:
   Pastikan rilis berasal dari branch `umum` atau rilis Free publik.
3. **Catat Rincian**:
   Simpan versi, tag, tanggal rilis, dan URL rilis ke `data/opensid_latest_info.json`.
4. **Verifikasi Kebutuhan Sistem**:
   Catat versi minimum PHP yang dipersyaratkan.
5. **Keluaran**:
   Informasi rilis mutakhir yang terverifikasi untuk digunakan oleh Fitur 2 dan 3.
