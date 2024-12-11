import React, { useState, useEffect } from 'react';
const API_URL = process.env.REACT_APP_DREAMS_API_URL;
const DreamList = () => {
    const [dreams, setDreams] = useState([]);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        const fetchDreams = async () => {
            try {
                const response = await fetch(API_URL);
                if (!response.ok) {
                    throw new Error('Failed to fetch dreams');
                }
                const data = await response.json();
                setDreams(data);
            } catch (error) {
                console.error("Error fetching dreams:", error);
            } finally {
                setLoading(false);
            }
        };
        fetchDreams();
    }, []);
    if (loading) {
        return <div>Loading dreams...</div>;
    }
    if (!dreams.length) {
        return <div>No dreams found</div>;
    }
    return (
        <div>
            <h2>Dream List</h2>
            <ul>
                {dreams.map((dream) => (
                    <li key={dream.id}>
                        <h3>{dream.title}</h3>
                        <p>{dream.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};
export default DreamList;