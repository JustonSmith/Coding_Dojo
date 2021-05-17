import React from 'react';


const Closing = (props) => {

    let num = true;
    if (isNaN(+props.id)){
        num = false;
    }
    const styles = {
        color: props.color,
        background: props.bgColor,
    }


    return (
        <div style={styles} >
            {num ? <p> The number is: {props.id}</p> : <p>The word is: {props.id}</p>}
        </div>
    );
};



export default Closing;