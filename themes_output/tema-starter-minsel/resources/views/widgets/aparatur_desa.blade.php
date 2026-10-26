<h3 class="text-base font-bold text-gray-900 mb-4 border-b pb-2"><?= $judul_widget ?? 'Aparatur Desa'; ?></h3>
<div class="text-center">
    <img src="<?= gambar_pamong($desa['foto_kepala_desa']); ?>" alt="Kepala Desa" class="w-24 h-24 object-cover rounded-full mx-auto mb-3 shadow border-2 border-blue-500">
    <h4 class="font-bold text-gray-800 text-sm"><?= $desa['nama_kepala_desa']; ?></h4>
    <p class="text-xs text-gray-500">Kepala Desa <?= $desa['nama_desa']; ?></p>
</div>
