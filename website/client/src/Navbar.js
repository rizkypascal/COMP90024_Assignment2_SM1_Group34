/*
    COMP90024 - Group 34 - Semester 1 2022:
    - Juny Kesumadewi (197751); Melbourne, Australia
    - Georgia Lewis (982172); Melbourne, Australia
    - Vilberto Noerjanto (553926); Melbourne, Australia
    - Matilda O’Connell (910394); Melbourne, Australia
    - Rizky Totong (1139981); Melbourne, Australia
*/

const Navbar = () => {
    return (
        <nav className="navbar">
            <h1>COMP90024 Team 34 </h1>
            <div className="links">
                <a href='/'>Refresh</a>
                {/* <a href='/create' style={{
                    color: "white",
                    backgroundColor: '#f1356d',
                    borderRadius: '8px'
                }}>New blog</a> */}
            </div>
        </nav>
    );
}

export default Navbar;