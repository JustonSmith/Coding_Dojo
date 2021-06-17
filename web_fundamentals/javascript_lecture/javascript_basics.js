// 
// 

// LET AND CONST

// variable can have one of two scopes, global or function:

var myAge = 50

function birthday(myAge){
    myAge += 51
    console.log("Inside the function " + myAge)
}

birthday(myAge)

console.log("Outside the function" + myAge) 

// let and const are block scoped. 
// const cannot be reassigned:

const num = 25

for(let i = 1; i < arr.length; i++){

}

// Use const unless you know the value will be reassigned.

const myArr = [1, 2, 3, 4, 5]
myArr.push(6)
console.log(myArr)

const myName = "Judge"
const myAge = 50

// Concatenation of strings:

console.log("Hello, my name is " + myName + " and I am " + myAge + " years old.")

// Template literals:

console.log(`Hello, my name is ${myName} and I am ${myAge} years old.`)



// *Reference Datatypes ie. Arrays and Objects*

var num = 5

const myNums = [1, 2, 3, 4, 5]

// SETTING
// Arrays are 0 indexed
myNums[0] = 7

// GETTING
console.log(myNums[2])

// Swapping values in an array:
const temp = myNums[0]
myNums[0] = myNums[4]
console.log(`first operation: ${myNums}`)

myNums[4] = temp
console.log(`first operation: ${myNums}`)

// Shifting values in an array:
const num3 = myNums.shift()
console.log(num3)

// Push, Pop, and Length:

myNums.push(6)
console.log(myNums)

myNums.pop()
// .pop also returns last element in an array. 
// Store in variable to keep and use it. 
const num2 = myNums.pop()

myNums.length
console.log(myNums.length)

for(let i = 0; i < myNums.length; i++){
    console.log(myNums[i])
}

// Function hoisting:

greet()

function greet(){
    console.log("Hello World")
}

// Function Expression:

const greetExpression = function(){
    console.log("Function Expression Example: Hello World")
}

greetExpression()

// Arrow Function:

function greet(){
    return "Hello World"
}
greet()

const greetArrow = () => {
    return "Hello World"
}

greetArrow()

// If only one parameter, can just give name of parameter.

// *** DONT FORGET TO CONSOLE.LOG NOT JUST RETURN. ***

// Reverse this array in place:

const myArr = [1, 2, 3, 4, 5, 6]

function reverseArray(arr){
    for(let i = 0; i < Math.floor(arr.length/2); i++){
        let temp = arr[i]
        arr[i] = arr[arr.length - 1 - i]
        arr[arr.length - 1 - i] = temp
    }
    return arr
}
console.log(reverseArray(myArr))