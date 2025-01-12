

import React, { useEffect, useState } from 'react';
import {Link, useParams} from 'react-router-dom';

import log from "eslint-plugin-react/lib/util/log.js";


const DescriptionTypeRose = () => {
    const { division_slug, class_name_slug, order_slug, family_slug, genus_slug, id } = useParams();
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch(`http://localhost:8000/api/kingdom/${division_slug}/${class_name_slug}/${order_slug}/${family_slug}/${genus_slug}/type-rose/${id}`)
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
    }, [id]);

    if (!data) return <div>Loading...</div>;

    return (
        <>
            <section>
                <h2>Описание типа роз</h2>
                <div className='types'>
                    <p>{data.descriptionBig}</p>
                </div>
            </section>
            <section>
                {data.speciesRose && data.speciesRose.length > 0 && (
                    <>
                        <h2>Виды</h2>
                        {data.speciesRose.map(spec => (
                            <Link key={spec.slug} to={`/api/kingdom/с${order_slug}/${family_slug}/${genus_slug}/species/${spec.slug}`}>{spec.name}</Link>
                        ))}
                    </>
                )}
            </section>
        </>
    );
}

export default DescriptionTypeRose;
