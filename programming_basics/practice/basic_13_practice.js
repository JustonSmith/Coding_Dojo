// Square the values.

function squareArrayVals(arr){
    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i] * arr[i]
    }
    return arr
}
console.log(squareArrayVals([0,69,420,365,1000]))

// Print and find max.

function printMaxOfArray(arr){
    var max = arr[0]
    for(var i = 1; i < arr.length; i++){
        if (arr[i] > max){
            max = arr[i]
        }
    } 
    return max
}
console.log(printMaxOfArray([0,69,420,365,1000]))

// Min, Max, Average.

function printMinMaxAverage(arr){
    var min = arr[0]
    var max = arr[0]
    var sum = arr[0]
    for(var i = 1; i < arr.length; i++){
        if (arr[i] > max){
            max = arr[i]
        }
        if (arr[i] < min){
            min = arr[i]
        }
        sum += arr[i]
        var average = sum / arr.length 
    }
    return[max, min, average] 
}
console.log(printMinMaxAverage([0,69,420,365,1000]))

// Return odds array.

function returnOddsArray(arr){
    var array = []
    for(var i = 1; i <= 255; i += 2){
        array.push(i)
    }
    return array
}
console.log(returnOddsArray())

// Print odds 1 - 255.

function printOdds1to255(){
    for(var i = 1; i <= 255; i += 2){
        console.log(i)
    }
}
printOdds1to255()

// Square the values.

function squareArrayVals(arr){
    for(var i = 0; i < arr.length; i++){
    arr[i] = arr[i] * arr[i]
    }
    return arr
}
console.log(squareArrayVals([0,69,420,356,1000]))

// Get and print average.

function printAverageOfArray(arr){
    var sum = arr[0]
    for(var i = 0; i < arr.length; i++){
        sum += arr[i]
        average = sum / arr.length
    }
    return average
}
console.log(printAverageOfArray([0,69,420,365,1000]))

// Print 1 to 255.

function print1To255(){
    for(var i = 1; i <= 255; i++){
        console.log(i)
    }
}
print1To255()

// Print integers and sum from 1 to 255.

function printIntegersAndSum(){
    var sum = 0
    for(var i = 0; i <= 255; i++){
        console.log(i)
        sum += i
        console.log(sum)
    }
}
printIntegersAndSum()

// Iterate and print an array.

function printArrayVals(arr){
    for(var i = 0; i < arr.length; i++){
        console.log(arr[i])
    } 
}
printArrayVals([0,69,420,365,1000])

// Return array count greater than Y.

function greaterThanY(arr,y){
    var count = 0
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > y)
        count++
    }
    return count
}
console.log(greaterThanY([0,69,420,365,1000],0))

// Zero out negative numbers in an array.

function zeroNegativeValues(arr){
    for(var i = 0; i <arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 0
        }
    }
    return arr
}
console.log(zeroNegativeValues([0,69,-420,365,1000]))

// Shift array values left.






