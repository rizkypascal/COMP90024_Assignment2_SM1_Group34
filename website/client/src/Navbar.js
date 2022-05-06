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