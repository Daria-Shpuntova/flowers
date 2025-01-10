import './CharacteristicsKingdom.css'
import React, { useEffect, useState } from 'react';

export default function CharacteristicsKingdom(){
    const [set, newSet] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/api/characteristics')
            .then(response => response.json())
            .then(data => {
                newSet(data);
            })
            .catch(error => console.error('Error fetching data:', error));
    }, []);


    return (
        <section>
            <div className='bigName'>
                <h2>Характеристики царства растений</h2>
            </div>
            <div className='characteristics'>
                {set.map(s => (
                    <div key={s.id} className='characteristic'>
                        <h3>{s.name}</h3>
                        <p>{s.description}</p>
                    </div>
                ))}
            </div>
        </section>
    )
}