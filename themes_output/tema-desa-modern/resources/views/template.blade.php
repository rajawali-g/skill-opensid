<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    @include('theme::commons.meta')
    @include('theme::commons.source_css')
    <title>@yield('title', $heading ?? $desa['nama_desa']) - Portal Resmi Desa</title>
    @stack('styles')
</head>
<body>
    @include('theme::commons.header')

    <div class="container mx-auto px-4 my-8">
        @yield('layout')
    </div>

    @include('theme::commons.footer')
    <script src="{{ theme_asset('js/script.js') }}"></script>
    @stack('scripts')
</body>
</html>
