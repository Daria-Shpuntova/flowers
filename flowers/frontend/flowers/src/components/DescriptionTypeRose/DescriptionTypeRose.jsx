

import React, { useEffect, useState } from 'react';
import {Link, useParams} from 'react-router-dom';

import log from "eslint-plugin-react/lib/util/log.js";


const DescriptionTypeRose = () => {
    const { division_slug, class_name_slug, order_slug, family_slug, genus_slug, id } = useParams();
    const [data, setData] = useState(null);

    useEffect(() => {
        console.log(`http://localhost:8000/api/kingdom/${division_slug}/${class_name_slug}/${order_slug}/${family_slug}/${genus_slug}/${id}`);
        fetch(`http://localhost:8000/api/kingdom/${division_slug}/${class_name_slug}/${order_slug}/${family_slug}/${genus_slug}/${id}`)
            .then(response => {
                console.log(response, 'response');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data, 'data'); // Логируем данные

                setData(data);
            })
            .catch(error => console.error('Fetch error:', error));
    }, [id]);

    if (!data) return <div>Loading...</div>;

    return (
        <>
            <section>
                <h2>Описание типа роз</h2>
                <div className='types'>
                    <p>{data.description}</p>
                </div>
            </section>
            <section>

                {data.speciesRose && data.speciesRose.length > 0 && (
                    <>
                        <h2>Виды</h2>
                        {data.speciesRose.map(spec => (
                            <Link key={spec.slug} to={spec.slug}>{spec.name}</Link>
                        ))}
                    </>
                )}
            </section>
        </>
    );
}

export default DescriptionTypeRose;
