import React, { useState, useEffect } from 'react';

function App() {

  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  return (
    // Checking if members array is equal to undefined or not - if so, it means APi is being fetched
    // Otherwise it has been fetched and will display members one by one
    <div>
      <h1>COMP90024 Assignment 2</h1>

      {(typeof data.members === "undefined") ? (
        <p>Loading...</p>
      ) : (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}

    </div>
  )
}

export default App