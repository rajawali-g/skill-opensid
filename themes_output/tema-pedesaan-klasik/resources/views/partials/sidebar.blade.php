<div class="space-y-6">
    <div class="card-klasik p-5">
        @include('theme::widgets.aparatur_desa', ['judul_widget' => 'Pamong & Kepala Desa'])
    </div>
    <div class="card-klasik p-5">
        @include('theme::widgets.keuangan', ['judul_widget' => 'Laporan APBDes Terbuka'])
    </div>
    <div class="card-klasik p-5">
        @include('theme::widgets.peta_wilayah_desa', ['judul_widget' => 'Batas Wilayah Agraris'])
    </div>
</div>
