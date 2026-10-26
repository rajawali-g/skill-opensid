<div class="widget-box bg-white p-6 rounded-xl shadow-sm border border-gray-100">
    <h3 class="text-base font-bold text-gray-900 mb-4 flex items-center justify-between border-b pb-2">
        <span>Transparansi APBDes</span>
        <span class="text-xs text-blue-600 bg-blue-50 px-2 py-1 rounded">Tahun <?= date('Y'); ?></span>
    </h3>
    <div class="space-y-4">
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="font-medium text-gray-600">Pendapatan Desa</span>
                <span class="font-bold text-green-600">Rp <?= number_format($transparansi['pendapatan'] ?? 1250000000, 0, ',', '.'); ?></span>
            </div>
            <div class="w-full bg-gray-200 h-2 rounded-full overflow-hidden">
                <div class="bg-green-500 h-2 rounded-full" style="width: 85%"></div>
            </div>
        </div>
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="font-medium text-gray-600">Belanja Desa</span>
                <span class="font-bold text-orange-600">Rp <?= number_format($transparansi['belanja'] ?? 1180000000, 0, ',', '.'); ?></span>
            </div>
            <div class="w-full bg-gray-200 h-2 rounded-full overflow-hidden">
                <div class="bg-orange-500 h-2 rounded-full" style="width: 78%"></div>
            </div>
        </div>
    </div>
</div>
