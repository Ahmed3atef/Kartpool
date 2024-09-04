// app.js

// Initialize the Leaflet map
const map = L.map('map').setView([37.7749, -122.4194], 13); // Centered on San Francisco

// Use OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Sample store data (you would fetch this from your backend)
const stores = [
    {
        name: "Local Grocery Store",
        coordinates: [37.7749, -122.4194]
    },
    {
        name: "Pharmacy",
        coordinates: [37.7690, -122.4233]
    },
    {
        name: "Hardware Store",
        coordinates: [37.8024, -122.4156]
    }
];

// Add stores to the map as markers
stores.forEach(store => {
    L.marker(store.coordinates)
        .addTo(map)
        .bindPopup(`<b>${store.name}</b>`)
        .openPopup();
});

// Display store list
const storeList = document.getElementById('store-list');
stores.forEach(store => {
    const storeItem = document.createElement('div');
    storeItem.className = 'store-item';
    storeItem.textContent = store.name;
    storeList.appendChild(storeItem);
});
