// 
// 

// Basic Foundation II:

// 1. Biggie size:
// Given an array, write a function that changes all positive numbers in the array to the string "big."

function biggieSize(arr){
    for(var i = 0; i <= arr.length; i++){
        if(arr[i] <= 0){
            console.log(arr[i])
        }
        else console.log("big")
    }
}
biggieSize([-1, 3, 5, -5])

// 2. Print Low, Return High:
// Create a function that Takes in an array of numbers. The function should print the lowest number in the array, and return the highest value in the array.

function printLowReturnHigh(arr){
    var low = arr[0]
    var high =arr[0] 
    for(var i = 0; i <= arr.length; i++){
        if(arr[i] > high){
        high = arr[i]
        }
        if(arr[i] < low){
        low = arr[i]
        }
    }
    console.log(low)
    return high
}
console.log(printLowReturnHigh([1, 2, 3, 4, 5]))

// 3. Print One, Return Another:
// Build a function that takes in an array of numbers. The function should print the SECOND TO LAST value in the array, and return the FIRST ODD value in the array. 

function print1ReturnAnother(arr){
    console.log("Second to last value: " + arr[arr.length - 2]);
    for(var i = 0; i < arr.length; i++){
        if(arr[i] % 2 != 0){
            return arr[i]
        }
    }
    return "No odd numbers in array"
}
console.log(print1ReturnAnother([2, 3, 4, 5, 6, 7, 8]))

// 4. Double Vision:
// Given an array, create a function the returns another array where each value in the array has doubled. Calling double([1, 2, 3]) should return [2, 4, 6] without changing the original array.

function doubleVision(arr){
    var newArr = []
    for(var i = 0; i < arr.length; i++){
        newArr.push(arr[i] * 2)
    }
    return newArr
}
console.log(doubleVision([1, 2, 3, 4, 5]))

// 5. Count Positives:
// Given an array of numbers, create a fuunction to replace the last value with the number of positive values found in the array. Example: countPositives([-1, 1, 1, 1, ]) changes the original array to [-1, 1, 1, 3].

function countPositives(arr){
    var count = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] >= 0){
        count++
        }
    }
    arr[arr.length-1] = count
    return arr
}
console.log(countPositives([-1, -2, -3, 1, 2, 3, 4]))

// 6. Evens and Odds:
// Create a function that accepts an array. Every time the array has three odd values in a row, print "Thats Odd!". Every time the array has three evens in a row, print "Even more so!"

function evensAndOdds(arr){
    var evens = 0
    var odds = 0
    for(var i = 0; i < arr.length; i++){
        if (arr[i] % 2 === 0){
            odds = 0
            evens++
            if(evens === 3){
                evens = 0
                console.log("Even more so!")
            }
        }else{
            evens = 0
            odds++
            if( odds === 3){
                odds = 0
                console.log("That's odd!")
            }
        }
    }
    return arr
}
console.log(evensAndOdds([1, 1, 1, 2, 2, 2]))

// 7. Increment the Seconds:
// Given an array of numbers (arr), add 1 to every other element, specifically those whose index is odd (arr[1], arr[3], arr[5], etc.). Afterwards console.log each array value and return arr.

function incrementSeconds(arr){
    for(var i = 0; i < arr.length; i++){
        if(i % 2 != 0){
            arr[i] += 1
        }
        console.log(arr[i])
    }
    return arr
}
console.log(incrementSeconds([1, 2, 3, 4, 5, 6, 7, 8]))

// 8.  Previous Lengths - You are passed an array(similar to saying 'takes in an array' or 'given an array') containing strings. Working within that same array, replace each string with a number - the length of the string at the previous array index - and return the array. For example, previousLengths(["hello", "dojo", "awesome"]) should return ["hello", 5, 4]. 

// const examplearrayOfStrings = ["hello, "dojo", "awesome"]

// ***PSEUDOCODE***
// Declare function that requires an array of strings.
// Do not instantiate a new array.
//  Start a for loop that starts at the end of the array and ends at the start of the array. 
// At each position, we must overwrite that position with the length of the string at the position to its left.
// We do that by subtracting 1 at each position and referencing the length. 
// after the for loop is complete, return the modified array.

    function previousLengths(arr){
        for(let i = arr.length - 1; i > 0; i--){
            arr[i] = arr[i - 1].length // Loop 1 - arr[2] = arr[1]
        }
        return arr
    }
console.log(previousLengths(["hello", "dojo", "awesome"]))

// 9. Add Seven:
// Build a function that accepts an array. Return a NEW array with all the values of the original, but add 7 to each. Do not alter the original array. Example: addSeven([1, 2, 3]) should return ([8, 9, 10]) in a new array. 

function addSeven(arr){
    var newArr = []
    for(i = 1; i < arr.length; i++){
        newArr.push(arr[i] + 7)
    } 
    return newArr
}
console.log(addSeven([1, 2, 3, 4, 5]))

// 10. Reverse Array:
// Given an array write a function that reverses its values, in place. Example: reverse([1, 2, 3, 4]) returns the same array, but now contains values reversed like so: ([4, 3, 2, 1]). Create without using an empty array temp variable.



function reverseArray(arr){
    for(let i = 0; i < Math.floor(arr.length/2); i++){
        let temp = arr[i]
        arr[i] = arr[arr.length - 1 - i]
        arr[arr.length - 1 - i] = temp
    }
    return arr
}
console.log(reverseArray([1, 2, 3, 4, 5, 6]))

// 11. Outlook; Negative:
// Given an array, CREATE AND RETURN A NEW ONE containing all the values of the original array, but make them negative(not simply multiplied by -1). Given ([-1, -3, 5]), return [-1, -3, -5].

function outlookNegative(arr){
    var newArr = []
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            newArr.push(arr[i] * -1)
        }else{
            newArr.push(arr[i])
        }
    }
    return newArr
}
console.log(outlookNegative([-1, -3, 5]))

// 12. Always Hungry:
// Create a function that accepts an array, and prints "Yummy" each time one of the values is equal to "Food". If no array values are food, then print "I'm Hungry" once.

function alwaysHungry(arr){
    var hungry = true
    for(var i = 0; i < arr.length; i++){
        if(arr[i] === "food"){
            console.log("Yummy")
            hungry = false
        }
    }
    if(hungry === true){
        console.log("I'm Hungry")
    }
    return 0
}
console.log(alwaysHungry([1, 2, 3, "food", 4, "food"]))

// 13. Swap Toward the Center:
// Given an array, swap the first and last values, third and third to last values, etc. Example: swapTowardsCenter([true, 42, "Ada", 2, "pizza"]) turns the array into ["pizza", 42, "Ada", 2, true].

function swapTowardsCenter(arr){
    for(var i = 0; i < arr.length/2; i+=2){
        var temp = arr[i]
        arr[i] = arr[arr.length - 1 - i]
        arr[arr.length - 1 - i] = temp
    }
    return arr
}
console.log(swapTowardsCenter([true, 42, "Ada", 2, "pizza"]))

// 14. Scale The Array:
// Given an array (arr) and a number (num), multiply all values in the array (arr) by the number (num) and return the changed array (arr). For example, scaleArray([1, 2, 3], 3) should return [3, 6, 9].

function scaleArray(arr, num){
    for(var i = 0; i < arr.length; i++){
        arr[i] *= num
    }
    return arr
}
console.log(scaleArray([1, 2, 3, 4, 5], 10))