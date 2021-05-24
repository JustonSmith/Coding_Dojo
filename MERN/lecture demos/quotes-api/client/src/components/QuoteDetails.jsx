import React, {useState, useEffect} from 'react';
import axios from 'axios';
import {navigate, Link} from '@reach/router';
import moment from 'moment'

const QuoteDetails = (props, _id) => {
    const [quoteInfo, setQuoteInfo] = useState({})


    useEffect(() => {
        axios.get(`http://localhost:8000/api/quotes/${props._id}`)
        .then(res => {
            console.log(res)
            setQuoteInfo(res.data.results)
        })
        .catch(err => console.log(err))
    }, [])

    const deleteButtonClickHandler = () => {
        axios.delete(`http://localhost:8000/api/quotes/delete/${props._id}`)
        .then(res => {
            console.log("********")
            console.log(res)
            console.log("********")
            navigate("/")
        })
        .catch(err => {
            console.log(err)
        })
    }

    return (
        <div className= "container w-50">
            <hr />
            <h3>- Quote Details -</h3>
            {props._id}
            <hr />
            <h4>* {quoteInfo.author} *</h4>
            <br />
            <p>"{quoteInfo.content}"</p>
            <p>{moment(quoteInfo.quotedOn).add(2, 'd').format("MM-DD-YYYY")}</p>
            <br />
            <button onClick= {deleteButtonClickHandler} className= "btn btn-danger">Delete Quote</button> &nbsp;| |
            &nbsp;<Link to={`/quotes/edit/${quoteInfo._id}`}><button className= "btn btn-warning">Edit Quote</button></Link>
            <hr />
        </div>
    );
};



export default QuoteDetails;