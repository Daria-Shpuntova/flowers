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

function App() {

  const [count, setCount] = useState(0)
  const { slug } = useParams();


  return (
    <Router>
      <Routes>
        <Route path="" element={<HomePage />} />
        <Route path='/api/kingdom/:slug' element={<DetailyDivision url='http://localhost:8000/api/kingdom' />} />
        <Route path='/api/kingdom/:division_slug/:class_name_slug' element={<DetailyClassName url='http://localhost:8000/api/kingdom' />} />
      </Routes>
    </Router>
  )
}

export default App
