import { useParams } from 'react-router-dom';
import Description from "./components/Description/Description.jsx";
import Header from "./components/Header/header.jsx";
import {useState} from "react";
import LastSpecies from "./components/Last/last.jsx";
import Footer from "./components/Footer/Footer.jsx";
import DescriptionClassName from "./components/DescriptionClassName/DescriptionClassName.jsx";

export default function DetailyClassName({url}) {
    const [count, setCount] = useState(0)
    const { division_slug, class_name_slug } = useParams();

    const newUrl = [url, division_slug, class_name_slug];

    return (
        <>
            <Header url={newUrl.join('/')} />
            <DescriptionClassName />
            <LastSpecies />
            <Footer />
        </>
    );
}
