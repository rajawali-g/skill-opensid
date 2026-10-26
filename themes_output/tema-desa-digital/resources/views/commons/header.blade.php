<header class="digital-header sticky top-0 z-50">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <div class="flex items-center space-x-3">
            <img src="<?= gambar_desa($desa['logo']); ?>" alt="Logo Desa" class="h-10 w-auto filter drop-shadow">
            <div>
                <div class="flex items-center space-x-2">
                    <h1 class="text-lg font-bold text-white tracking-wide"><?= $desa['nama_desa']; ?></h1>
                    <span class="badge-glow text-xs px-2 py-0.5 rounded-full font-mono uppercase">Smart Village</span>
                </div>
                <p class="text-xs text-gray-400">Kec. <?= $desa['nama_kecamatan']; ?>, Kab. <?= $desa['nama_kabupaten']; ?></p>
            </div>
        </div>
        <nav class="hidden md:flex items-center space-x-6 text-sm font-medium">
            <a href="<?= site_url(); ?>" class="text-gray-300 hover:text-cyan-400 transition">Dashboard</a>
            <a href="<?= site_url('profil-desa'); ?>" class="text-gray-300 hover:text-cyan-400 transition">Profil</a>
            <a href="<?= site_url('artikel'); ?>" class="text-gray-300 hover:text-cyan-400 transition">Warta Digital</a>
            <a href="<?= site_url('peta'); ?>" class="text-gray-300 hover:text-cyan-400 transition">Geo-Portal</a>
            <a href="<?= site_url('layanan-mandiri'); ?>" class="btn-mandiri-digital">Layanan Mandiri Online</a>
        </nav>
    </div>
</header>

<!-- Live Stats Bar (Smart Village Indicator) -->
<div class="container mx-auto px-4 mt-6">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="stat-counter-box">
            <span class="text-xs text-gray-400 block mb-1">Total Penduduk</span>
            <span class="text-xl font-bold text-cyan-400"><?= number_format($total_penduduk ?? 3420); ?></span>
        </div>
        <div class="stat-counter-box">
            <span class="text-xs text-gray-400 block mb-1">Kepala Keluarga</span>
            <span class="text-xl font-bold text-purple-400"><?= number_format($total_kk ?? 980); ?></span>
        </div>
        <div class="stat-counter-box">
            <span class="text-xs text-gray-400 block mb-1">Surat Online Terbit</span>
            <span class="text-xl font-bold text-emerald-400"><?= number_format($total_surat ?? 1250); ?></span>
        </div>
        <div class="stat-counter-box">
            <span class="text-xs text-gray-400 block mb-1">Status Indeks Desa</span>
            <span class="text-xl font-bold text-amber-400">Desa Mandiri</span>
        </div>
    </div>
</div>
