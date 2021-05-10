import React, {useState} from 'react'
import './styles.css';

const Form = props => {
    const [state, setState] = useState({
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        confirmPassword: "",
    });
    const onChangeHandler = e => {
        setState({
            ...state,
            [e.target.name]: e.target.value,
        });
    }
    return(
        <form>
            <hr />
            <div className="form-group">
                <label htmlFor="firstName">First Name</label>
                <input onChange={onChangeHandler} type="text" name="firstName" />
            </div>
            <hr />
            <div className="form-group">
                <label htmlFor="lastName">Last Name</label>
                <input onChange={onChangeHandler} type="text" name="lastName" />
            </div>
            <hr />
            <div className="form-group">
                <label htmlFor="email">Email</label>
                <input onChange={onChangeHandler} type="text" name="email" />
            </div>
            <hr />
            <div className="form-group">
                <label htmlFor="password">Password</label>
                <input onChange={onChangeHandler} type="password" name="password" />
            </div>
            <hr />
            <div className="form-group">
                <label htmlFor="confirmPassword">Confirm Password</label>
                <input onChange={onChangeHandler} type="text" name="confirmPassword" />
            </div>
            <hr />
            <div className="error">
                {(state.firstName.length !== 0 && state.firstName.length <2) && <p>First Name must be 2 characters long</p>}
                {(state.lastName.length !== 0 && state.lastName.length <2) && <p>Last Name must be 2 characters long</p>}
                {(state.email.length !== 0 && state.email.length <5) && <p>Email must be 5 characters long.</p>}
                {(state.password.length !== 0 && state.password.length <8) && <p>Password must be 8 characters long.</p>}
                {(state.confirmPassword.length !== 0 && state.password) && <p>Confirm Password must match password.</p>}
            </div>
        </form>
    )
}

export default Form;