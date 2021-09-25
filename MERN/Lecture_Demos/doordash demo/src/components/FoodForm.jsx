import React, {useState} from 'react';

const FoodForm = props => {

    // const [email, setEmail] = useState("");
    // const [foodName, setFoodName] = useState("");
    // const [spiceLevel, setSpiceLevel] = useState(1);

    const [formInfo, setFormInfo] = useState({
        email:"",
        foodName:"",
        spiceLevel:"",
    }) 

    const changeHandler = (e) => {
        console.log("changing inputs now")
        console.log("changing this input now: ", e.target.name)
        setFormInfo({
            ...formInfo,
            [e.target.name]: e.target.value
        })

    } 

    const [isSubmitted, setIsSubmitted] = useState(false);

    const submitHandler = (e)=> {
        e.preventDefault();
        console.log(`Wazzzaaa! You just ordered ${formInfo.foodName}`)
        setIsSubmitted(true);
    }

    return(
        <div>
            {isSubmitted?<h1 className = "text-success">Thank you for your order!</h1>: <h1 className="text-warning">Please fill out the form.</h1>}
            <br/>
            <h1>Welcome to Door Dash!</h1>
            <form onSubmit={submitHandler}>
                <div className="form-group">
                    <br />
                    <label htmlFor="exampleInputEmail1">Email address:</label>
                    <br />
                    <input onChange={changeHandler}type="email" name="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email"/>
                    <small id="emailHelp" className="form-text text-muted text-info">We'll never share your email with anyone else.</small>
                </div>
                <br />
                <div className="form-group">
                    <label htmlFor="">What would you like to order?:</label>
                    <input onChange={changeHandler} type="text" name="foodName" id="" className="form-control" placeholder="Order" />
                    <p className="text-danger">{formInfo.foodName.length < 4 && formInfo.foodName.length > 0 ? `Your order must be at least ${4 - formInfo.foodName.length} characters.`: "" }</p>
                </div>
                <div className="form-group">
                    <label htmlFor="">Spice Level: </label>&nbsp; &nbsp;
                    <select onChange={changeHandler} name="spiceLevel" id="">
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select>
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
            <br />
            <hr />
            <br />
            <div>
                <p>Your email address: {formInfo.email}</p>
                <p>Your order: {formInfo.foodName}</p>
                <p>Spice Level: {formInfo.spiceLevel}</p>
            </div>
        </div>
    )
}

export default FoodForm;


