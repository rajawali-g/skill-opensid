# OpenSID Release Information Schema

Schema informasi yang harus dikumpulkan saat melakukan Release Discovery (Fitur 1).

## Format Data Rilis
Setiap rilis yang terverifikasi dicatat dengan atribut:
- `tag_name`: String (contoh: `v2408.0.0`)
- `published_at`: ISO 8601 Timestamp
- `is_prerelease`: Boolean
- `target_commitish`: Branch atau commit SHA
- `requirements`:
  - `php_min`: Versi minimum PHP (misal PHP 8.1 / 8.2)
  - `php_extensions`: List ekstensi yang wajib (intl, mbstring, curl, gd, mysqli/pdo_mysql, zip, bcmath)
  - `database`: MariaDB / MySQL version
  - `web_server`: Apache 2.4+ / Nginx
- `theme_engine`: Laravel Blade (`theme::` namespace)
- `release_notes_url`: URL release notes GitHub
- `verification_status`: `verified` | `partially_verified` | `unverified`
