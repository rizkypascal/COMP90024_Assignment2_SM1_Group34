import React, { useState, useEffect } from 'react';
import Navbar from './Navbar';
import Home from './Home';


function App() {
  const [lgaData, setLgaData] = useState([{}])
  const [lgaNames, setLgaNames] = useState([{}]);
  const [lgaCodes, setLgaCodes] = useState([{}]);

  useEffect(() => {
    fetch("/api/lgas", { "methods": "GET", headers: { "Content-Type": "application/json" } }).then(
      res => res.json()
    ).then(
      data => {
        console.log(data)
        setLgaNames(data.lgaNames)
        setLgaCodes(data.lgaCodes)
        console.log(lgaNames)
        console.log(lgaCodes)
      }
    ).catch(error => console.log(error))
  }, [])
  return (
    // Checking if members array is equal to undefined or not - if so, it means APi is being fetched
    // Otherwise it has been fetched and will display members one by one
    <div className="App">
      <Navbar />

      <div className="content">

        {/* <h1>COMP90024 Assignment 2</h1> */}

        <Home lgaNames={lgaNames} lgaCodes={lgaCodes} />

      </div>
      {/* {(typeof data.data === "undefined") ? (
        <p>Loading...</p>
      ) : (
        data.data.map((data, i) => (
          <p key={i}>{data}</p>
        ))
      )} */}

    </div>
  )
}

export default App