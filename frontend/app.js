const API_URL = process.env.REACT_APP_API_URL;

const dreamsCache = {
  data: null,
  lastFetch: -Infinity,
};

const fetchDreams = async () => {
  const now = Date.now();
  if (now - dreamsCache.lastFetch < 60000 && dreamsCache.data !== null) {
    console.log('Using cached dreams');
    displayDreams(dreamsCache.data);
    return;
  }

  try {
    const response = await fetch(`${API_URL}/dreams`);
    if (!response.ok) throw new Error('Failed to fetch dreams');

    const data = await response.json();
    dreamsCache.data = data;
    dreamsCache.lastFetch = Date.now();
    displayDreams(data);
  } catch (error) {
    console.error('Error fetching dreams:', error);
  }
};

const createOrUpdateOrDeleteDream = async (method, dream = {}, id = '') => {
  const url = id ? `${API_URL}/dreams/${id}` : `${API_URL}/dreams`;
  try {
    const options = {
      method: method,
      headers: { 'Content-Type': 'application/json' },
    };
    if (method !== 'DELETE') options.body = JSON.stringify(dream);

    const response = await fetch(url, options);
    if (!response.ok) throw new Error(`Failed to ${method === 'POST' ? 'create' : method === 'PUT' ? 'update' : 'delete'} dream`);

    dreamsCache.data = null;
    fetchDreams();
  } catch (error) {
    console.error(`Error ${method === 'POST' ? 'creating' : method === 'PUT' ? 'updating' : 'deleting'} dream:`, error);
  }
};

const displayDreams = (dreams) => {
  const dreamsContainer = document.getElementById('dreams-container');
  dreamsContainer.innerHTML = '';

  dreams.forEach((dream) => {
    const dreamElement = document.createElement('div');
    dreamElement.innerText = `${dream.description} - Analysis: ${dream.analysis}`;
    dreamsContainer.appendChild(dreamElement);
  });
};

document.addEventListener('DOMContentLoaded', () => {
  fetchDreams();

  const createForm = document.getElementById('create-dream-form');
  createForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const dreamDesc = document.getElementById('dream-description').value;
    await createOrUpdateOrDeleteDream('POST', { description: dreamDesc });
    createForm.reset();
  });

  document.getElementById('dreams-container').addEventListener('click', (event) => {
    const target = event.target;

    if (target.className.includes('delete-button')) {
      const dreamId = target.getAttribute('data-id');
      createOrUpdateOrDeleteDream('DELETE', {}, dreamId);
    }

    if (target.className.includes('update-button')) {
      const dreamId = target.getAttribute('data-id');
      const updatedDescription = prompt('Update your dream description:');
      if (updatedDescription) {
        createOrUpdateOrDeleteDream('PUT', { description: updatedDescription }, dreamId);
      }
    }
  });
});