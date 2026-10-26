@extends('theme::template')

@section('layout')
    <div class="container mx-auto px-4 my-6 flex flex-col lg:flex-row gap-6">
        <main class="lg:w-2/3 w-full bg-white rounded-xl p-6 shadow-sm border border-gray-100">
            @yield('content')
        </main>
        <aside class="lg:w-1/3 w-full space-y-6">
            @include('theme::partials.sidebar')
        </aside>
    </div>
@endsection
