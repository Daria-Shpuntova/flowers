//import { useEffect, useState } from 'react';
import './header.css';

//export default function Header({url}){
//    const [set, newSet] = useState([]);
//
//    useEffect(() => {
//        console.log(url)
//        fetch(url)
//            .then(response => response.json())
//            .then(data => {
//                newSet(data);
//            })
//            .catch(error => console.error('Error fetching data:', error));
//    }, [url]);
//
//
//    return (
//        <>
//            <nav>
//                <div><a href='#'>Царство</a></div>
//                <form className='search'>
//                    <input type="text" name="text" placeholder='Поиск'/>
//                    <button>
//                    </button>
//                </form>
//            </nav>
//
//            <div>
//                {set.map(s => (
//                    <div key={s.id} className='headerH1'>
//                        <div className='headerText'>
//                            <h1>{s.name}</h1>
//                            <p>{s.description}</p>
//                        </div>
//
//                        <div className='headerFoto'>
//                            <img src={`${s.image}`} alt={s.name}/>
//                        </div>
//                    </div>
//                ))}
//            </div>
//        </>
//    )
//}


import { useEffect, useState } from 'react';
import './header.css';

const Header = ({ url }) => {

    console.log(url, 'url5')
    const [set, newSet] = useState([]);
    const [error, setError] = useState(null); // Добавляем состояние для ошибок

    useEffect(() => {
        fetch(url)
            .then(response => {
                console.log(response, 'response')
                console.log(!response.ok, '!response.ok')
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data, 'data')
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
                <div><a href='#'>Царство</a></div>
                <form className='search'>
                    <input type="text" name="text" placeholder='Поиск' />
                    <button type="submit">Поиск</button>
                </form>
            </nav>

            <div>
                {set.map(s => (
                    <div key={s.id} className='headerH1'>
                        <div className='headerText'>
                            <h1>{s.name}</h1>
                            <p>{s.description}</p>
                        </div>

                        <div className='headerFoto'>
                            <img src={`${s.image}`} alt={s.name} />
                        </div>
                    </div>
                ))}
            </div>
        </>
    );
}


export default Header;