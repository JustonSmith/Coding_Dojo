// Let's say we want to make an app that contains a component for creating messages and another component for displaying messages.


import react, { useState } from 'react';
    
    
const MessageForm = (props) => {
    const [msg, setMsg] = useState("");
    
    const handleSubmit = (e) => {
        e.preventDefault();
        // what should we do with the message?
    };
    
    return (
        <form onSubmit={ handleSubmit }>
            <h1>Set Message</h1>
            <textarea 
                rows="4"
                cols="50"
                placeholder="Enter your message here"
                onChange={ (e) => setMsg(e.target.value) }
                value={ msg }
            ></textarea>
            <input type="submit" value="Send Message" />
        </form>
    );
};
    
export default MessageForm;