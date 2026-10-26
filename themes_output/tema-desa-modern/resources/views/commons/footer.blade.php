<footer class="bg-slate-900 text-slate-300 py-12 mt-16 border-t border-slate-800 text-sm">
    <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
            <h3 class="font-bold text-white text-base mb-3">Pemerintah Desa <?= $desa['nama_desa']; ?></h3>
            <p class="text-slate-400"><?= $desa['alamat_kantor']; ?></p>
            <p class="text-slate-400">Kode Pos <?= $desa['kode_pos']; ?></p>
            <p class="mt-4 text-xs text-slate-500">Pelayanan publik berbasis tata kelola pemerintahan yang bersih dan akuntabel.</p>
        </div>
        <div>
            <h3 class="font-bold text-white text-base mb-3">Saluran Informasi</h3>
            <p class="text-slate-400">Surat Elektronik: <?= $desa['email_desa']; ?></p>
            <p class="text-slate-400">Telepon Layanan: <?= $desa['telepon']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white text-base mb-3">Infrastruktur Digital</h3>
            <p class="text-slate-400">Ditenagai oleh Ekosistem OpenSID.</p>
            <p class="text-xs text-slate-500 mt-2">&copy; <?= date('Y'); ?> Pemerintah Desa <?= $desa['nama_desa']; ?>. Hak cipta dilindungi.</p>
        </div>
    </div>
</footer>
