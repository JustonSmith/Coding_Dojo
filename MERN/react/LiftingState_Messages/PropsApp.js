// The solution is that we can provide a prop to the <MessageForm /> from the parent of both it and <MessageDisplay />. If this prop is a function, then we can have the child component call the function. And if the function accepts a parameter, then the child can pass a parameter into this function.

// imports removed for brevity
function App() {
    const [currentMsg, setCurrentMsg] = useState("There are no messages");
    
    const youveGotMail = ( newMessage ) => {
        setCurrentMsg( newMessage );
    }
    
    return (
        <>
            <MessageForm onNewMessage={ youveGotMail } />
            <MessageDisplay message={ currentmsg } />
        </>
    );
}

// We need to pass a new prop into <MessageForm />, we can call this onNewMessage and make this prop pass along the yoveGotMail function. When the child component uses the onNewMessage prop, it can pass a newMessage parameter into it. This will run the youveGotMail function inside of App which takes the newMessage and sets the currentMsg to it.
