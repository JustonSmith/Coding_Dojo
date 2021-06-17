// 
// 
// 
// Programming Basics Belt Exam:

// Basic 13:

// 1. Print 1 - 255.

function print1To255(){
    for (var i = 1; i <=255; i++){
        console.log(i)
    }
}
print1To255()

// 2. Print odds 1 - 255.

function printOdds1To255(){
    for(var i = 1; i <= 255; i+=2){
        console.log(i)
    }
}
printOdds1To255()

// 3. Print integers and sum 0 - 255.

function printIntsAndSum0To255(){
    var sum = 0
    for(var i = 0; i <= 255; i++){
        console.log(i)
        sum += i
        console.log(sum)
    }
}
printIntsAndSum0To255()

// 4. Iterate and Print an Array.

function printArrayVals(arr){
    for(var i = 0; i < arr.length; i++){
        console.log(arr[i])
    }
}
printArrayVals([1, 2, 3, 4, 5])

// 5. Find and Print Max.

function printMaxOfArray(arr){
    var max = 0
    for(var i = 0; i < arr.length; i++){
        if (arr[i] > max){
            max = arr[i]
        }
    }
    console.log(max)
}
printMaxOfArray([1, 2, 3, 4, 5])

// 6. Get and Print Average.

function printAverageOfArray(arr){
    var sum = arr[0]
    for(var i = 1; i < arr.length; i++){
        sum = sum + arr[i]
        average = sum / arr.length
    }
    return average
}
console.log(printAverageOfArray([1, 2, 3, 4, 5]))

// 7. Array with Odds.

function returnOddsArray1To255(){
    var array = []
    for(var i = 1; i <= 255; i+=2){
        array.push(i)
    }
    return array
}
console.log(returnOddsArray1To255())

// 8. Square the values.

function squareArrayVals(arr){
    for(var i = 0; i < arr.length; i++){
        arr[i] = (arr[i] * arr[i])
    }
    return arr
}
console.log(squareArrayVals([1, 2, 3, 4, 5]))

// 9. Greater than Y.

function returnArrayCountGreaterThanY(arr, y){
    var count = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > y)
        count++
    }
    console.log(count)
}
returnArrayCountGreaterThanY([1, 2, 3, 4, 5], 0)

// 10. Zero out Negative Numbers.

function zeroOutArrayNegativeVals(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 0
        }
    }
    return arr
}
console.log(zeroOutArrayNegativeVals([-1, -2, -3, -4, -5, ]))

// 11. Max, Min, Average

function maxMinAvg (arr){
    var max = arr[0]
    var min = arr[0]
    var sum = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i] 
        }
        if(arr[i] < min){
            min = arr[i]
        }
        sum += arr[i]
        }
        average = sum / arr.length
            console.log(max, min, average)
}
maxMinAvg([1, 2, 3, 4, 5])

// 12. Shift Array Values.

function shiftArrayValsLeft(arr){
    for(var i = 1; i < arr.length; i++){
        arr[i - 1] = arr[i]
    }
    arr[arr.length - 1] = 0
    return arr
}
console.log(shiftArrayValsLeft([1, 2, 3, 4, 5]))

// 13. Swap String for Array Negative Values.

function swapStringForNegativeArrayValues(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = "Dojo"
        }
    }
    return arr
}
console.log(swapStringForNegativeArrayValues([-1, -2, -3, -4, -5]))
// 
// 
// 
// Algorithm Challenge 1: FiZZ BuZZ

// Write a function that prints numbers from 1 to 100. For multiples of three print "fizz" instead of the number. For multiples of 5 print "buzz" instead of the number, and for numbers that are miltiples of both three and five print "fizzbuzz" instead of the number.

// PSEUDOCODE:
//  First I need to write a function that will print the numbers between 1 and 100. 
//  Then I need to use a FOR loop that includes 1 and stops at 100.
//  I will need an IF statement and a modulo to get my multiples of three.
//  I will need an ELSE IF statement and a modulo to get my multiples of five.
//  For each of these I will need to indicate those numbers are swapped with either the string "fizz" for threes, the string "buzz" for fives, or the string "fizzbuzz" for multiples of both. 
//  I do this by logging the string after the IF/ELSE IF statements.
//  I will also need to use another ELSE statement to log the numbers that are not multiples of either three or five.
// 
// 

function fizzBuzzChallenge(){
    for(var i = 1; i <= 100; i++){
        if( i % 3 === 0 && i % 5 === 0){
            console.log("fizzbuzz")
        }
        else if(i % 3 === 0){
            console.log("fizz")
        }
        else if( i % 5 === 0){
            console.log("buzz")
        }
        else console.log(i)
    }
}
fizzBuzzChallenge()
// 
// 
// 
// 