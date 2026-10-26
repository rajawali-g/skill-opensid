<?php defined('BASEPATH') || exit('No direct script access allowed'); ?>
<!DOCTYPE html>
<html lang="id">
<head>
    <?php include(__DIR__ . '/layouts/header.php'); ?>
</head>
<body class="bg-gray-50 text-gray-800">
    <!-- Header / Navigasi Desa -->
    <header class="desa-header shadow-sm">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <img src="<?= gambar_desa($desa['logo']); ?>" alt="Logo Desa" class="h-12 w-auto">
                <div>
                    <h1 class="text-xl font-bold text-gray-900"><?= $desa['nama_desa']; ?></h1>
                    <p class="text-sm text-gray-500">Kec. <?= $desa['nama_kecamatan']; ?>, Kab. <?= $desa['nama_kabupaten']; ?></p>
                </div>
            </div>
            <nav class="hidden md:flex space-x-6 text-sm font-medium items-center">
                <a href="<?= site_url(); ?>" class="nav-link">Beranda</a>
                <a href="<?= site_url('profil-desa'); ?>" class="nav-link">Profil</a>
                <a href="<?= site_url('artikel'); ?>" class="nav-link">Kabar Desa</a>
                <a href="<?= site_url('layanan-mandiri'); ?>" class="btn-mandiri">Layanan Mandiri</a>
            </nav>
        </div>
    </header>

    <!-- Konten Utama -->
    <main class="container mx-auto px-4 py-8 grid grid-cols-1 lg:grid-cols-3 gap-8">
        <section class="lg:col-span-2 space-y-6">
            <?php include(__DIR__ . '/partials/artikel.php'); ?>
            <?php include(__DIR__ . '/partials/apbdes.php'); ?>
            <?php include(__DIR__ . '/partials/peta.php'); ?>
        </section>

        <aside class="space-y-6">
            <?php include(__DIR__ . '/layouts/sidebar.php'); ?>
        </aside>
    </main>

    <!-- Footer -->
    <?php include(__DIR__ . '/layouts/footer.php'); ?>
    <script src="<?= base_url("desa/themes/tema-starter-minsel/assets/js/theme.js"); ?>"></script>
</body>
</html>
