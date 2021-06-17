// What is the correct way to create a variable with a value of 5?

var num = 5

// How does one log 'Hello World' into the console?

console.log("Hello World")

// Given the following piece of code:
    var ciso = ["Narciso", "Lobo", "nlobo@codingdojo.com"]
// What is the correct way to log Narciso into the console?

console.log(ciso[0])

// Using the same array, what is the correct way to change nlobo@codingdojo.com to narcisolobo@gmail.com?

ciso[2] = "narcisolobo@gmail.com"

// Which of the following code blocks will log the numbers 1 - 10 to the console?

    for(var i = 1; i <= 10; i++){

    }

// Which is the correct expression to check if a variable called num is negative?

    if(num >= 0){

    }

// What is the data type of the variable declared in the following line of JavaScript code?
// var pi = "3.14159"
"String"

// Which of the following code blocks defines a function that take in a name and logs it into the console?

function hello(name){

console.log(name)
}

// Which of the following loops prints the numbers from 1 to 100, but for mutiples of three prints "fizz" instead of the numbers?

var num = 1
    while (num <= 100){
        if (num % 3 == 0){
            console.log("fizz")}
                else{
                    console.log(num)
                    num++
                }
            }
