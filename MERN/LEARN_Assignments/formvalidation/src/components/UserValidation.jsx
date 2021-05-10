

import React from 'react';

const UserValidation = (values) => {
    let errors = {};

    // First Name

    if (!values.firstName){
        errors.firstName = "First name required.";
    }else if (values.firstName.length < 2) {
        errors.firstName = "First name must be at least 2 characters.";
    }

    // Last Name

    if (!values.lastName){
        errors.lastName = "Last name required.";
    }else if (values.lastName.length < 2) {
        errors.lastName = "Last name must be at least 2 characters.";
    }

    // Email

    if (!values.email){
        errors.email = "Email address required.";
    }else if (!/\S+@\S+\.\S+/.test(values.email)) {
        errors.email = "Invalid email address.";
    }

    // Password

    if (!values.password) {
        errors.password = "Password required.";
    }else if (values.password.length < 8) {
        errors.password = "Password must be at least 8 characters."
    }
    return errors
}
export default UserValidation