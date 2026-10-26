<footer class="bg-gray-950 text-gray-400 py-12 mt-16 border-t border-gray-800 text-sm">
    <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
            <h3 class="font-bold text-white text-base mb-3 flex items-center space-x-2">
                <span>Pusat Layanan Digital</span>
                <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
            </h3>
            <p><?= $desa['alamat_kantor']; ?></p>
            <p>Kode Pos <?= $desa['kode_pos']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white text-base mb-3">Integrasi SPBE & OpenSID</h3>
            <p>Pemerintahan Cerdas berbasis satu data desa terpadu.</p>
            <p class="mt-2 text-cyan-400 text-xs">Email: <?= $desa['email_desa']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white text-base mb-3">Keamanan & Keandalan</h3>
            <p>Didukung Enkripsi SSL & Validasi TTE.</p>
            <p class="text-xs text-gray-600 mt-2">&copy; <?= date('Y'); ?> Smart Village <?= $desa['nama_desa']; ?>.</p>
        </div>
    </div>
</footer>
