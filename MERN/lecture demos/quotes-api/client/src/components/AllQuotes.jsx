import React, {useState, useEffect} from 'react';
import axios from 'axios';
import {Link} from '@reach/router';
import moment from 'moment'

const AllQuotes = () => {
    const [quotes, setQuotes] = useState([])
    // const [deleteClicked, setDeleteClicked] = useState(0)
    const [deleteClicked, setDeleteClicked] = useState(false)

    useEffect(() => {
        axios.get("http://localhost:8000/api/quotes")
        .then(res => {
            console.log("********")
            console.log(res)
            console.log("********")
            setQuotes(res.data.results)
            })
            .catch(err => {
                console.log(err)
            })

    }, [deleteClicked])

    // const [sortedInfo, setSortedInfo] = useState({});

    // // }

    const deleteButtonClickHandler = (event, deleteQuoteId) => {
        axios.delete(`http://localhost:8000/api/quotes/delete/${deleteQuoteId}`)
        .then(res => {
            console.log("********")
            console.log(res)
            console.log("********")
            setDeleteClicked(!deleteClicked) // (deleteCLicked +1)
            // navigate("/")
        })
        .catch(err => {
            console.log(err)
        })
    }

    

    return (
        <div className="container w-50">
            <br />
            {
            quotes.map((quote,i) => {
                return <div key={i} className="card">
                <div className="card-body">
                    <h3><img src= ""></img></h3>
                    <hr />
                    <h4 className="card-title">* {quote.author} *</h4>
                    <hr />
                    <p className="card-text">
                    "{quote.content}"
                    </p>
                    <h6 className="card-subtitle mb-2 text-muted">{moment(quote.quotedOn).add(2, 'd').format("MM-DD-YYYY")}</h6>
                    <br />
                    <Link to = {`/quotes/${quote._id}`} className="card-link" >- View Details -</Link> &nbsp; &nbsp;| |
                    <Link onClick={(event) => deleteButtonClickHandler(event, quote._id)} to = "#!" className = "card-link text-danger">- Delete -</Link> &nbsp; &nbsp; | |
                    <hr />
                    </div>
                </div>
            })
            }
        </div>
    );
};


export default AllQuotes;