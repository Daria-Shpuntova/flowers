import { useParams } from 'react-router-dom';
import Header from "./components/Header/header.jsx";
import {useState} from "react";
import LastSpecies from "./components/Last/last.jsx";
import Footer from "./components/Footer/Footer.jsx";

import DescriptionSort from "./components/DescriptionSort/DescriptionSort.jsx";

export default function DetailySort({url}) {
    const [count, setCount] = useState(0)
    const { division_slug, class_name_slug, order_slug, family_slug, genus_slug, sort_slug } = useParams();


    const newUrl = `${url}/${division_slug}/${class_name_slug}/${order_slug}/${family_slug}/${genus_slug}/sort/${sort_slug}`;
    console.log(newUrl, 'newUrl')

    return (
        <>
            <Header url={newUrl} />
            <DescriptionSort />
            <LastSpecies />
            <Footer />
        </>
    );
}
