import { Dropdown } from "react-bootstrap";
import { useState } from 'react';
import Collapsible from 'react-collapsible';
import { TileLayer, GeoJSON, MapContainer, Popup } from 'react-leaflet';
import { Icon } from 'leaflet';
import { AgGridReact } from 'ag-grid-react'; // the AG Grid React Component

import 'ag-grid-community/dist/styles/ag-grid.css'; // Core grid CSS, always needed
import 'ag-grid-community/dist/styles/ag-theme-alpine.css'; // Optional theme CSS

import 'leaflet/dist/leaflet.css';

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

const LgaData = ({ lgaNames, lgaCodes, geoJSONData }) => {


    const [aurinLgaData, setAurinLgaData] = useState([{ "name": "", "code": undefined, "tweet_languages": [] }])
    const [censusLanguageData, setCensusLanguageData] = useState([{ "data": [] }]);
    const [censusReligionData, setCensusReligionData] = useState([{}])
    const [censusAncestryData, setCensusAncestryData] = useState([{}])
    const [value, setValue] = useState('Please select an LGA.')
    const [languageColumns] = useState([
        { field: 'language', resizable: true, flex: 2 },
        { field: 'proportion', resizable: true, flex: 1 },])
    const [ancestryColumns] = useState([
        { field: 'ancestry', resizable: true, flex: 2 },
        { field: 'proportion', resizable: true, flex: 1 },])
    const [religionColumns] = useState([
        { field: 'religion', resizable: true, flex: 2 },
        { field: 'proportion', resizable: true, flex: 1 },])

    const handleSelect = (e, i) => {
        setValue(e)
        fetch("/api/twitter/all/lgas/" + lgaCodes[i], { "methods": "GET", headers: { "Content-Type": "application/json" } }).then(
            res => res.json()
        ).then(res => {
            setAurinLgaData(res.data)
        }).catch(err => console.log(err))
        fetch("/api/census/2016/lgas/" + lgaCodes[i] + "/language", { "methods": "GET", headers: { "Content-Type": "application/json" } }).then(
            res => res.json()
        ).then(res => {
            setCensusLanguageData(calcPercentage(res.data))
        }).catch(err => console.log(err))
        fetch("/api/census/2016/lgas/" + lgaCodes[i] + "/religion", { "methods": "GET", headers: { "Content-Type": "application/json" } }).then(
            res => res.json()
        ).then(res => {
            setCensusReligionData(calcPercentage(res.data))
        }).catch(err => console.log(err))
        fetch("/api/census/2016/lgas/" + lgaCodes[i] + "/ancestry", { "methods": "GET", headers: { "Content-Type": "application/json" } }).then(
            res => res.json()
        ).then(res => {
            setCensusAncestryData(calcPercentage(res.data))
        }).catch(err => console.log(err))
    }

    const calcPercentage = (input) => {
        for (let i = 0; i < input.length; i++) {
            input[i]['proportion'] = (parseFloat(input[i]['proportion']) * 100).toFixed(2).toString() + "%"
            console.log(input[i]['proportion'])
        }
        return input;

    }

    return (
        <div className="lgaData">
            <div className="lgaDataDropdown">
                {(typeof lgaNames === "undefined") ? (
                    <p>Loading...</p>
                ) : (<div className="dropdown">
                    <div className="map">
                        <script>{console.log(geoJSONData)}</script>
                        {(typeof geoJSONData === "undefined" || geoJSONData.length == 1) ? (
                            <div>
                                <p>Loading...</p>
                            </div>
                        ) : (
                            <div>
                                <script>{console.log(geoJSONData[0].geometry.coordinates)}</script>

                                <MapContainer center={[-37.840935, 144.946457]} zoom={10} scrollWheelZoom={false}>
                                    <TileLayer
                                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                                    />
                                    <div>
                                        {geoJSONData.map((data, i) => {
                                            return (<GeoJSON key={i} data={data} eventHandlers={{
                                                click: () => {
                                                    handleSelect(data.properties.lga_name_2016, i)
                                                }
                                            }} >
                                                <Popup>{data.properties.lga_name_2016}</Popup>
                                            </GeoJSON>)
                                        })}
                                    </div>
                                </MapContainer>
                            </div>
                        )}
                    </div >
                    <p></p>
                    <Dropdown>
                        <Dropdown.Toggle className="button" variant="success" id="dropdown-basic">
                            {value}
                        </Dropdown.Toggle>

                        <Dropdown.Menu variant="success">
                            {lgaNames.map((data, i) => {
                                return (<Dropdown.Item key={i} title={value} onClick={() => handleSelect(data, i)}
                                >{data}</Dropdown.Item>)
                            })}
                        </Dropdown.Menu>
                    </Dropdown>
                </div>)

                }
            </div>
            <div className="lgaDataDisplay">


                {(aurinLgaData.code === undefined) ? (
                    <div>
                        <p></p>
                        < p > Please select an LGA to view its data</p>
                    </div>
                ) : (
                    <div>
                        <p></p>
                        <h2 className="h2">{value}</h2>
                        <div className="languageData">
                            <div className="column">
                                <div>
                                    <h4 className="h4">Twitter Language Data</h4>
                                    <p className="LGACode">LGA Code: {aurinLgaData.code}</p>
                                    <p className="italics">Language: # Tweets Collected</p>
                                </div>

                                <div>{aurinLgaData.tweet_languages.map((data, k) => {
                                    return (
                                        <div>
                                            <p key={k}>
                                                {data.name}: '{data.code}' ----- {data.tweet_count}
                                            </p>
                                        </div>

                                    )
                                })}
                                </div>
                            </div>
                            <div className="column" key={2}>
                                <h4 className="h4">Census Data</h4>
                                <Collapsible trigger="Language: Proportion of First Language Speakers">
                                    <div>
                                        <p></p>
                                        <div>
                                            <div className="ag-theme-alpine" style={{ height: 400, width: 400 }}>
                                                <AgGridReact rowData={censusLanguageData} columnDefs={languageColumns}></AgGridReact>
                                            </div>
                                        </div>
                                    </div>
                                </Collapsible>
                                <p></p>
                                <Collapsible trigger="Ancestry">
                                    <p></p>
                                    <div>
                                        <div>
                                            <div className="ag-theme-alpine" style={{ height: 400, width: 400 }}>
                                                <AgGridReact rowData={censusAncestryData} columnDefs={ancestryColumns}></AgGridReact>
                                            </div>
                                        </div>
                                    </div>
                                </Collapsible>
                                <p></p>
                                <Collapsible trigger="Religion">
                                    <p></p>
                                    <div>
                                        <div>
                                            <div className="ag-theme-alpine" style={{ height: 400, width: 400 }}>
                                                <AgGridReact expandField="collapsed" rowData={censusReligionData} columnDefs={religionColumns}></AgGridReact>
                                            </div>
                                        </div>
                                    </div>
                                </Collapsible>
                            </div>
                        </div>
                    </div>

                )}
            </div>
        </div >

    );
}

export default LgaData;