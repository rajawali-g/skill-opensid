# Workflow: Validate Theme (Fitur 6)

Prosedur validasi komprehensif tema:

1. Periksa integritas file: pastikan `template.blade.php`, `config.json`, dan assets tersedia.
2. Periksa sintaks Blade: pastikan tidak ada tag unclosed atau sintaks php fatal.
3. Periksa dependensi asset lokal: tidak ada link asset yang 404.
4. Periksa integrasi widget: pastikan looping widget menggunakan `@includeIf`.
