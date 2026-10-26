# Theme Development Rules

Aturan baku pengembangan tema OpenSID:

1. **Gunakan Namespace `theme::`**: Semua `@include` wajib menggunakan prefix `theme::`.
2. **Panggilan Aset Mandiri**: Gunakan helper `asset()` atau helper URL OpenSID `base_url("themes/{nama_tema}/assets/...")`.
3. **Dukungan Widget Dinamis**: Wajib memuat widget dengan syntax:
   `@includeIf("theme::widgets.{$widget['isi']}", $judul_widget)`
4. **Sanitasi Output**: Jangan gunakan `{!! $var !!}` tanpa sanitasi untuk data publik pengguna. Gunakan `{{ $var }}` default Blade.
5. **Responsif & Ringan**: Desain wajib mobile-first, zero horizontal overflow, dan tidak bergantung pada CDN eksternal berat tanpa fallback.
