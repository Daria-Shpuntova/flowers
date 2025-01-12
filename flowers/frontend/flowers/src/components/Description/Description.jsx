import React, { useEffect, useState } from 'react';
import {Link, useParams} from 'react-router-dom';
import './Description.css'
import log from "eslint-plugin-react/lib/util/log.js";


const Description = () => {
    const { slug } = useParams();
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch(`http://localhost:8000/api/kingdom/${slug}`)
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
    }, [slug]);

    if (!data) return <div>Loading...</div>;

    return (
        <>
            <section>
                <h2>Описание Отдела</h2>
                <div className='types'>
                        <p>{data.descriptionBig}</p>
                </div>
            </section>
            <section>
                {data.classes && data.classes.length > 0 && (
                    <>
                        <h2>Классы</h2>
                        <div className='lists'>
                            {data.classes.map(cls => (
                                <Link key={cls.slug} to={cls.slug}>{cls.name}</Link>
                            ))}
                        </div>
                    </>
                )}
                {data.classes && data.classes.length === 0 && data.orders && data.orders.length > 0 && (
                    <>
                        <h2>Порядки</h2>
                        <div className='lists'>
                            {data.orders.map(order => (
                                <Link key={order.slug} to={order.slug}>{order.name}</Link>
                            ))}
                        </div>
                        </>
                        )}
                    </section>
                    </>
                    );
                }

                export default Description;
