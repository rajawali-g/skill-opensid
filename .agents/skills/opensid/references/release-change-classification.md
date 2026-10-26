# Release Change Classification

Klasifikasi dampak perubahan rilis OpenSID terhadap siklus hidup tema:

1. **Requirement Change**: Perubahan versi minimum PHP, ekstensi, web server.
2. **Architecture Change**: Perubahan direktori tema atau mekanisme pemuatan view.
3. **Template Contract Change**: Perubahan variabel bawaan controller (misal `$artikel`, `$desa`, `$menu`), helper, atau direktif Blade.
4. **Frontend Change**: Pembaruan bootstrap, fontawesome, jquery, atau penghapusan CSS/JS legacy.
5. **Feature Change**: Fitur modul baru di OpenSID (misal IDM, SDGs, APBDes, Peta GeoJSON).
6. **Breaking Change**: Perubahan yang menyebabkan error fatal jika tema lama dijalankan di OpenSID baru.
7. **Security Change**: Aturan sanitasi XSS (`e()`, htmlspecialchars) dan token CSRF.
