import { Dropdown } from "react-bootstrap";
import { useState } from 'react';
const LgaData = ({ lgaNames, lgaCodes }) => {
    const [aurinLgaData, setAurinLgaData] = useState([{ "name": "", "code": undefined, "tweet_languages": [] }])
    const [censusLgaData, setCensusLgaData] = useState([{ "data": [] }]);
    const [value, setValue] = useState('Please select an LGA.')

    const handleSelect = (e, i) => {
        setValue(e)
        //     return (
        //         <p>{data2}</p>
        //     )
        fetch("/api/lgas/" + lgaCodes[i], { "methods": "GET", headers: { "Content-Type": "application/json" } }).then(
            res => res.json()
        ).then(res => {
            setAurinLgaData(res.data)
        }
        ).catch(err => console.log(err))
        fetch("/api/census/2016/lgas/" + lgaCodes[i] + "/languages", { "methods": "GET", headers: { "Content-Type": "application/json" } }).then(
            res => res.json()
        ).then(res => {
            setCensusLgaData(res.data)
        }
        ).catch(err => console.log(err))
    }
    return (
        <div className="lgaData">
            <div className="lgaDataDropdown">
                {(typeof lgaNames === "undefined") ? (
                    <p>Loading...</p>
                ) : (<div className="dropdown">
                    <Dropdown>
                        <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                            {value}
                        </Dropdown.Toggle>

                        <Dropdown.Menu>
                            {lgaNames.map((data, i) => {
                                return (<Dropdown.Item key={i} eventKey={"option-" + i} title={value} onClick={() => handleSelect(data, i)}
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


                {(aurinLgaData.code == undefined ? (
                    <div>
                        <p></p>
                        < p > Please select an LGA to view its data</p>
                    </div>
                ) : (
                    <div>
                        <p></p>
                        <h2>{value}</h2>
                        <div className="languageData">
                            <div className="column">
                                <div>
                                    <h4>Twitter Language Data</h4>
                                </div>
                                <div>
                                    <p>LGA Code: {aurinLgaData.code}</p>
                                    <p className="italics">
                                        Language: # Tweets Collected
                                    </p>
                                </div>


                                <div>{aurinLgaData.tweet_languages.map((data, i) => {
                                    return (
                                        <div>
                                            <p key={i}>
                                                {data.name}: '{data.code}' ----- {data.tweet_count}
                                            </p>
                                        </div>

                                    )
                                })}
                                </div>
                            </div>
                            <div className="column">
                                <h4>Census Data</h4>
                                <p className="italics">
                                    Language: Proportion of First Language Speakers
                                </p>
                                <div className="column">{censusLgaData.map((data, j) => {
                                    return (
                                        <div>
                                            <p key={j}>
                                                {data.language}:  {data.proportion}                                            </p>
                                        </div>

                                    )
                                })}
                                </div>
                            </div>
                        </div>
                    </div>
                )
                )}
            </div>
        </div >

    );
}

export default LgaData;