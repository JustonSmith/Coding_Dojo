import React, {useState, useEffect} from 'react';
import axios from 'axios';
import moment from 'moment';
import {navigate} from '@reach/router';

const Edit = (props) => {
    const[quoteInfo, setQuoteInfo]= useState({
        content:"",
        author:"",
        quotedOn:"",
    })

    useEffect(()=> {
        axios.get(`http://localhost:8000/api/quotes/${props._id}`)
            .then(res => {
                console.log(res)
                setQuoteInfo(res.data.results)
            })
            .catch(err => console.log(err))

    },[])

    const updateInfo = (event) => {
        event.preventDefault();
        axios.put(`http://localhost:8000/api/quotes/update/${props._id}`, quoteInfo)
        .then(res => {
            console.log(res)
            navigate("/quotes/editsuccess")
        })
        .catch(err => console.log(err))
    }

    const changeHandler = (event => {
        setQuoteInfo({
            ...quoteInfo,
            [event.target.name]: event.target.value
        })
    })

    return(
        <div className="container w-50" >
            <hr />
            <h3>Edit Quote</h3>
            <form onSubmit= {updateInfo}>
                <div className="form-group">
                    <hr/>
                    <label> Author:</label>
                    <hr />
                    <input onChange= {changeHandler} type="text" name="author" id="" className= "form-control" value={quoteInfo.author} />
                    <hr />
                </div>
                <br />
                <div className="form-group">
                    <label> Content:</label>
                    <hr />
                    <textarea onChange= {changeHandler} name="content" id="" cols="30" rows="5" className="form-control" value= {quoteInfo.content}></textarea>
                    <hr />
                </div>
                <br />
                <div className="form-group">
                    <hr />
                    <label> QuotedOn:</label>
                    <hr />
                    <input onChange= {changeHandler}  type="date" name="quotedOn" id="" className= "form-control" value= {moment(quoteInfo.quotedOn).add(2, 'd').format("MM-DD-YYYY")} />
                    <hr />
                    <br />
                    <input type="submit" value="Update!" className="btn btn-primary" />
                </div>
            </form>
        </div>
    );
};



export default Edit;