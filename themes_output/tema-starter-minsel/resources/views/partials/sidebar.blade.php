<div class="space-y-6">
    @if ($widgetAktif ?? false)
        @foreach ($widgetAktif as $widget)
            @php
                $judul_widget = [
                    'judul_widget' => str_replace('Desa', ucwords(setting('sebutan_desa')), strip_tags($widget['judul'])),
                ];
            @endphp
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-5 overflow-hidden">
                @includeIf("theme::widgets.{$widget['isi']}", $judul_widget)
            </div>
        @endforeach
    @else
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
            @include('theme::widgets.aparatur_desa', ['judul_widget' => 'Aparatur Desa'])
        </div>
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
            @include('theme::widgets.keuangan', ['judul_widget' => 'Transparansi APBDes'])
        </div>
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
            @include('theme::widgets.peta_wilayah_desa', ['judul_widget' => 'Peta Wilayah Desa'])
        </div>
    @endif
</div>
