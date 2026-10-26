@extends('theme::template')

@section('layout')
    <div class="flex flex-col lg:flex-row gap-6">
        <main class="lg:w-2/3 w-full space-y-6">
            @yield('content')
        </main>
        <aside class="lg:w-1/3 w-full space-y-6">
            @include('theme::partials.sidebar')
        </aside>
    </div>
@endsection
