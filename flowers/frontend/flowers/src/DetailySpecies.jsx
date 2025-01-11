import { useParams } from 'react-router-dom';
import Header from "./components/Header/header.jsx";
import {useState} from "react";
import LastSpecies from "./components/Last/last.jsx";
import Footer from "./components/Footer/Footer.jsx";

import DescriptionSpecies from "./components/DescriptionSpecies/DescriptionSpecies.jsx";

export default function DetailySpecies({url}) {
    const [count, setCount] = useState(0)
    const { division_slug, class_name_slug, order_slug, family_slug, genus_slug, species_slug } = useParams();


    const newUrl = `${url}/${division_slug}/${class_name_slug}/${order_slug}/${family_slug}/${genus_slug}/species/${species_slug}`;
    console.log(newUrl, 'newUrl')

    return (
        <>
            <Header url={newUrl} />
            <DescriptionSpecies />
            <LastSpecies />
            <Footer />
        </>
    );
}
