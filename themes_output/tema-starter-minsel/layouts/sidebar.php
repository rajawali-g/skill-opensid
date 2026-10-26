<div class="widget-box bg-white p-6 rounded-xl shadow-sm border border-gray-100 text-center">
    <h3 class="text-base font-bold text-gray-900 mb-4 border-b pb-2 text-left">Kepala Desa</h3>
    <img src="<?= gambar_pamong($desa['foto_kepala_desa']); ?>" alt="Kepala Desa" class="w-28 h-28 object-cover rounded-full mx-auto mb-3 shadow">
    <h4 class="font-bold text-gray-800"><?= $desa['nama_kepala_desa']; ?></h4>
    <p class="text-xs text-gray-500">Kepala Desa <?= $desa['nama_desa']; ?></p>
</div>
