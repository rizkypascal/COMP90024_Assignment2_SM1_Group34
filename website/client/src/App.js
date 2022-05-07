import React, { useState, useEffect } from 'react';
import Navbar from './Navbar';
import Home from './Home';

function App() {
  const [lgaData, setLgaData] = useState([[]])
  const [lgaNames, setLgaNames] = useState([[]]);
  const [lgaCodes, setLgaCodes] = useState([[]]);

  useEffect(() => {
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