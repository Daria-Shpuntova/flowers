import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const Description = () => {
    const { slug } = useParams();
    const [data, setData] = useState(null);

    useEffect(() => {
        console.log(`http://localhost:8000/api/kingdom/${slug}`);
        fetch(`http://localhost:8000/api/kingdom/${slug}`)
            .then(response => {
                console.log(response, 'response');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data, 'data'); // Логируем данные
                setData(data);
            })
            .catch(error => console.error('Fetch error:', error));
    }, [slug]);

    if (!data) return <div>Loading...</div>;

    return (
        <section>
            <h2>{data.name}</h2>
            <p>{data.descriptionBig}</p>
            <img src={data.image} alt={data.name} />
        </section>
    );
}

export default Description;
