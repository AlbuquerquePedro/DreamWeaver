const API_URL = process.env.REACT_APP_API_URL;

const fetchDreams = async () => {
    try {
        const response = await fetch(`${API_URL}/dreams`);
        const data = await response.json();
        if (response.ok) {
            displayDreams(data);
        } else {
            throw new Error('Failed to fetch dreams');
        }
    } catch (error) {
        console.error('Error fetching dreams:', error);
    }
};

const displayDreams = (dreams) => {
    const dreamsContainer = document.getElementById('dreams-container');
    dreamsContainer.innerHTML = '';
    dreams.forEach(dream => {
        const dreamElement = document.createElement('div');
        dreamElement.innerText = `${dream.description} - Analysis: ${dream.analysis}`;
        dreamsContainer.appendChild(dreamElement);
    });
};

const createDream = async (dream) => {
    try {
        const response = await fetch(`${API_URL}/dreams`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dream),
        });
        if (!response.ok) {
            throw new Error('Failed to create dream');
        }
        fetchDreams();
    } catch (error) {
        console.error('Error creating dream:', error);
    }
};

const updateDream = async (id, dreamUpdate) => {
    try {
        const response = await fetch(`${API_URL}/dreams/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dreamUpdate),
        });
        if (!response.ok) {
            throw new Error('Failed to update dream');
        }
        fetchDreams();
    } catch (error) {
        console.error('Error updating dream:', error);
    }
};

const deleteDream = async (id) => {
    try {
        const response = await fetch(`${API_URL}/dreams/${id}`, {
            method: 'DELETE',
        });
        if (!response.ok) {
            throw new Error('Failed to delete dream');
        }
        fetchDreams();
    } catch (error) {
        console.error('Error deleting dream:', error);
    }
};

document.addEventListener('DOMContentLoaded', () => {
    fetchDreams();

    const createForm = document.getElementById('create-dream-form');
    createForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const dreamDesc = document.getElementById('dream-description').value;
        await createDream({ description: dreamDesc });
        createForm.reset();
    });

    document.getElementById('dreams-container').addEventListener('click', e => {
        if (e.target.className === 'delete-button') {
            const dreamId = e.target.getAttribute('data-id');
            deleteDream(dreamId);
        }

        if (e.target.className === 'update-button') {
            const dreamId = e.target.getAttribute('data-id');
            const updatedDescription = prompt('Update your dream description:');
            updateDream(dreamId, { description: updatedDescription });
        }
    });
});