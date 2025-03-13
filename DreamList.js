import React, { useState, useEffect } from 'react';

const DREAMS_API_URL = process.env.REACT_APP_DREAMS_API_URL;

const DreamListViewer = () => {
    const [dreamList, setDreamList] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        async function fetchDreams() {
            try {
                const response = await fetch(DREAMS_API_URL);

                if (!response.ok) {
                    throw new Error('Failed to fetch dreams');
                }

                const dreamsData = await response.json();
                setDreamList(dreamsData);
            } catch (error) {
                console.error("Error while fetching dreams:", error);
            } finally {
                setIsLoading(false);
            }
        }

        fetchDreams();
    }, []);

    if (isLoading) {
        return <div>Loading dreams...</div>;
    }

    if (!dreamList.length) {
        return <div>No dreams found</div>;
    }

    return (
        <div>
            <h2>Dream List</h2>
            <ul>
                {dreamList.map(({ id, title, description }) => (
                    <li key={id}>
                        <h3>{title}</h3>
                        <p>{description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default DreamListViewer;