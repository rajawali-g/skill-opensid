<h3 class="card-title-klasik font-bold text-base flex justify-between items-center">
    <span><?= $judul_widget ?? 'APBDes Desa'; ?></span>
    <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-0.5 rounded font-mono"><?= date('Y'); ?></span>
</h3>
<div class="space-y-3 text-xs">
    <div>
        <div class="flex justify-between font-semibold mb-1">
            <span class="text-gray-700">Pendapatan Asli & Dana Desa</span>
            <span class="text-green-700">Rp <?= number_format($transparansi['pendapatan'] ?? 1250000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-200 h-2.5 rounded-full overflow-hidden">
            <div class="bg-green-600 h-full rounded-full" style="width: 82%"></div>
        </div>
    </div>
    <div>
        <div class="flex justify-between font-semibold mb-1">
            <span class="text-gray-700">Belanja Pembangunan & Warga</span>
            <span class="text-amber-700">Rp <?= number_format($transparansi['belanja'] ?? 1180000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-gray-200 h-2.5 rounded-full overflow-hidden">
            <div class="bg-amber-600 h-full rounded-full" style="width: 76%"></div>
        </div>
    </div>
</div>
