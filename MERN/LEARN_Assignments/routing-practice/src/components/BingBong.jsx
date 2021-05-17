import React from 'react';


const BingBong = (props) => {

    let num = true;
    if (isNaN(+props.id)){
        num = false;
    }

    return (
        <div>
            {num ? <p>The Number is: {props.id}</p> : <p>The word is: {props.id}</p>}
        </div>
    );
};



export default BingBong;