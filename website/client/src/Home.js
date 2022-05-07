
import LgaData from './LgaData';
const Home = ({ lgaNames, lgaCodes, lgaGeoJSON }) => {


    return (
        <div className="home">

            <h1 className="h1">AURIN Language Data Versus Census Language Data</h1>

            <LgaData lgaNames={lgaNames} lgaCodes={lgaCodes} geoJSONData={lgaGeoJSON} />
        </div >
    )
}

export default Home;