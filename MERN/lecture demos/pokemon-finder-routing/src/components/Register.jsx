import React from 'react';


const Register = () => {
    return (
        <div className= "container w-25">
            <form>
            <div className="form-group">
                    <label for="exampleInputEmail1">- First Name -</label>
                    <input type="text" className="form-control .col-sm-*" />
                </div>
                <br />
                <div className="form-group">
                    <label for="exampleInputEmail1">- Last Name -</label>
                    <input type="text" className="form-control" />
                </div>
                <br />
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
                <br />
                <div className="form-group">
                    <label for="exampleInputPassword1">- Confirm Password -</label>
                    <input type="password" className="form-control" />
                </div>
                <br />
                <br />
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
        </div>
    );
};



export default Register;