document.addEventListener('DOMContentLoaded', function() {
    console.log('[Tema Desa Digital] Smart Village System Loaded.');
    var petaElem = document.getElementById('peta-desa-digital');
    if (petaElem && typeof L !== 'undefined') {
        var map = L.map('peta-desa-digital').setView([-1.2, 124.8], 13);
        L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; CartoDB & OpenStreetMap'
        }).addTo(map);
    }
});
