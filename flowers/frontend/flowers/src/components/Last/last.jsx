import "./last.css";
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const LastSpecies = () => {
    const [specieslast, setSpecieslast] = useState([]);

    useEffect(() => {
        const fetchSpecies = async () => {
            const response = await axios.get('http://localhost:8000/api/specieslast'); // Убедитесь, что путь правильный
            setSpecieslast(response.data);
        };
        fetchSpecies();
    }, []);

    const truncateWords = (text, wordLimit) => {
        const words = text.split(' ');
        return words.length > wordLimit ? words.slice(0, wordLimit).join(' ') + '...' : text;
    };

    return (
        <section>
            <div className='bigName'>
                <h2>Последне добавленые Виды</h2>
            </div>
            <div className='lastSpecies'>
            {specieslast.map(item => (
                <div key={item.slug}>
                    <h3>{item.name}</h3>
                    <div className='lastSpeciesText'>
                        <p>{truncateWords(item.description, 40)}</p>
                        <div className='lastSpeciesImg'>
                            <img src={item.image} alt={item.name}/>
                        </div>
                    </div>
                </div>
            ))}
            </div>
        </section>
    );
};

export default LastSpecies;
