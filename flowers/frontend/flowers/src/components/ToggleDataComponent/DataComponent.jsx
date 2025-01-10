import React from 'react';
import ToggleDataComponent from './ToggleDataComponent';
import './DataComponent.css'

const DataComponent = () => {
    return (
        <section className='toggleData'>
            <ToggleDataComponent apiUrl="http://localhost:8000/api/divisionHome" buttonText="Показать отделы" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/classNameHome" buttonText="Показать классы" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/ordersHome" buttonText="Показать порядки" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/familyHome" buttonText="Показать семейства" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/genusHome" buttonText="Показать рода" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/speciesHome" buttonText="Показать виды" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/subspeciesHome" buttonText="Показать подвиды" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/sortHome" buttonText="Показать сорта" />
        </section>
    );
};

export default DataComponent;
