// INTERVIEW ALGORITHIM
// 
// Write a function that, given an array, reverses the order of the elemenets in that array, in place. Write out the pseudocode.

// In place means do not create a new array.

// ***NOT***
var newArray = []

// PSEUDOCODE:
// Design a function that reverses the order of the array. (reverseArray())
// Identify the values of the array.
// Create a loop that will go through every position in the array.
// Swap first position with last position
// Swap second position with second to last position
// etc. until I get halfway.

function reverseArray(arr){
    for(var i = 0; i < Math.floor(arr.length/2); i++){
        var temp = arr[i]
        arr[i] = arr[arr.length - 1 - i]
        arr[arr.length - 1 - i] = temp
        console.log("Loop number " + i + ": " + arr)
    }
}
var myArray = [1,2,3,4,5,6]
reverseArray(myArray)

// Math.floor stops the loop in the middle when the number if values in the Array are odd.