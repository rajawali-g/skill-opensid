<h3 class="text-base font-bold text-white mb-4 border-b border-gray-800 pb-2 flex items-center justify-between">
    <span><?= $judul_widget ?? 'Aparatur'; ?></span>
    <span class="text-xs text-cyan-400 font-mono">Digital Signature Ready</span>
</h3>
<div class="text-center">
    <div class="relative w-24 h-24 mx-auto mb-3">
        <img src="<?= gambar_pamong($desa['foto_kepala_desa']); ?>" alt="Kepala Desa" class="w-full h-full object-cover rounded-full border-2 border-cyan-400 shadow">
        <span class="absolute bottom-0 right-0 w-4 h-4 bg-emerald-500 border-2 border-gray-900 rounded-full" title="Online"></span>
    </div>
    <h4 class="font-bold text-white text-sm"><?= $desa['nama_kepala_desa']; ?></h4>
    <p class="text-xs text-cyan-400">Kepala Desa <?= $desa['nama_desa']; ?></p>
</div>
