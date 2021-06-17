// Programming Basics Week One Review

// *TO POST CODE INTO DISCORD*: Three backticks plus JS (```js) to start and three backticks (''') to end.

// Code flow: 
// Code is read and executed from top to bottom. 
// IMPORTANT**- Not necessarily linear.
// Functions are executed if/when they are called/invoked.
// For loops and while loops are executed iteratively.

// Variables and Data Types:
// Booleans (true/false), strings (QUOTATION MARKS ""), numbers (5, 6.78), null (placeholder), undefined (probably did something wrong), arrays([5, 3, 9, "Judge", false, [1,2,3,4,5]]).

var myString = "This is a string with spaces"
var num = 7
var array = [1,2,3,4,5]

// Conditionals:
// Conditionals return Booleans.
// Create threesFives() that finds and counts how many values from 1 and 100 (inclusinve) are evenly divisible by three and evenly divisible by 5. Display the final sum in the console. :::::::::

// PSEUDOCODE
// Design a function with no parameters.
// Create a variable to keep track of how many values are divisible by three. (threeCount)
// Create a variable to keep track of how many values are divisible by five. (fiveCount)
// Create a for loop.
// Define the limits of the loop.(Start = 1. End <= 100)
// find every number divisible by three.
// Increment the threeCount variable.
// Find every number divisible by five.
// Increment the fiveCount variable.
// after the for loop, log the count variables to the console.
// Call the function.

function threesFivesCount(){
    var threeCount = 0
    var fiveCount = 0
    for(var i = 1; i <= 100; i++){
        if( i % 3 === 0){
            threeCount++
        }
        if( i % 5 === 0){
            fiveCount++
        }
    }
    console.log(" The number of three multiples is " + threeCount + " The number of five multiples is " + fiveCount,".") 
}
threesFivesCount()

// Concatenator (+ in the log)

// Double equal == converts both sides of the operator to the same data type before comparison.
// Triple equal === does not. It checks

// Scope:
// A variable decalred within a function is not visible outside of it, but a variable declared outside a function can be visible inside it.

var die = [1,2,3,4,5,6]

console.log(die[Math.floor(Math.random()*die.length)])

// Operators (such as =, ==, ===, &&, ||, !, +=, ++, -=, --, *=, /=, and %)

if (num % 3 === 0){
    // code block here
}
if (num % 3 === 0 && num %5 === 0){
    // code block here
}
if(!num % 3 === 0){
    // code block here
}

count = count + 1
count++

function squareArrayVals(arr){
    for(var i = 0; i < arr.length; i++){
        arr[i] *= arr[i]
    }
    return arr
}
console.log(squareArrayVals([0,69,420,365,1000]))

// MODULOUS OPERATOR: Returns the remainder of dividing the first operand by the second operand over and over and over again until it cant anymore. (X % Y). X is first Op. Y is second Op.

console.log(42 % 10)

// Loops (FOR, WHILE, BREAK, CONTINUE)

function countToFive(){
    var num
    while (num <= 5){
        // run code
        console.log("num is now: " + num)
        if (num === 3){
            console.log("when num equals three")
            num++
            continue

        }
        num++
    }
    return num
}

var myNum = countToFive()

console.log(myNum)

// ***STOP CODE*** CNTRL + ALT + M

// Functions (input parameters and return value).

function sayMyName(name){
    return name
}
var myName = sayMyName("Sludgey")
console.log(sayMyName("Sludgey"))

// Second: Create betterThreesFives(start, end) that allows you to enter arbitrary start and end values for your range. Think of threesFivesCount() as betterThreesFivesCount(1,100).

function betterThreesFivesCount(startNum, endNum){
    var threeCount = 0
    var fiveCount = 0
    for(var i = startNum; i <= endNum ; i++){
        if( i % 3 === 0){
            threeCount++
        }
        if( i % 5 === 0){
            fiveCount++
        }
    }
    console.log(" The number of three multiples is " + threeCount + " and the number of five multiples is " + fiveCount + ".") 
}

betterThreesFivesCount(1,100)

// JavaScript Math Library:

// floor
// ceil (round up)
// round
// trunc (shorten by cutting top or end)
// random

var num = 6.2

num = Math.floor(num)

console.log(num)

var randomNum = Math.trunc(Math.random()) * 10
console.log(randomNum)

// Rockin’ the Dojo Sweatshirt:
// Ever since you arrived at the Dojo, you wanted one of those cool Coding Dojo sweatshirts – maybe even more than one. Let’s say they cost $20 (including tax), but friendly Josh gives a 9% discount if you buy two, a nice 19% discount if you buy three, or a sweet 35% discount if you buy four or more. He only accepts cash and says he doesn’t have coins, so you should round up to the nearest dollar. Build function sweatshirtPricing(num) that, given a number of sweatshirts, returns the cost.

function sweatShirtPricing(num){
    var cost = 20
    if(num === 1){                                                
        return cost
    }
    else if(num === 2){
        cost = (cost * 2) - (cost * 2 * .09)
            return Math.ceil(cost)
    }
    else if(num === 3){
        cost = (cost * 3) - (cost * 3 * .19)
            return Math.ceil(cost)
    }
    else if(num === 4){
        cost = cost * 4 - (cost * 4 * .35)
            return Math.ceil(cost)
    }
}
console.log(sweatShirtPricing(4))

// 
// ***OR***
//

function sweatshirtPricing(num){
    var $money= null
    var sweatshirtCost = 20
    if(num == 1){
        $money = sweatshirtCost
    }
    if(num == 2){
        $money = Math.ceil(num*(sweatshirtCost*.91))
    }
    if(num == 3){
        $money = Math.ceil(num*(sweatshirtCost*.81))
    }
    if(num>=4){
        $money = Math.ceil(num*(sweatshirtCost*.65))
    }
    return $money
}
console.log(sweatshirtPricing(2))