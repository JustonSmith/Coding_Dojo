// 
// 

// Basic foundation 1:

// 1. Print 1-255. Print all integers from 1 - 255.

function print1To255(){
    for(var i = 1; i <= 255; i++){
        console.log(i)
    }
}
print1To255()

// 2. Print Odds 1-255. Print all odd integers from 1 - 255.

function oddNum(){
    for(var i = 1; i <= 255; i+=2){
        console.log(i)
    }
}
oddNum()

// 3. Print integers and sum 0 - 255. With each integer print the sum so far.

function integerPrint(){
var sum = 0
    for(var i = 0; i <= 255; i++){
        console.log(i)
        sum += i
        console.log(sum)
    }
}
integerPrint()

// 4. Iterate and print array. Iterate through a given array, printing each value.

var myArray = [0,69,420,365]
function printArrayValue(arr){
    for(var i = 0; i < arr.length; i++){
        console.log(arr[i])
    } 
}
printArrayValue(myArray)

// 5. Find and print max. Given an array, find and print its largest element.

var myArray = [0,69,420,365]
function findAndPrintMax(arr){
    var max = arr[0]
        for(var i = 0; i < arr.length; i++){
        if(arr[i] > max){ 
            max = arr[i]
        }
    }
    console.log(max)
}    

findAndPrintMax(myArray)

// 6. Get and print average. Analyze an array's values and print the average.

function findAverage(arr){
    var sum = 0
    for(var i = 0; i < arr.length; i++){
        sum = sum + arr[i]
    }
    console.log (sum/arr.length)
}

findAverage([1013, 619, 327])

// 7. Array with odds. Create an array with all the odd integers between 1 and 255. (inclusive). 

function returnOddsarray(arr){
    var oddsArray = []
    for(i = 1; i <= arr.length; i+=2){
        oddsArray.push(i)
        arr[i] >= 255
            break;
    }
    return oddsArray
}
console.log(returnOddsarray[0,69,420,365,100])



// 8. Square the Values. Square each value in a given array, returning that same array with changed values.

var arr = [0,69,420,365]
function squareArrayValues(arr){
    for(var i = 0; i < arr.length; i++){
        arr[i] = (arr[i]* arr[i])
    }
    console.log(arr)
}
squareArrayValues(arr)

// 9. Greater than Y. Given an array and a value Y, count and print the number of array values greater than Y.

function returnGreaterthatY(arr,y){
    var count = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > y){
        count++
        }
    }
    console.log(count)
}
returnGreaterthatY([0,69,420,365,1000], 50)


// 10. Zero out negative numbers. Return the given array, after seeing any negative values to zero.

function zeroOutArrayNegativeValues(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 0
        }
    }
    return arr
}

console.log(zeroOutArrayNegativeValues([0,69,-420,365,100]))


// 11. Max, Min, Average. Given an array, print the minimum, maximum, and average values for that array.

function maxMinAverage(arr){
    var max = arr[0]
    var min = arr[0]
    var average = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i]
        }
        if(arr[i] < min){
            min = arr[i]
        }
        average += arr[i]
        average / arr.length
    }
    console.log(max,min,average)
}
maxMinAverage([0,69,420,365,1000])


// 12. Shift array values. Given an array, move all the values forward (to the left) by one index, dropping the first value and leaving a 0 (zero) value at the end of the array.

function shiftArrayValuesLeft(arr){
    for(var i = 1; i < arr.length; i++){
        arr[i - 1] = arr[i] 
    }
    arr[arr.length - 1] = 0
    return arr
}
console.log(shiftArrayValuesLeft([0,69,420,365,1000]))

// 13. Swap string for array negative values. Given an array of numbers, replace any negative values with the string 'Dojo'.

function swapStringForArrayNegativeValues(arr){
    for(i = 0; i < arr.length; i++){
        if (arr[i] < 0){
            arr[i] = "Dojo"
        }
    }
    return arr
}
console.log (swapStringForArrayNegativeValues([0,-69,-420,-365,-100]))

