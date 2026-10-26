<footer class="bg-gray-900 text-gray-300 py-10 mt-12 text-sm">
    <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
            <h3 class="font-bold text-white mb-3">Pemerintah Desa <?= $desa['nama_desa']; ?></h3>
            <p><?= $desa['alamat_kantor']; ?></p>
            <p>Kode Pos: <?= $desa['kode_pos']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white mb-3">Kontak Pelayanan</h3>
            <p>Email: <?= $desa['email_desa']; ?></p>
            <p>Telepon: <?= $desa['telepon']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-white mb-3">Sistem Informasi Desa</h3>
            <p>Ditenagai oleh OpenSID. Dikelola oleh Tim Publikasi Desa.</p>
        </div>
    </div>
</footer>
