import { useParams } from 'react-router-dom';

import Header from "./components/Header/header.jsx";
import {useState} from "react";
import LastSpecies from "./components/Last/last.jsx";
import Footer from "./components/Footer/Footer.jsx";

import DescriptionGenus from "./components/DescriptionGenus/DescriptionGenus.jsx";

export default function DetailyGenus({url}) {
    const [count, setCount] = useState(0)
    const { division_slug, class_name_slug, order_slug, family_slug , genus_slug} = useParams();

    const newUrl = [url, division_slug, class_name_slug, order_slug, family_slug, genus_slug];
    console.log(newUrl, 'newUrl')


    return (
        <>
            <Header url={newUrl.join('/')} />
            <DescriptionGenus />
            <LastSpecies />
            <Footer />
        </>
    );
}
