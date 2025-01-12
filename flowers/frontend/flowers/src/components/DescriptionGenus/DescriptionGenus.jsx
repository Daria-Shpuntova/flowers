
import React, { useEffect, useState } from 'react';
import {Link, useParams} from 'react-router-dom';
import './DescriptionGenus.css'
import log from "eslint-plugin-react/lib/util/log.js";


const DescriptionGenus = () => {
    const { division_slug, class_name_slug, order_slug, family_slug, genus_slug } = useParams(); // Извлекаем оба slug'а
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch(`http://localhost:8000/api/kingdom/${division_slug}/${class_name_slug}/${order_slug}/${family_slug}/${genus_slug}`)
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
                <h2>Описание Рода</h2>
                <div className='types'>
                    <p>{data.descriptionBig}</p>
                </div>
            </section>
            <section>
                {data.species && data.species.length > 0 && (
                    <>
                        <h2>Виды</h2>
                        <div className='lists'>
                        {data.species.map(spec => (
                            <Link key={spec.slug} to={`/api/kingdom/${division_slug}/${class_name_slug}/${order_slug}/${family_slug}/${genus_slug}/species/${spec.slug}`}>{spec.name}</Link>
                        ))}
                        </div>
                    </>
                )}
            </section>
                {data.genusRose && data.genusRose.length > 0 && (
                    <section>
                        <h2>Типы роз</h2>
                        <div className='typeRoseS'>
                        {data.genusRose.map(gRose => (
                            <div className='typeRose'>
                                <div><img src={`http://127.0.0.1:8000/${gRose.image}`} alt={gRose.name}/></div>
                                <Link key={gRose.id} to={`type-rose/${gRose.id}`}>{gRose.name}</Link>
                            </div>
                        ))}
                        </div>
                    </section>
                )}
        </>
    );
}

export default DescriptionGenus;
