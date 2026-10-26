# Contoh Praktis Modul OpenSID

Contoh pembuatan modul sederhana: **Buku Tamu Digital Desa** (`Modules/BukuTamu/`).

### 1. `module.json`
```json
{
    "name": "BukuTamu",
    "alias": "buku-tamu",
    "description": "Modul registrasi pengunjung dan tamu kantor desa",
    "version": "1.0.0"
}
```

### 2. Controller `Http/Controllers/BukuTamuController.php`
```php
<?php

namespace Modules\BukuTamu\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Modules\BukuTamu\Models\BukuTamu;

class BukuTamuController extends Controller
{
    public function index()
    {
        $daftarTamu = BukuTamu::latest()->paginate(15);
        return view('bukutamu::index', compact('daftarTamu'));
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'nama_tamu' => 'required|string|max:100',
            'asal_instansi' => 'nullable|string|max:100',
            'tujuan' => 'required|string|max:255',
            'no_hp' => 'nullable|string|max:20',
        ]);

        BukuTamu::create($validated);

        return redirect()->back()->with('success', 'Buku tamu berhasil dicatat.');
    }
}
```

### 3. Route `Routes/web.php`
```php
<?php

use Illuminate\Support\Facades\Route;
use Modules\BukuTamu\Http\Controllers\BukuTamuController;

Route::prefix('buku-tamu')->middleware(['web', 'auth'])->group(function () {
    Route::get('/', [BukuTamuController::class, 'index'])->name('bukutamu.index');
    Route::post('/', [BukuTamuController::class, 'store'])->name('bukutamu.store');
});
```
