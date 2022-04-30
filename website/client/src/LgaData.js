import { Dropdown } from "react-bootstrap";
import { useState } from 'react';
const LgaData = ({ data }) => {
    const [dataFromLga, setDataFromLga] = useState([""])
    const [value, setValue] = useState('Please select an LGA.')

    const handleSelect = (e) => {
        setValue(e)
        setDataFromLga(e)
        //     return (
        //         <p>{data2}</p>
        //     )
        // fetch("/place/#/" + data2, { "methods": "GET", headers: { "Content-Type": "application/json" } }).then(
        //     res => res.json()
        // ).then(res => setDataFromLga(res)
        // ).catch(err => console.log(err))
    }
    return (
        <div className="lgaData">
            <div className="lgaDataDropdown">
                {(typeof data.data === "undefined") ? (
                    <p>Loading...</p>
                ) : (<div className="dropdown">
                    <Dropdown>
                        <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                            {value}
                        </Dropdown.Toggle>

                        <Dropdown.Menu>
                            {data.data.map((data, i) => {
                                return (<Dropdown.Item key={i} eventKey={"option-" + i} title={value} onClick={() => handleSelect(data)}
                                >{data}</Dropdown.Item>)
                            })}
                        </Dropdown.Menu>
                    </Dropdown>
                </div>)

                }
                {/* {props.data.data.map(d => {
                return (
                    <div key={d._id}>
                        <h2 className="tweetText"> {d.text}</h2>
                        <p> {d.user}</p>
                        <hr />
                    </div>
                )
            })} */}
            </div>
            <div className="lgaDataDisplay">


                {(dataFromLga == "" ? (
                    <div>
                        <p></p>
                        < p > Please select an LGA to view its data</p>
                    </div>
                ) : (
                    <div><p></p><h2>{value}</h2><div><p>{dataFromLga}</p></div></div>
                )
                )}
            </div>
        </div >

    );
}

export default LgaData;