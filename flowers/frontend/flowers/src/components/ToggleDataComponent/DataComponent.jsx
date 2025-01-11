import React from 'react';
import ToggleDataComponent from './ToggleDataComponent';
import './DataComponent.css'

const DataComponent = () => {
    return (
        <section className='toggleData'>
            <ToggleDataComponent apiUrl="http://localhost:8000/api/divisionHome" lastSlug='slug' buttonText="Показать отделы" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/classNameHome" lastSlug='slug' buttonText="Показать классы" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/ordersHome" lastSlug='slug' buttonText="Показать порядки" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/familyHome" lastSlug='slug' buttonText="Показать семейства" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/genusHome" lastSlug='slug' buttonText="Показать рода" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/speciesHome" lastSlug='species_slug' buttonText="Показать виды" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/subspeciesHome" lastSlug='subspecies_slug' buttonText="Показать подвиды" />
            <ToggleDataComponent apiUrl="http://localhost:8000/api/sortHome" lastSlug='sort_slug' buttonText="Показать сорта" />
        </section>
    );
};

export default DataComponent;
