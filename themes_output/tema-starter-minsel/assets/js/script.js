document.addEventListener('DOMContentLoaded', function() {
    var petaElem = document.getElementById('peta-desa-widget');
    if (petaElem && typeof L !== 'undefined') {
        var map = L.map('peta-desa-widget').setView([-1.2, 124.8], 12);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);
    }
});
