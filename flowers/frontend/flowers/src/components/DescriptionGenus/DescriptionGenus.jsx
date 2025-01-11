
import React, { useEffect, useState } from 'react';
import {Link, useParams} from 'react-router-dom';

import log from "eslint-plugin-react/lib/util/log.js";


const DescriptionGenus = () => {
    const { division_slug, class_name_slug, order_slug, family_slug, genus_slug } = useParams(); // Извлекаем оба slug'а
    const [data, setData] = useState(null);

    useEffect(() => {
        console.log(`http://localhost:8000/api/kingdom/${division_slug}/${class_name_slug}/${order_slug}/${family_slug}/${genus_slug}`);
        fetch(`http://localhost:8000/api/kingdom/${division_slug}/${class_name_slug}/${order_slug}/${family_slug}/${genus_slug}`)
            .then(response => {
                console.log(response, 'response');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data, 'data'); // Логируем данные
                console.log(data.genus, 'data.genus' )
                setData(data);
            })
            .catch(error => console.error('Fetch error:', error));
    }, [division_slug, class_name_slug]);

    if (!data) return <div>Loading...</div>;

    return (
        <>
            <section>
                <h2>Описание Рода</h2>
                <div className='types'>
                        <p>{data.descriptionBig}</p>
                </div>
            </section>
            <section>

                {data.species && data.species.length > 0 && (
                    <>
                        <h2>Виды</h2>
                            {data.species.map(spec => (
                                <Link key={spec.slug} to={spec.slug}>{spec.name}</Link>
                            ))}
                    </>
                )}
            </section>
        </>
    );
}

export default DescriptionGenus;
