async function fetchItems() {
    try {
        const response = await fetch('http://localhost:5000/items');
        const items = await response.json();
        const dropdown = document.getElementById('items-dropdown');

        // Vider le menu déroulant
        dropdown.innerHTML = '';

        if (items.length === 0) {
            const option = document.createElement('option');
            option.textContent = 'Aucun item disponible';
            dropdown.appendChild(option);
            return;
        }

        // Ajouter les items dans le menu déroulant
        items.forEach(item => {
            const option = document.createElement('option');
            option.value = item.id; // Assure-toi que ta table a un champ id
            option.textContent = item.name; // ou item.titre selon ta table
            dropdown.appendChild(option);
        });
    } catch (error) {
        console.error('Erreur:', error);
        const dropdown = document.getElementById('items-dropdown');
        dropdown.innerHTML = '';
        const option = document.createElement('option');
        option.textContent = 'Impossible de récupérer les items';
        dropdown.appendChild(option);
    }
}

// Charger les items au chargement de la page
window.onload = fetchItems;
