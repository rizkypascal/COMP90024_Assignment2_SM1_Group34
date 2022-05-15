/*
    COMP90024 - Group 34 - Semester 1 2022:
    - Juny Kesumadewi (197751); Melbourne, Australia
    - Georgia Lewis (982172); Melbourne, Australia
    - Vilberto Noerjanto (553926); Melbourne, Australia
    - Matilda O’Connell (910394); Melbourne, Australia
    - Rizky Totong (1139981); Melbourne, Australia
*/

import LgaData from './LgaData';
const Home = ({ lgaNames, lgaCodes, lgaGeoJSON }) => {


    return (
        <div className="home">

            <h1 className="h1">Cultural and Language Diversity In Melbourne</h1>

            <LgaData lgaNames={lgaNames} lgaCodes={lgaCodes} geoJSONData={lgaGeoJSON} />
        </div >
    )
}

export default Home;