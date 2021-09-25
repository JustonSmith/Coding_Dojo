import React, {useState} from 'react';
import axios from'axios'
import { navigate } from '@reach/router';



const Create = () => {
    const [formInfo, setFormInfo] = useState({
        content:"",
        author:"",
        quotedOn:"",
    })

    const [errors, setErrors] = useState({})

    const changeHandler = (event) => {
        console.log("...changing inputs.")
        console.log(event.target.value)
        setFormInfo({
            ...formInfo, 
            [event.target.name]: event.target.value
        })
    }

    const submitHandler = (event) => {
        event.preventDefault()
        console.log("...form is being submitted.")
        axios.post("http://localhost:8000/api/quotes/create", formInfo)
        .then(res => {
            console.log("...quote posted!")
            console.log(res)
            if(res.data.results){
            navigate("/quotes/success")
            }else {
                setErrors(res.data.errors) 
            }
        })
        .catch(err => console.log("...form has errors. Please try again.", err))
    }

    // const sortQuote = () => {

    // }

    return (
        <div className= "container w-50" >
            <hr />
            <h3>- Create Quote -</h3>
            <hr />
            <br />
            <form onSubmit={submitHandler}>
                <div className="form-group">
                    <label> Author:</label>
                    {errors.author? <p className="text-danger">{errors.author.message}</p>: ""}
                    <hr />
                    <input onChange={changeHandler} type="text" name="author" id="" className= "form-control" />
                    <hr />
                </div>
                <br />
                <div className="form-group">
                    <label> Content:</label>
                    <hr />
                    {errors.content? <p className="text-danger">{errors.content.message}</p>: ""}
                    <textarea onChange= {changeHandler} name="content" id="" cols="30" rows="5" className="form-control"></textarea>
                    <hr />
                </div>
                <br />
                <div className="form-group">
                    <hr />
                    <label> QuotedOn:</label>
                    <hr />
                    {errors.quotedOn? <p className= "text-danger"> {errors.quotedOn.message}</p>: ""}
                    <input onChange={changeHandler} type="date" name="quotedOn" id="" className= "form-control" />
                    <hr />
                    <br />
                    <br />
                    <input type="submit" value="Create!" className="btn btn-primary" />
                </div>
            </form>
        </div>
    );
};



export default Create;