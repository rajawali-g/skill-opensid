# Release Acceptance Criteria & Gates

Kriteria kelulusan tema untuk masuk ke status `ready_to_publish` / `published`:

1. **Gate 1: Compatibility Pass**: 100% kompatibel dengan versi target OpenSID Free.
2. **Gate 2: Functional Test Pass**: Semua skenario halaman (beranda, artikel, galeri, peta, widget) terverifikasi.
3. **Gate 3: Visual QA Pass**: Lolos uji multi-resolusi tanpa layout breaking.
4. **Gate 4: Security & Cleanliness**: Tidak ada kredensial atau debug dump (`var_dump`, `dd()`, console.log).
5. **Gate 5: Licensing Architecture Ready**: Terintegrasi dengan sistem lisensi dua lapis.
6. **Gate 6: Package Completeness**: Memiliki ZIP valid, `catatan_rilis.md`, `config.json`, dan dokumentasi instalasi.
