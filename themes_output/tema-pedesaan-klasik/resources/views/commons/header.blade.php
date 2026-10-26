<!-- Top Bar Sambutan Desa -->
<div class="top-bar-pedesaan">
    <div class="container mx-auto px-4 flex justify-between items-center">
        <span>🌾 Kearifan Lokal & Guyub Rukun Warga</span>
        <span><?= date('l, d F Y'); ?></span>
    </div>
</div>

<!-- Header Identitas Desa -->
<header class="header-pedesaan py-5">
    <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-4">
        <div class="flex items-center space-x-4">
            <img src="<?= gambar_desa($desa['logo']); ?>" alt="Logo Desa" class="h-16 w-16 logo-frame">
            <div>
                <span class="text-xs font-bold uppercase tracking-wider text-green-800">Pemerintah Desa</span>
                <h1 class="text-2xl font-bold text-yellow-900 leading-tight"><?= $desa['nama_desa']; ?></h1>
                <p class="text-sm text-gray-600">Kecamatan <?= $desa['nama_kecamatan']; ?>, Kabupaten <?= $desa['nama_kabupaten']; ?></p>
            </div>
        </div>
        <div class="text-right hidden lg:block italic text-sm text-yellow-950 bg-yellow-50 p-3 rounded border border-yellow-200 max-w-md">
            "<?= $salam_kades ?? 'Tabea! Bersama Membangun Desa yang Berbudaya, Rukun, dan Sejahtera.'; ?>"
        </div>
    </div>
</header>

<!-- Navigasi Utama -->
<nav class="navbar-pedesaan">
    <div class="container mx-auto px-4 flex justify-between items-center py-2">
        <div class="flex space-x-2">
            <a href="<?= site_url(); ?>" class="nav-item-pedesaan">Beranda</a>
            <a href="<?= site_url('profil-desa'); ?>" class="nav-item-pedesaan">Profil Desa</a>
            <a href="<?= site_url('artikel'); ?>" class="nav-item-pedesaan">Kabar Desa</a>
            <a href="<?= site_url('peta'); ?>" class="nav-item-pedesaan">Peta Wilayah</a>
        </div>
        <div>
            <a href="<?= site_url('layanan-mandiri'); ?>" class="btn-mandiri-klasik">Pelayanan Warga Online</a>
        </div>
    </div>
</nav>
