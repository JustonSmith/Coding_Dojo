// Design a function that given a number, returns whether that number is even or odd.

function evenOdd(num){
    if(num % 2 != 0){
        return "Odd"
    }
    else{
        return "Even"
    }
}   
console.log(evenOdd(6))

// Given an array of numbers, create a function to replace the last value with number of positive values.

function countPositive(arr){
    var count = 0
    for (var i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            count++
        }
    }
    arr[arr.length - 1] = count
    return arr
}
console.log(countPositive([-1,1,1,1,1,1]))