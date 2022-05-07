
import { TileLayer, GeoJSON, MapContainer } from 'react-leaflet';
import { Icon } from 'leaflet';

import 'leaflet/dist/leaflet.css';

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

const Map = ({ geoJSONData }) => {


    console.log(geoJSONData)
    return (


        <div className="map">
            {(geoJSONData.length == 1) ? (
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
                                        console.log(data.properties.lga_name_2016)
                                    }
                                }} />)
                            })}
                        </div>
                        {/* <Marker position={[-37.840935, 144.946457]}>
                            <Popup>
                                A pretty CSS3 popup. <br /> Easily customizable.
                            </Popup>
                        </Marker> */}
                    </MapContainer>
                </div>
            )}
        </div >
    )
}

export default Map;