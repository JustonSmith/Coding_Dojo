import React, {useState, useEffect} from 'react';
import axios from 'axios'
// import styling from './components/News.Module.css'


const News = () => {

    const [allArticles, setAllArticles] = useState([])
    // useEffect is saying "upon load of the page, run this code inside of the useEffect function on time"
    useEffect(() => {
    }, [])
    
    const getArticles = ()=> {

        // fetch method:

        // fetch("https://newsapi.org/v2/top-headlines?country=us&apiKey=aef11bf23736484f9883f9f541ffdefe&category=technology")
        // .then(res => {
        //     return res.json()
        // })
        // .then(res => {
        //     console.log("******")
        //     console.log(res.articles)
        //         setAllArticles(res.articles)
        // })
        // .catch(err => console.log("error", err))

        axios.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=aef11bf23736484f9883f9f541ffdefe&category=technology")
        .then(res => {
            console.log (res)
            setAllArticles(res.data.articles)
        })
        .catch(err => {
            console.log(err)
        })
    }
    
    console.log("logging response outside of the fetch.")
    return (
        <div>
            <br />
            <button onClick= {getArticles} className="btn btn-primary">Click here to get today's tech news</button>
            <br />
            <h1>Here's the tech news for today:</h1>
            {
                allArticles.map( (article, id) =>  {
                    return <div key={id} className="card">
                        <img src={article.urlToImage} alt="" height="200px" width= "300" className="text-align-center" />
                        <div className="card-body">
                            <h5 className="card-title">{article.title}</h5>
                            <p className="card-text">{article.description? article.description: "no description available"}</p>
                            <p >Source: {article.source.name}</p>
                            <a href={article.url} className="btn btn-primary">Check it out</a>
                        </div>
                    </div>
                    })
                }
        </div>
    );
};

export default News;