import { useState } from 'react'
import Header from "./components/Header/header.jsx";
import Types from "./components/Types/types.jsx";
import LastSpecies from "./components/Last/last.jsx";
import DataComponent from "./components/ToggleDataComponent/DataComponent.jsx";
import CharacteristicsKingdom from './components/CharacteristicsKingdom/CharacteristicsKingdom.jsx'
import Footer from "./components/Footer/Footer.jsx";


function HomePage() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Header url='http://localhost:8000/api/kingdom' />
      <Types />
      <LastSpecies />
      <DataComponent />
      <CharacteristicsKingdom />
      <Footer />
    </>
  )
}

export default HomePage