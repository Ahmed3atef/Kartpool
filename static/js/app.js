// Initialize the Leaflet map centered on a default location (will update after getting user's location)
const map = L.map('map').setView([30.033333, 31.233334], 13); // Default location (San Francisco)

// Use OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Global markers array to keep track of added markers
let markers = [];

// Function to clear existing markers
function clearMarkers() {
    markers.forEach(marker => map.removeLayer(marker));
    markers = [];
}

// Function to add markers for nearby stores on the map
function addStoreMarkers(stores) {
    clearMarkers();  // Clear existing markers

    stores.forEach(store => {
        const marker = L.marker([store.latitude, store.longitude])
            .addTo(map)
            .bindPopup(`<b>${store.name}</b><br>Type: ${store.store_type}<br>Address: ${store.address}<br>Distance: ${store.distance} km`)
        markers.push(marker);
    });
}

// Function to Show the user's current location on the map
function showUserLocation(lat, lng) {
    // Add a marker for the user's location
    let userMarker = L.marker([lat, lng],{color:'red'}).addTo(map).bindPopup("You are here!");
    L.circle([lat,lng],{
        color: 'blue',
        radius: 15, // You can adjust the radius
    }).addTo(map);

    // Pan the map to the user's location
    map.setView([lat, lng], 13);
}

// Function to update the store list in the HTML
function updateStoreList(stores) {
    const storeList = document.getElementById('store-list');
    storeList.innerHTML = '';  // Clear the existing store list

    stores.forEach(store => {
        const storeItem = document.createElement('div');
        storeItem.className = 'store-item';
        storeItem.innerHTML = `
        <a href="store/${store.id}">
            <b>${store.name}</b>
        </a>
        <br>
        Type: ${store.store_type}
        <br>
        Distance: ${store.distance} km
        <br>
        Opening: ${store.opening_hour}
        <br>
        Closeing: ${store.closing_hour}
        <br>
        Rating: `;
        let rating = parseInt(store.rating, 0)
        for(let i=0; i < rating; i++){
            storeItem.innerHTML+=`<span class="fa fa-star checked"></span>`
        }
        storeList.appendChild(storeItem);
    });
}

// Function to fetch nearby or searched stores from the API
function fetchStores(apiUrl) {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            addStoreMarkers(data);   // Add markers to the map
            updateStoreList(data);   // Update the store list in the HTML
        })
        .catch(error => {
            console.error('Error fetching stores:', error);
            alert('Error fetching stores');
        });
}

// Function to handle success when getting user's location
function onLocationSuccess(position, searchQuery = null) {
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;

    // Show user's location on the map
    showUserLocation(lat, lng);

    // Construct the API URL based on whether it's a search or fetching nearby stores
    let apiUrl;
    if (searchQuery) {
        apiUrl = `http://127.0.0.1:8000/api/stores_search/?q=${searchQuery}&lat=${lat}&lng=${lng}`;
    } else {
        apiUrl = `http://127.0.0.1:8000/api/stores/?lat=${lat}&lng=${lng}`;
    }

    // Fetch stores based on location and search query if provided
    fetchStores(apiUrl);
}

// Function to handle error when getting user's location
function onLocationError(error) {
    console.error('Error getting location:', error);
    alert('Unable to retrieve your location');
}

// Use the Geolocation API to get user's current location
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(onLocationSuccess, onLocationError);
} else {
    alert('Geolocation is not supported by your browser');
}

// Handle search box form submission
document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent form from reloading the page

    const searchQuery = document.getElementById('search-box').value.trim();

    if (searchQuery !== '') {
        // Get the user's location
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(position => {
                // Call the function to fetch stores based on the search query and user's location
                onLocationSuccess(position, searchQuery);
            }, onLocationError);
        } else {
            alert('Geolocation is not supported by your browser');
        }
    } else {
        alert('Please enter a search term');
    }
});
