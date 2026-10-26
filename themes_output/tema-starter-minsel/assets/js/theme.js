document.addEventListener('DOMContentLoaded', function() {
    var petaElem = document.getElementById('peta-desa');
    if (petaElem && typeof L !== 'undefined') {
        var map = L.map('peta-desa').setView([-1.2, 124.8], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);
    }
});
