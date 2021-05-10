import React from 'react';
import './styles.css';

const HookForm = props => {
    const {input, setInput} = props;
    const onChange = (e) => {
        setInput({
            ...input,
            [e.target.name]: e.target.value,
        });
    };
    return(
        <form>
            <div className ="form-group">
                <label htmlFor="firstName">First Name</label>
                <input onChange={onChange} type="text" name="firstName" />
            </div>
            <div className="form-group">
                <label htmlFor="lastName">Last Name</label>
                <input onChange={onChange} type="text" name="lastName" />
            </div>
            <div className="form-group">
                <label htmlFor="email">Email Address</label>
                <input onChange={onChange} type="text" name= "email" />
            </div>
            <div className="form-group">
                <label htmlFor="password">Password</label>
                <input onChange={onChange} type="password" name="password" />
            </div>
            <div className="form-group">
                <label htmlFor="confirm password"> Confirm Password</label>
                <input onChange={onChange} type="password" name="confirm-password" />
            </div>
        </form>
    )
};
export default HookForm;