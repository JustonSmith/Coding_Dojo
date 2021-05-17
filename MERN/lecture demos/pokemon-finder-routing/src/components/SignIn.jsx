import React from 'react';


const SignIn = () => {
    return (
        <div className= "container w-25">
            <form>
                <div className="form-group">
                    <label for="exampleInputEmail1">- Email address -</label>
                    <input type="email" className="form-control" />
                    <small id="emailHelp" className="form-text text-muted">We'll never share your email with anyone else.</small>
                </div>
                <br />
                <div className="form-group">
                    <label for="exampleInputPassword1">- Password -</label>
                    <input type="password" className="form-control" />
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
        </div>
    );
};



export default SignIn;