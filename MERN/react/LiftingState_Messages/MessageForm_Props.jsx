// We need to pass a new prop into <MessageForm />, we can call this onNewMessage and make this prop pass along the yoveGotMail function. When the child component uses the onNewMessage prop, it can pass a newMessage parameter into it. This will run the youveGotMail function inside of App which takes the newMessage and sets the currentMsg to it.

// most of the component removed for brevity
const handleSubmit = (e) => {
    e.preventDefault();
    props.onNewMessage( msg );
};
    