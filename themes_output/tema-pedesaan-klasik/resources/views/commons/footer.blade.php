<footer class="bg-yellow-950 text-yellow-100 py-10 mt-12 border-t-4 border-yellow-600">
    <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8 text-sm">
        <div>
            <h3 class="font-bold text-yellow-400 text-base mb-2">Kantor Pemerintah Desa <?= $desa['nama_desa']; ?></h3>
            <p><?= $desa['alamat_kantor']; ?></p>
            <p>Kode Pos: <?= $desa['kode_pos']; ?></p>
            <p class="mt-2 text-xs text-yellow-300">Gotong royong membangun lumbung desa mandiri.</p>
        </div>
        <div>
            <h3 class="font-bold text-yellow-400 text-base mb-2">Kontak Kerukunan Warga</h3>
            <p>Telepon Kantor: <?= $desa['telepon']; ?></p>
            <p>Surel Resmi: <?= $desa['email_desa']; ?></p>
        </div>
        <div>
            <h3 class="font-bold text-yellow-400 text-base mb-2">Sistem Informasi Desa</h3>
            <p>Tema Pedesaan Klasik &bullet; Ditenagai OpenSID</p>
        </div>
    </div>
</footer>
