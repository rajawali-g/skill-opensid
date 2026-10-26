<h3 class="text-base font-bold text-slate-900 mb-4 flex justify-between items-center border-b pb-2">
    <span><?= $judul_widget ?? 'Transparansi Anggaran'; ?></span>
    <span class="text-xs bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-semibold">T.A. <?= date('Y'); ?></span>
</h3>
<div class="space-y-4 text-xs">
    <div>
        <div class="flex justify-between mb-1.5 font-medium">
            <span class="text-slate-600">Realisasi Pendapatan</span>
            <span class="font-bold text-emerald-600">Rp <?= number_format($transparansi['pendapatan'] ?? 1250000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
            <div class="bg-emerald-500 h-full rounded-full" style="width: 86%"></div>
        </div>
    </div>
    <div>
        <div class="flex justify-between mb-1.5 font-medium">
            <span class="text-slate-600">Realisasi Belanja</span>
            <span class="font-bold text-blue-600">Rp <?= number_format($transparansi['belanja'] ?? 1180000000, 0, ',', '.'); ?></span>
        </div>
        <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
            <div class="bg-blue-600 h-full rounded-full" style="width: 79%"></div>
        </div>
    </div>
</div>
