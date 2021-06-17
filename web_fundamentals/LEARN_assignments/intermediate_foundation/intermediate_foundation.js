// 
// 

// Intermediate Foundation

// 1. SIGMA:
//  Impliment function sigma(num) that, given a number, returns the sum of all positive integers up to the given number. Ex: sigma(3) = 6 (or 1 + 2+ 3); sigma(5) = 15 (or 1 + 2 + 3 + 4 +5).

function sigma(num){
    var sum = 0
    for(var i = 0; i <= num; i++){
        sum += i;
    }
    return sum
}
console.log(sigma(5))

// 2. FACTORIAL:
// Write a function factorial(num) that, given a number, returns the product (multiplication) of all positive integers from 1 up to the given number (inclusive). For example, factorial(3) = 6 (or 1 * 2 * 3); factorial(5) = 120 (or 1 * 2 * 3 * 4 * 5)

function factorial(num){
    var product = 1
    for(var i = 1; i <= num; i++){
        if(i >= 0){
            product *= i
        }
    }
    return product
}
console.log(factorial(5))

// 3. FIBONACCI:
// Create a function to generate Fibonacci numbers. In this famous mathematical sequence, each number is the sum of the previous two, starting with values 0 and 1. Your function should accept one argument, an index into the sequence (where 0 corresponds to the initial value, 4 corresponds to the value four later, etc.) Examples: fibonacci(0) = 0 (given), fibonacci(1) = 1 (given), fibonacci(2) = 1 (fib(0)+fib(1), or 0+1), fibonacci(3) = 2 (fib(1) + fib(2)3, or 1+1), fibonacci(4) = 3 (1+2), fibonacci(5) = 5 (2+3), fibonacci(6) = 8 (3+5), fibonacci(7) = 13 (5+8).  Do this without using recursion first. 

function fibonacci(num){
    var arr = [0, 1]
    if(num >= 2){
        for(var i = 2; i <= num; i++){
            arr.push(arr[i - 1] + arr [i - 2])
        }
    }
    return arr[num]
}
console.log(fibonacci(7))

// OR

function fibRecursive(num){
    if(num < 2){
        return num
    }
    else{
        return fibRecursive(num - 2) + fibRecursive(num - 1)
    }
}
console.log(fibRecursive(20))

// 4. ARRAY: SECOND - TO - LAST:
// Return the second to last element in an array.Given [42, true, 4, "Liam", 7]

function secondToLast(arr){
    if(arr.length < 2) {
        return null
    }
    return arr[arr.length - 2]
}

console.log(secondToLast([1, 2, 3, 4, 5]))

// 5. ARRAY: NTH - TO - LAST:
// Return the element that is N from array's end. Given ([5, 2, 3, 6, 4, 9, 7]) return 4.

function nthToLast(arr, num){
    if (num > arr.length){
        return null
    }
    return arr[arr.length - num]
}
console.log(nthToLast([1, 2, 3, 4, 5], 3))

// 6. ARRAY: SECOND - LARGEST:
// Return the second larget number in the array. Given ([42, 1, 4, 3.14, 7]) return 7. 

function secondLargest(arr){
    var biggest = 0
    var secondbiggest = 0
    for(var i = 0; i < arr.length; i++){
        if(biggest < arr[i]){
            secondbiggest = biggest;
            biggest = arr[i]
        }
        else if( secondbiggest < arr[i]){
            if(arr[i] != biggest){
                secondbiggest = arr[i]
            }
        }
    }
    return secondbiggest
}
console.log(secondLargest([42, 1, 4, 3.14, 7]))

// 7. DOUBLE TROUBLE: 
// Create a function that changes a given array to list each existing element twice, retaining original order. Convert [4, "Ulysses", 42, False] to [4, 4, "Ulysses", "Ulysses", 42, 42, false, false]

function doubleTrouble(arr){
    var count = arr.length
    for(var i = count - 1; i <= 0; i--){
        arr.push(arr[i])
        for(var idx = arr.length - 1; idx > i + 1; idx++){
            var temp = arr[idx]
            arr[idx] = arr[idx - 1]
            arr[idx] = temp
        }
    }
    return arr
}
console.log(doubleTrouble([4, 4, "Ulysses", 42, false]))