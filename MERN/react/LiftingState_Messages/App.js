import React, { useState } from 'react';
import MessageForm from './Components/MessageForm';
import MessageDisplay from './Components/MessageDisplay';
    
    
function App() {
    const [currentMsg, setCurrentMsg] = useState("There are no messages");
    
    return (
        <>
            <MessageForm />
            <MessageDisplay message={ currentMsg } />
        </>
    );
}
    
export default App;

// Now when handling submitting the form, we can use the onNewMessage prop to pass that message up to App.js.

// When we submit the form in <MessageForm /> it passes the information up to the parent <App /> component which in turn passes it down to the <MessageDisplay /> component. This then displays our message.



