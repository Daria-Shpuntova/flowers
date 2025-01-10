import { useParams } from 'react-router-dom';
import Description from "./components/Description/Description.jsx";
import Header from "./components/Header/header.jsx";
import {useState} from "react";
import LastSpecies from "./components/Last/last.jsx";
import Footer from "./components/Footer/Footer.jsx";

export default function DetailyDivision({url}) {
    const [count, setCount] = useState(0)
    const { slug } = useParams();

    const newUrl = [url, slug]

    return (
        <>
            <Header url={newUrl.join('/')} />
            <Description />
            <LastSpecies />
            <Footer />
        </>
    );
}
