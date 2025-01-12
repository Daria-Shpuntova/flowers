import React, { useState } from 'react';
import {Link} from "react-router-dom";

const generateSlug = (item, lastSlug) => {
    const slugs = [
        item.division_slug,
        item.class_name_slug,
        item.order_slug,
        item.family_slug,
        item.genus_slug,
    ].filter(Boolean); // Убираем все значения, которые равны null или undefined

    if (lastSlug === 'species_slug') {
        slugs.push('species', item.slug);
    } else if (lastSlug === 'subspecies_slug') {
        slugs.push('species',item.species_slug, item.slug);
    } else if (lastSlug === 'sort_slug') {
        slugs.push('sort', item.slug);
    } else if (lastSlug === 'slug') {
        slugs.push(item.slug);
    }

    return `api/kingdom/${slugs.join('/')}`; // Объединяем оставшиеся слаги в строку
};



const ToggleDataComponent = ({ apiUrl,lastSlug, buttonText }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [data, setData] = useState([]);

    const toggleDiv = async () => {
        if (!isOpen) {
            // Загружаем данные только при открытии
            const response = await fetch(apiUrl);
            const result = await response.json();
            setData(result);
        }
        setIsOpen(!isOpen);
    };

    return (
        <>
            <button onClick={toggleDiv}>
                {isOpen ? 'Скрыть' : buttonText}
            </button>
            {isOpen && (
                <div className='lists' style={{transition: 'opacity 0.5s', opacity: isOpen ? 1 : 0}}>
                    {data.length > 0 ? (
                        data.map(item => (
                            <p key={item.slug}>
                                <Link to={generateSlug(item, lastSlug)}>{item.name}</Link>
                            </p>
                        ))
                    ) : (
                        <p>Загрузка...</p>
                    )}
                </div>
            )}
        </>
    );
};

export default ToggleDataComponent;
