import "./types.css";
import { useEffect, useState } from 'react';

export default function Types(){
    const [set, newSet] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/api/type')
            .then(response => response.json())
            .then(data => {
                newSet(data);
            })
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <section>
            <div className='bigName'>
                <h2>Основные типы растений</h2>
            </div>
            <div className='typesAll'>
            {set.map(s => (
                <div key={s.id} className='types'>
                    <div className='typesText'>
                        <h3>{s.name}</h3>
                        <p><strong>Описание:</strong><br/> {s.description}</p>
                        <p><strong>Характеристики:</strong><br/> {s.characteristics}</p>

                        <p><strong>Примеры:</strong><br/> {s.examples.map(example => example.name).join(', ')}</p>
                    </div>
                    <div className='typesFoto'>
                        {s.examples.map(example => (
                            <img key={example.id} src={`${example.image}`}
                                 alt={example.name}/>
                        ))}
                    </div>
                </div>
            ))}
            </div>
        </section>
    )
}