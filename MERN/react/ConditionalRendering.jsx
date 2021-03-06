
// Let's say we want to render something in the DOM that is based on some other value. Using the previous example from the form, we want to have output after the form was submitted. At the top, let's say we want to have an <h3> that will say "Welcome. please submit the form." if the form has not been submitted. After we click submit, we want to change the text to say "Thank you for submitting the form!". We can add some logic in our component to take care of this. We will need to add a submit button and a function that will run onSubmit (we'll call it createUser).




import React, { useState } from  'react';
    
    
const UserForm = (props) => {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [hasBeenSubmitted, setHasBeenSubmitted] = useState(false);
    
    const createUser = (e) => {
        e.preventDefault();
        const newUser = { username, email, password };
        console.log("Welcome", newUser);
        setHasBeenSubmitted( true );
    };
    
    const formMessage = () => {
        if( hasBeenSubmitted ) {
        return "Thank you for submitting the form!";
	} else {
        return "Welcome, please submit the form";
	}
    };
    
    return (
        <form onSubmit={ createUser }>
            <h3>{ formMessage() }</h3>
        <div>
                <label>Username: </label> 
                <input type="text" onChange={ (e) => setUsername(e.target.value) } />
            </div>
            <div>
                <label>Email Address: </label> 
                <input type="text" onChange={ (e) => setEmail(e.target.value) } />
            </div>
            <div>
                <label>Password: </label>
                <input type="text" onChange={ (e) => setPassword(e.target.value) } />
            </div>
            <input type="submit" value="Create User" />
        </form>
    );
};
    
export default UserForm;

// By default, hasBeenSubmitted is false. When the form is submitted this value in state will be flipped to true which will cause the form to re-render and the formMessage function can be run again which will produce a message thanking the user for submitting the form.