import React, { useState } from 'react';
import {Link} from "react-router-dom";

const generateSlugPath = (item) => {
    const slugs = [];
    if (item.division) slugs.push(item.division.slug);
    if (item.className) slugs.push(item.className.slug);
    if (item.order) slugs.push(item.order.slug);
    if (item.family) slugs.push(item.family.slug);
    if (item.genus) slugs.push(item.genus.slug);
    if (item.species) slugs.push(item.species.slug);
    if (item.subspecies) slugs.push(item.subspecies.slug);
    slugs.push(item.slug); // Добавляем текущий элемент
    return `/${slugs.join('/')}`; // Формируем полный путь
};

const generateSlug = (item) => {
    const slugs = [
        item.division_slug,
        item.class_name_slug ? item.class_name_slug : null,
        item.order_slug,
        item.family_slug,
        item.genus_slug,
        item.species_slug,
        item.subspecies_slug ? item.subspecies_slug : null,
        item.slug,
    ].filter(Boolean); // Убираем все значения, которые равны null или undefined

    return `api/kingdom/${slugs.join('/')}`; // Объединяем оставшиеся слаги в строку
};


const ToggleDataComponent = ({ apiUrl, buttonText }) => {
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

                                <Link to={generateSlug(item)}>{item.name}</Link>
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
