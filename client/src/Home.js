import { useState, useEffect } from 'react';
import LgaData from './LgaData';
const Home = ({ data }) => {
    // let name = 'mario';
    const [name, setName] = useState('mario');
    const [age, setAge] = useState(25);
    const handleClick = (e) => {
        setName('luigi');
        setAge(30);
        // name = 'luigi'
        console.log('hello, ninjas', e)
    }

    const [blogs, setBlogs] = useState([
        { title: 'My new website', body: 'lorem ipsum...', author: 'mario', id: 1 },
        { title: 'Welcome party!', body: 'lorem ipsum...', author: 'yoshi', id: 2 },
        { title: 'Web dev top tips', body: 'lorem ipsum...', author: 'mario', id: 3 }
    ])

    const handleDelete = (id) => {
        const newBlogs = blogs.filter(blog => blog.id !== id)
        setBlogs(newBlogs)
    }


    useEffect(() => {
        console.log('useEffect ran')
    }, [name]);

    // const handleClickAgain = (name, e) => {
    //     console.log('hello ' + name, e.target)
    // }

    return (
        <div className="home">

            <h1>AURIN Language Data Versus Census Language Data</h1>
            <LgaData data={data} />
            {/* map method cycles through each item in an array */}
            {/* <BlogList blogs={blogs} title="All Blogs!" handleDelete={handleDelete} />
            <button onClick={() => setName('luigi')}>Change name</button>
            <p>{name}</p> */}

            {/* <BlogList blogs={blogs.filter((blog) => blog.author === 'mario')} title="Mario's Blogs!"/> */}

            {/* <h2>Home Page</h2>

            <div className="dropdown">
                <Dropdown>
                    <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                        Dropdown Button
                    </Dropdown.Toggle>

                    <Dropdown.Menu>
                        <Dropdown.Item as="button">Action</Dropdown.Item>
                        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
            </div>
            <p>{name} is {age} years old.</p><button onClick={handleClick}>Click Me </button>
            <button onClick={(e) => handleClickAgain('mario', e)}>Click me again</button> */}
        </div >
    )
}

export default Home;