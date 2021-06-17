

// greater than Y.

function greaterThanY(arr, y){
    var count = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > y){
        count++
        }
    }
    console.log(count)
}
greaterThanY([69, 420, 365, 1000], 50)
// 
// 
console.log(Math.random()*13)

// Get and print average.

function printAverageOfArray(arr){
    var sum = 0
    for(var i = 0; i < arr.length; i++){
        sum = sum + arr[i]
    }
    console.log(sum / arr.length)
}
printAverageOfArray([69,420,365,1000])
// 
// 
console.log(Math.random()*13)

// Print Odds 1 - 255.

function printOdds1To255(){
    for(var i = 1; i <= 255; i+=2){
        console.log(i)
    }
}
printOdds1To255()
// 
// 
console.log(Math.random()*13)

// Square the Values.

function squareArrayVals(arr){
    for( var i = 0; i < arr.length; i++){
        arr[i] = (arr[i] * arr[i])
    }
    console.log(arr)
}
squareArrayVals([69,420,365,1000])
// 
// 
console.log(Math.random()*13)

// Iterate and Print Array.

function printArrayVals(arr){
    for(var i = 0; i <arr.length; i++){
        console.log(arr[i])
    }
}
printArrayVals([69, 420, 365, 1000])
// 
// 
console.log(Math.random()*13)

// Array with Odds.

function returnOddsArray(){
    var oddsArray = []
    for(var i = 1; i <= 255; i+=2){
        oddsArray.push(i)
    }
    return oddsArray
}
console.log(returnOddsArray())
// 
// 
console.log(Math.random()*13)

// Print 1 to 255.

function print1To255(){
    for(var i = 1; i <= 255; i++){
        console.log(i)
    }
}
print1To255()
// 
// 
console.log(Math.random()*13)

// Zero Out Negative Numbers.

function zeroNegVals(arr){
    for(var i = 0; i < arr.length; i++){
        if (arr[i] < 0){
            arr[i] = 0
        }
    }
    return arr
}
console.log(zeroNegVals([-1, -2, -3, -4, -5]))
// 
// 
console.log(Math.random()*13)

// Find and print max.

function printMaxOfArray(arr){
    var max = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i]
        }
    }
    return arr
}
console.log(printMaxOfArray([1, 2, 3, 4, 5]))
// 
//  

console.log(Math.random()*13)

// Array with Odds.

function returnOdds(){
    var array = []
    for(var i = 1; i < 255; i+=2){
        array.push(i)
    }
    return array
}
console.log(returnOdds())
// 
// 

console.log(Math.random()*13)

// Greater than Y.

function greaterThanY(arr, y){
    var count = 0
    for(var i = 1; i < arr.length; i++){
        if(arr[i] > y){
            count++
        }
    }
    console.log(count)
}
greaterThanY([1,2,3,4,5], 0)
// 
// 

console.log(Math.random()*13)

// Square the Values.

function squareArrayValues(arr){
    for(var i = 0; i < arr.length; i++){
        arr[i] = (arr[i] * arr[i])
    }
    console.log(arr)
}
squareArrayValues([2,4,6,8,10])

// Max Min Average

function maxMinAvg (arr){
    var max = arr[0]
    var min = arr[0]
    var sum = 0
    for(var i = 1; i < arr.length; i++){
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
maxMinAvg([0, 69, 420, 365, 1000])
// 
// 

console.log(Math.random()*13)

//  


