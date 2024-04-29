window.onload = function() {
    fetchBrands();
    fetchModels();
    fetchVehicles();
};


function fetchBrands() {
    fetch('http://localhost:3000/api/getBrands')
        .then(response => response.json())
        .then(brands => {
            populateDropdown(brands, 'brand-select');
        })
        .catch(error => console.error('Error fetching brands:', error));
}

// Update other API calls similarly


function fetchModels() {
    fetch('http://localhost:3000/api/getModels')
        .then(response => response.json())
        .then(models => {
            populateDropdown(models, 'model-select');
        })
        .catch(error => console.error('Error fetching models:', error));
}

function fetchVehicles() {
    fetch('http://localhost:3000/api/getVehicles')
        .then(response => response.json())
        .then(vehicles => {
            populateVehiclesList(vehicles);
        })
        .catch(error => console.error('Error fetching vehicles:', error));
}

function searchAndDisplayVehicles() {
    const brandId = document.getElementById('brand-select').value;
    const modelId = document.getElementById('model-select').value;
    // Fetch and display vehicles based on selected brand and model
}

function populateDropdown(items, selectId) {
    const select = document.getElementById(selectId);
    select.innerHTML = '';  // Clear existing options
    items.forEach(item => {
        let option = document.createElement('option');
        option.value = item.id;
        option.textContent = item.name;
        select.appendChild(option);
    });
}

function populateVehiclesList(vehicles) {
    const vehiclesList = document.getElementById('vehicles-list');
    vehiclesList.innerHTML = '';  // Clear existing vehicles
    vehicles.forEach(vehicle => {
        const vehicleDiv = document.createElement('div');
        vehicleDiv.textContent = `Brand: ${vehicle.brand}, Model: ${vehicle.model}, VIN: ${vehicle.vin}`;
        vehiclesList.appendChild(vehicleDiv);
    });
}
