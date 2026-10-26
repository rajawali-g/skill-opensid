<div class="modern-topbar">
    <div class="container mx-auto px-4 flex justify-between items-center">
        <span>🏛️ Portal Resmi Pemerintahan Desa <?= $desa['nama_desa']; ?></span>
        <span class="flex items-center space-x-4">
            <span>Email: <?= $desa['email_desa']; ?></span>
            <span>Telp: <?= $desa['telepon']; ?></span>
        </span>
    </div>
</div>

<header class="modern-navbar sticky top-0 z-40">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <div class="flex items-center space-x-3">
            <img src="<?= gambar_desa($desa['logo']); ?>" alt="Logo Desa" class="h-11 w-auto">
            <div>
                <h1 class="text-lg font-bold text-slate-900 tracking-tight leading-tight"><?= $desa['nama_desa']; ?></h1>
                <p class="text-xs text-slate-500">Kec. <?= $desa['nama_kecamatan']; ?>, Kab. <?= $desa['nama_kabupaten']; ?></p>
            </div>
        </div>
        <nav class="hidden md:flex items-center space-x-4">
            <a href="<?= site_url(); ?>" class="modern-nav-link">Beranda</a>
            <a href="<?= site_url('profil-desa'); ?>" class="modern-nav-link">Profil</a>
            <a href="<?= site_url('artikel'); ?>" class="modern-nav-link">Berita & Pengumuman</a>
            <a href="<?= site_url('peta'); ?>" class="modern-nav-link">Peta WebGIS</a>
            <a href="<?= site_url('layanan-mandiri'); ?>" class="btn-mandiri-modern">Portal Warga</a>
        </nav>
    </div>
</header>
