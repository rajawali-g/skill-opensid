document.addEventListener('DOMContentLoaded', function() {
    console.log('[Tema Desa Modern] Aktif.');
    var petaElem = document.getElementById('peta-desa-modern');
    if (petaElem && typeof L !== 'undefined') {
        var map = L.map('peta-desa-modern').setView([-1.2, 124.8], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);
    }
});
