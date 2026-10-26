<h3 class="card-title-klasik font-bold text-base"><?= $judul_widget ?? 'Pamong Desa'; ?></h3>
<div class="text-center">
    <img src="<?= gambar_pamong($desa['foto_kepala_desa']); ?>" alt="Kepala Desa" class="w-28 h-28 object-cover rounded-full mx-auto mb-3 shadow border-4 border-yellow-700">
    <h4 class="font-bold text-yellow-900"><?= $desa['nama_kepala_desa']; ?></h4>
    <p class="text-xs text-green-800 font-semibold">Kepala Desa <?= $desa['nama_desa']; ?></p>
    <p class="text-xs text-gray-500 mt-1 italic">"Melayani warga dengan tulus dan bijaksana."</p>
</div>
