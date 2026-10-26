# Workflow: Create New Theme (Fitur 3)

Prosedur pembuatan tema baru:

1. Tentukan target versi OpenSID dan identitas tema (nama, slug, deskripsi).
2. Buat struktur direktori tema sesuai standar di `themes_output/<nama_tema>/`.
3. Buat manifest tema: `config.json`, `composer.json`, `catatan_rilis.md`, `index.html`.
4. Implementasikan resources Blade:
   - `commons/` (`header`, `footer`, `meta`, `navbar`)
   - `layouts/` (`index`)
   - `partials/` (`artikel`, `slider`, `pagination`)
   - `widgets/` (widget dinamis OpenSID)
   - `template.blade.php`
5. Buat stylesheet dan aset mandiri di `assets/`.
6. Kemas tema ke dalam ZIP dengan nama `<nama_tema>.zip`.
7. Catat tema di katalog.
