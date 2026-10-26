@php
    $themeVersion = 'v1.0.0';
@endphp
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    @include('theme::commons.meta')
    @include('theme::commons.source_css')
    <title>@yield('title', $heading ?? $desa['nama_desa'])</title>
    @stack('styles')
</head>
<body class="bg-gray-50 text-gray-800 font-sans">
    @include('theme::commons.header')

    {{-- Konten layout (full-content atau right-sidebar) --}}
    @yield('layout')

    @include('theme::commons.footer')

    <script src="{{ theme_asset('js/script.js') }}"></script>
    @stack('scripts')
</body>
</html>
