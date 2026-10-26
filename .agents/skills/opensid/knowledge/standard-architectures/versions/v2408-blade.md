# Arsitektur Tema OpenSID v2408.0.0+ (Blade Engine)

Arsitektur standar yang berlaku untuk rilis OpenSID modern:
- Engine: Laravel Blade
- Namespace: `theme::`
- Mandatory Files:
  - `template.blade.php`: Controller entry view
  - `config.json`: Skema pengaturan tema di Admin Web
  - `composer.json`: Type definition
  - `catatan_rilis.md`: Changelog tema
  - `index.html`: Directory protection
- Partials Structure:
  - `commons/`: header, footer, meta, navbar
  - `layouts/`: index (wrapper utama)
  - `partials/`: komponen artikel, slider, pagination
  - `widgets/`: template widget dinamis
