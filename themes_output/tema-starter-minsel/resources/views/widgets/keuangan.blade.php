<h3 class="text-base font-bold text-gray-900 mb-4 flex justify-between items-center border-b pb-2">
    <span><?= $judul_widget ?? 'APBDes'; ?></span>
    <span class="text-xs text-blue-600 bg-blue-50 px-2 py-1 rounded">Tahun <?= date('Y'); ?></span>
</h3>
<div class="space-y-3 text-xs">
    <div>
        <div class="flex justify-between mb-1">
            <span class="text-gray-600">Pendapatan</span>
            <span class="font-bold text-green-600">Rp <?= number_format($transparansi['pendapatan'] ?? 1250000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-200 h-2 rounded-full overflow-hidden">
            <div class="bg-green-500 h-2 rounded-full" style="width: 85%"></div>
        </div>
    </div>
    <div>
        <div class="flex justify-between mb-1">
            <span class="text-gray-600">Belanja</span>
            <span class="font-bold text-orange-600">Rp <?= number_format($transparansi['belanja'] ?? 1180000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-200 h-2 rounded-full overflow-hidden">
            <div class="bg-orange-500 h-2 rounded-full" style="width: 78%"></div>
        </div>
    </div>
</div>
