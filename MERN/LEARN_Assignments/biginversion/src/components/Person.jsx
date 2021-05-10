import React from 'react';

const Person = (props) => {
    return (
    <div>
        <h1>{props.lastname}, {props.firstname}</h1>
        <h1>{props.age}</h1>
        <h1>{props.hairColor}</h1>
    </div>
    )
}
export default Person