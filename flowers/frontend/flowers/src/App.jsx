import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'


import Header from "./components/Header/header.jsx";
import Types from "./components/Types/types.jsx";
import LastSpecies from "./components/Last/last.jsx";
import DataComponent from "./components/ToggleDataComponent/DataComponent.jsx";
import CharacteristicsKingdom from './components/CharacteristicsKingdom/CharacteristicsKingdom.jsx'
import Footer from "./components/Footer/Footer.jsx";

import { useState } from 'react'
import {BrowserRouter as Router, Routes, Route, useLocation, useParams} from 'react-router-dom';

import HomePage from "./HomePage.jsx";
import './App.css'
import DetailyDivision from "./DetailyDivision.jsx";
import DetailyClassName from "./DetailyClassName.jsx";
import DetailyOrder from "./DetailyOrder.jsx";
import DetailyFamily from './DetailyFamily.jsx'
import DetailyGenus from "./DetailyGenus.jsx";
import DetailyTypeRose from "./DetailyTypeRose.jsx";
import DetailySpecies from "./DetailySpecies.jsx";
import DetailySubspecies from "./DetailySubspecies.jsx";
import DetailySort from "./DetailySort.jsx";

function App() {

  const [count, setCount] = useState(0)
  const { slug } = useParams();


  return (
    <Router>
      <Routes>
        <Route path="" element={<HomePage />} />
        <Route path='/api/kingdom/:slug' element={<DetailyDivision url='http://localhost:8000/api/kingdom' />} />
        <Route path='/api/kingdom/:division_slug/:class_name_slug' element={<DetailyClassName url='http://localhost:8000/api/kingdom' />} />
        <Route path='/api/kingdom/:division_slug/:class_name_slug/:order_slug' element={<DetailyOrder url='http://localhost:8000/api/kingdom' />} />
        <Route path='/api/kingdom/:division_slug/:class_name_slug/:order_slug/:family_slug' element={<DetailyFamily url='http://localhost:8000/api/kingdom' />} />
        <Route path='/api/kingdom/:division_slug/:class_name_slug/:order_slug/:family_slug/:genus_slug' element={<DetailyGenus url='http://localhost:8000/api/kingdom' />} />
        <Route path='/api/kingdom/:division_slug/:class_name_slug/:order_slug/:family_slug/:genus_slug/type-rose/:id' element={<DetailyTypeRose url='http://localhost:8000/api/kingdom' />} />
        <Route path='/api/kingdom/:division_slug/:class_name_slug/:order_slug/:family_slug/:genus_slug/species/:species_slug' element={<DetailySpecies url='http://localhost:8000/api/kingdom' />} />
        <Route path='/api/kingdom/:division_slug/:class_name_slug/:order_slug/:family_slug/:genus_slug/species/:species_slug/:subspecies_slug' element={<DetailySubspecies url='http://localhost:8000/api/kingdom' />} />
        <Route path='/api/kingdom/:division_slug/:class_name_slug/:order_slug/:family_slug/:genus_slug/sort/:sort_slug' element={<DetailySort url='http://localhost:8000/api/kingdom' />} />

      </Routes>
    </Router>
  )
}

export default App
