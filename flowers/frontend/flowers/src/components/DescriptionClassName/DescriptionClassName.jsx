import React, { useEffect, useState } from 'react';
import {Link, useParams} from 'react-router-dom';

import log from "eslint-plugin-react/lib/util/log.js";


const DescriptionClassName = () => {
    const { division_slug, class_name_slug } = useParams(); // Извлекаем оба slug'а
    const [data, setData] = useState(null);

    useEffect(() => {
        console.log(`http://localhost:8000/api/kingdom/${division_slug}/${class_name_slug}`);
        fetch(`http://localhost:8000/api/kingdom/${division_slug}/${class_name_slug}`)
            .then(response => {
                console.log(response, 'response');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data, 'data'); // Логируем данные
                console.log(data.orderClass, 'data.orderClass' )

                setData(data);
            })
            .catch(error => console.error('Fetch error:', error));
    }, [division_slug, class_name_slug]);

    if (!data) return <div>Loading...</div>;

    return (
        <>
            <section>
                <h2>{data.name}</h2>
                <div className='types'>
                        <p>{data.descriptionBig}</p>
                </div>
            </section>
            <section>

                {data.orderClass && data.orderClass.length > 0 && (
                    <>
                        <h2>Порядки</h2>
                            {data.orderClass.map(ord => (
                                <Link key={ord.slug} to={ord.slug}>{ord.name}</Link>
                            ))}
                    </>
                )}
            </section>
        </>
    );
}

export default DescriptionClassName;
