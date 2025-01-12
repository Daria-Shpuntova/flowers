import React, { useEffect, useState } from 'react';
import {Link, useParams} from 'react-router-dom';

import log from "eslint-plugin-react/lib/util/log.js";


const DescriptionClassName = () => {
    const { division_slug, class_name_slug } = useParams(); // Извлекаем оба slug'а
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch(`http://localhost:8000/api/kingdom/${division_slug}/${class_name_slug}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setData(data);
            })
            .catch(error => console.error('Fetch error:', error));
    }, [division_slug, class_name_slug]);

    if (!data) return <div>Loading...</div>;

    return (
        <>
            <section>
                <h2>Описание Класса</h2>
                <div className='types'>
                        <p>{data.descriptionBig}</p>
                </div>
            </section>
            <section>
                {data.orderClass && data.orderClass.length > 0 && (
                    <>
                        <h2>Порядки</h2>
                        <div className='lists'>
                            {data.orderClass.map(ord => (
                                <Link key={ord.slug} to={ord.slug}>{ord.name}</Link>
                            ))}
                        </div>
                    </>
                )}
            </section>
        </>
    );
}

export default DescriptionClassName;
