//
// 

// GENERATE COIN CHANGE:
// Change is inevitable (especially when breaking a twenty). Make generateCoinChange(cents). Accept a number of American cents, compute and print how to represent that amount with smallest number of coins. return the optimal configuration of coins in an object.

const change = {
    quarters: 0,
    dimes: 0,
    nickels: 0,
    pennies: 0
}

function generateCoinChange(cents){

    while(cents > 4){
        if(cents > 25){
            change.quarters++
            cents = cents - 25
        }
        else if(cents > 10){
            change.dimes++
            cents = cents - 10
        }
        else if(cents > 5){
            change.nickels++
            cents = cents - 5
        }
        else if(cents > 1){
            change.pennies++
            cents = cents - 5
        }
    }
}
generateCoinChange(94)
console.log(change)
