<h3 class="text-base font-bold text-white mb-4 flex justify-between items-center border-b border-gray-800 pb-2">
    <span><?= $judul_widget ?? 'APBDes Data'; ?></span>
    <span class="text-xs bg-cyan-950 text-cyan-400 border border-cyan-800 px-2 py-0.5 rounded font-mono"><?= date('Y'); ?></span>
</h3>
<div class="space-y-4 text-xs">
    <div>
        <div class="flex justify-between mb-1">
            <span class="text-gray-400">Target Pendapatan</span>
            <span class="font-bold text-cyan-400">Rp <?= number_format($transparansi['pendapatan'] ?? 1250000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-800 h-2 rounded-full overflow-hidden">
            <div class="bg-gradient-to-r from-cyan-500 to-blue-500 h-full rounded-full" style="width: 88%"></div>
        </div>
    </div>
    <div>
        <div class="flex justify-between mb-1">
            <span class="text-gray-400">Realisasi Belanja</span>
            <span class="font-bold text-purple-400">Rp <?= number_format($transparansi['belanja'] ?? 1180000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-800 h-2 rounded-full overflow-hidden">
            <div class="bg-gradient-to-r from-purple-500 to-pink-500 h-full rounded-full" style="width: 80%"></div>
        </div>
    </div>
</div>
