// With Reach Router, we have an extremely easy way to pass parameters through our React project. Our front end url parameters will be passed down as props to our component. Let's say we have the following:

function App(){
    return (
        <div className="App">
            <Router>
                <ListOfDogsComponent path="/dogs" />
                <DetailDogComponent path="/dogs/:id" />
            </Router>
        </div>
    )
}

// Then, within our Detail dog component:

import React from 'react';
const DetailDogComponent = props => {
    return (
        <p>You are looking at the dog with id {props.id}</p>
    )
}

// Note: Regardless of what we send down in our url, the type of the parameter will always be a string. If you need it to be a number, you will need to convert the value into a number.

