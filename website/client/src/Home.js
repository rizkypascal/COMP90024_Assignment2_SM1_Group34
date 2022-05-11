
import LgaData from './LgaData';
const Home = ({ lgaNames, lgaCodes, lgaGeoJSON }) => {


    return (
        <div className="home">

            <h1 className="h1">Cultural and Language Diversity In Victoria</h1>

            <LgaData lgaNames={lgaNames} lgaCodes={lgaCodes} geoJSONData={lgaGeoJSON} />
        </div >
    )
}

export default Home;