/*
  COMP90024 - Group 34 - Semester 1 2022:
  - Juny Kesumadewi (197751); Melbourne, Australia
  - Georgia Lewis (982172); Melbourne, Australia
  - Vilberto Noerjanto (553926); Melbourne, Australia
  - Matilda O’Connell (910394); Melbourne, Australia
  - Rizky Totong (1139981); Melbourne, Australia
*/

import React, { useState, useEffect } from 'react';
import Navbar from './Navbar';
import Home from './Home';

function App() {
  const [lgaData, setLgaData] = useState([[]])
  const [lgaNames, setLgaNames] = useState([[]]);
  const [lgaCodes, setLgaCodes] = useState([[]]);

  useEffect(() => {

    document.title = "Cultural & Language Diversity in Victoria"
    fetch("/api/lgas?compact=true", { "methods": "GET", headers: { "Content-Type": "application/json" } }).then(
      res => res.json()
    ).then(
      data => {
        setLgaNames(data.lgaNames)
        setLgaCodes(data.lgaCodes)
      }
    ).catch(error => console.log(error))
    fetch("/api/lgas", { "methods": "GET", headers: { "Content-Type": "application/json" } }).then(
      res => res.json()
    ).then(
      data => {
        setLgaData(data.lgaDetails)
      }
    ).catch(error => console.log(error))
  }, [])
  return (
    <div className="App">
      <Navbar />

      <div className="content">
        <Home lgaNames={lgaNames} lgaCodes={lgaCodes} lgaGeoJSON={lgaData} />

      </div>

    </div>
  )
}

export default App