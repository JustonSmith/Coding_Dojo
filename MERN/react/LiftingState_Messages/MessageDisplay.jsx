// Let's say we want to make an app that contains a component for creating messages and another component for displaying messages.


import react, { useState } from 'react';
    
    
const MessageDisplay = (props) => {
    return (
        <>
            <h1>Current Message</h1>
            <pre>{ props.message }</pre>
        </>
    );
};
    
export default MessageDisplay;