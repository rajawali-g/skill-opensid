<h3 class="text-base font-bold text-slate-900 mb-4 border-b pb-2"><?= $judul_widget ?? 'Aparatur Desa'; ?></h3>
<div class="flex items-center space-x-4">
    <img src="<?= gambar_pamong($desa['foto_kepala_desa']); ?>" alt="Kepala Desa" class="w-16 h-16 rounded-full object-cover border-2 border-blue-600 shadow">
    <div>
        <h4 class="font-bold text-slate-900 text-sm"><?= $desa['nama_kepala_desa']; ?></h4>
        <span class="text-xs bg-blue-50 text-blue-700 px-2 py-0.5 rounded font-medium">Kepala Desa</span>
        <p class="text-xs text-slate-400 mt-1">Periode Aktif</p>
    </div>
</div>
