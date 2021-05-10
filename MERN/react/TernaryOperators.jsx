// Ternary operators offer a better way to conditionally render an element. For a Ternary refresher check out the MDN documentation. The biggest advantage to us using a ternary operator here, is that we can replace the formMessage function we wrote with some code that can go directly into our JSX.



{/* rest of component removed for brevity */}
    
<form onSubmit={ createUser }>
    {
        hasBeenSubmitted ? 
        <h3>Thank you for submitting the form!</h3> :
        <h3>Welcome, please submit the form.</h3> 
    }
    <div>
        <label>Username: </label> 
        <input type="text" onChange={ (e) => setUsername(e.target.value) } />
    </div>
</form>
    
{/* rest of component removed for brevity */}