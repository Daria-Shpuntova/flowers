import { useParams } from 'react-router-dom';
import Description from "./components/Description/Description.jsx";
import Header from "./components/Header/header.jsx";
import {useState} from "react";

export default function Detaily({url}) {
    const [count, setCount] = useState(0)
    const { slug } = useParams();
//
    const url3 = `http://localhost:8000/api/kingdom/${slug}`
    console.log(slug, 'slug2');
    console.log(url, 'url')

    console.log(url3, 'url3')

    const newUrl = [url, slug]

    console.log(newUrl.join('/'))

    return (
        <>
            <Header url={newUrl.join('/')} />
            <Description />
        </>
    );
}
