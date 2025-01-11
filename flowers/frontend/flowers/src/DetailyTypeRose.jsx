
import { useParams } from 'react-router-dom';
import Description from "./components/Description/Description.jsx";
import Header from "./components/Header/header.jsx";
import {useState} from "react";
import LastSpecies from "./components/Last/last.jsx";
import Footer from "./components/Footer/Footer.jsx";

import DescriptionTypeRose from "./components/DescriptionTypeRose/DescriptionTypeRose.jsx";

export default function DetailyTypeRose({url}) {
    const [count, setCount] = useState(0)
    const { division_slug, class_name_slug, order_slug, family_slug, genus_slug, id } = useParams();

    console.log(id, 'idd')


    const newUrl = [url, division_slug, class_name_slug, order_slug, family_slug, genus_slug, id];
    console.log(newUrl, 'newUrl')

    return (
        <>
            <Header url={newUrl.join('/')} />
            <DescriptionTypeRose />
            <LastSpecies />
            <Footer />
        </>
    );
}
