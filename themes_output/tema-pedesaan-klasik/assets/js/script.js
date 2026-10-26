document.addEventListener('DOMContentLoaded', function() {
    console.log('[Tema Pedesaan Klasik] Diaktifkan.');
    var petaElem = document.getElementById('peta-desa-klasik');
    if (petaElem && typeof L !== 'undefined') {
        var map = L.map('peta-desa-klasik').setView([-1.2, 124.8], 12);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);
    }
});
