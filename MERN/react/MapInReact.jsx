

import React from 'react';
 
    
const Groceries = (props) => {
    // this could just as easily come from props
    const groceryList = ["pearl onions", "thyme", "cremini mushrooms", "butter"];
    return (
        <ul>{
            groceryList.map( (item, i) => 
                <li key={ i }>{ item }</li>
            )
        }</ul>
    ); 
}
    
export default Groceries;


// In this component we have a list of grocery items and we return an unordered list. Inside of the <ul> we use map to transform the array of groceries into an array of <li>, and for each element, we used its index i as the key to silence a React warning. Where did the index come from? The function we supply can optionally take in two additional arguments in addition to the current value: the current index, and a reference to the array itself. Thus, the entire signature of a map callback looks like the following:

// function (currentVal, currentIndex, thisArray) {
    // transform the val here

