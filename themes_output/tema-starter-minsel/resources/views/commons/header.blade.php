<header class="bg-white border-b border-gray-200 sticky top-0 z-50 shadow-sm">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <div class="flex items-center space-x-3">
            <img src="<?= gambar_desa($desa['logo']); ?>" alt="Logo Desa" class="h-12 w-auto">
            <div>
                <h1 class="text-lg font-bold text-gray-900"><?= $desa['nama_desa']; ?></h1>
                <p class="text-xs text-gray-500">Kec. <?= $desa['nama_kecamatan']; ?>, Kab. <?= $desa['nama_kabupaten']; ?></p>
            </div>
        </div>
        <nav class="hidden md:flex space-x-6 text-sm font-medium items-center">
            <a href="<?= site_url(); ?>" class="text-gray-700 hover:text-blue-600">Beranda</a>
            <a href="<?= site_url('profil-desa'); ?>" class="text-gray-700 hover:text-blue-600">Profil</a>
            <a href="<?= site_url('artikel'); ?>" class="text-gray-700 hover:text-blue-600">Kabar Desa</a>
            <a href="<?= site_url('layanan-mandiri'); ?>" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">Layanan Mandiri</a>
        </nav>
    </div>
</header>
