# Panduan Pemembangan Modul OpenSID

OpenSID menggunakan arsitektur modular (`nwidart/laravel-modules` compatible). Modul memungkinkan penambahan fitur baru seperti Layanan Khusus, Integrasi Sensor IoT, Buku Tamu, Antrean Desa, atau E-Commerce Lapak Desa secara terisolasi.

---

## 1. Struktur Standar Sebuah Modul

Setiap modul ditempatkan di dalam folder `Modules/<NamaModul>/`:

```text
Modules/AspirasiWarga/
├── Config/
│   └── config.php
├── Database/
│   ├── Migrations/
│   └── Seeders/
├── Http/
│   ├── Controllers/
│   │   └── AspirasiWargaController.php
│   └── Requests/
├── Models/
│   └── Aspirasi.php
├── Resources/
│   └── views/
│       ├── index.blade.php
│       └── create.blade.php
├── Routes/
│   ├── api.php
│   └── web.php
├── composer.json
└── module.json
```

---

## 2. Berkas Konfigurasi `module.json`

Setiap modul wajib memiliki `module.json` sebagai manifes identitas:

```json
{
    "name": "AspirasiWarga",
    "alias": "aspirasi-warga",
    "description": "Modul penampung aspirasi dan pengaduan masyarakat desa",
    "keywords": ["aspirasi", "pengaduan", "opensid"],
    "priority": 0,
    "providers": [
        "Modules\\AspirasiWarga\\Providers\\AspirasiWargaServiceProvider"
    ],
    "files": []
}
```

---

## 3. Rute Modul (`Routes/web.php`)

Gunakan grup rute dengan middleware autentikasi OpenSID:

```php
<?php

use Illuminate\Support\Facades\Route;
use Modules\AspirasiWarga\Http\Controllers\AspirasiWargaController;

Route::prefix('aspirasi-warga')->middleware(['web', 'auth'])->group(function () {
    Route::get('/', [AspirasiWargaController::class, 'index'])->name('aspirasi.index');
    Route::get('/create', [AspirasiWargaController::class, 'create'])->name('aspirasi.create');
    Route::post('/store', [AspirasiWargaController::class, 'store'])->name('aspirasi.store');
    Route::delete('/{id}', [AspirasiWargaController::class, 'destroy'])->name('aspirasi.destroy');
});
```

---

## 4. Model Eloquent (`Models/Aspirasi.php`)

```php
<?php

namespace Modules\AspirasiWarga\Models;

use Illuminate\Database\Eloquent\Model;

class Aspirasi extends Model
{
    protected $table = 'modul_aspirasi_warga';

    protected $fillable = [
        'id_penduduk',
        'judul',
        'kategori',
        'isi_aspirasi',
        'status', // pending, diproses, selesai, ditolak
        'tanggapan'
    ];

    // Relasi ke penduduk desa
    public function penduduk()
    {
        return $this->belongsTo(\App\Models\Penduduk::class, 'id_penduduk', 'id');
    }
}
```

---

## 5. Migrasi Database (`Database/Migrations/`)

Buat skema tabel dengan prefix `modul_` agar tidak bertabrakan dengan tabel bawaan:

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('modul_aspirasi_warga', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('id_penduduk')->nullable();
            $table->string('judul', 200);
            $table->string('kategori', 50)->default('Umum');
            $table->text('isi_aspirasi');
            $table->string('status', 20)->default('pending');
            $table->text('tanggapan')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('modul_aspirasi_warga');
    }
};
```
