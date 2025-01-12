import './header.css';
import { useEffect, useState } from 'react';
import {Link} from "react-router-dom";


const Header = ({ url }) => {
    const [set, newSet] = useState([]);
    const [error, setError] = useState(null); // Добавляем состояние для ошибок

    useEffect(() => {
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (Array.isArray(data)) {
                    newSet(data);
                } else {
                    newSet([data])
                }
            })
            .catch(error => {
                console.error('Error fetching error');
                setError(error.message); // Сохраняем сообщение об ошибке
            });
    }, [url]); // Добавляем url в зависимости

    if (error) {
        return <div>Error: {error}</div>; // Отображаем сообщение об ошибке
    }

    return (
        <>
            <nav>
                <div><Link to={`/`}>Царство Растений</Link></div>
                <div><Link to={`/admin`}>Админ панель</Link></div>
            </nav>
            <div>
                {set.map(s => (
                    <div key={`${s.slug || s.id}-${s.name}`} className='headerH1'>
                        <div className='headerText'>
                            <h1>{s.name}</h1>
                            <p>{s.description}</p>
                        </div>
                        <div className='headerFoto'>
                            <img src={`${s.image}`} alt={s.name}/>
                        </div>
                    </div>
                ))}
            </div>
        </>
    );
}


export default Header;