// 
// 
// What is a two - dimensional array? (2D) = NESTED ARRAY
// A two - dimensional array is an array that contains arrays as its elements.
// 
// What is a two - dimensional loop? = NESTED LOOP 


var my2DArray = [[1, -2, 3], [-4, 5, 6], [7, 8, -9]]

// Zero out negative array values in a two - dimensional array.

console.log(my2DArray[0][1])

function zeroOutNegArrayVals(arr){
    for(var i = 0; i < arr.length; i++){
        for(var j = 0; j < arr.length; j++){ 
            if(arr[i][j] < 0){
                arr[i][j] = 0
            }
        }
    }
    console.log(arr)
}


// Print Max of Array (2D Array)
// printMaxOf2DArray(arr)
// Given a two - dimensional array, find and print its larges element.

function printMaxOf2DArray(arr){
    var max = arr[0][0]
    for (var i = 0; i < arr.length; i++){
        console.log("i is " + i)
        for (var j = 0; j < arr[i].length; j++){
            console.log("j is " + j)
            if (arr[i][j] > max){
                console.log("In the if block.")
                max = arr[i][j]
            }
        }
    }
    console.log(max)
}

var twoDArray = [[4, -2, 300, 1, 999], [4, -2, 300, 1, 1000]]
printMaxOf2DArray(twoDArray)


// Algorithim Challenge: Push Front
// pushfront(arr,val)
// Given an array and a value, insert this value at the beginning of the array. Do this without using any built in array methods.

// For example; pushFront([5, 93, 22, 4]) should return [100, 5, 93, 22, 4]

// PSEUDOCODE
// Design a function named pushFront that accepts two parameters - an array and a value.
// ([5, 93, 22, 4],100) to [100, 5, 93, 22, 4]




function pushFront(arr,val){
    for(var i = arr.length - 1; i >= 0; i++){
        arr[i + 1] = arr[i]
    }
    arr[0] = val
    console.log(arr)
}
pushFront([5, 93, 22, 4],100)


// Algorithm Challenge: Insert At.
// insertAt(arr,idx,val)
// Given an array, insert the value of                       

function insertAt(arr, idx, val){
    for(var i = arr.length - 1; i >= 0; i--){
        arr[i+1] = arr[i]
    }
    arr[idx] = val
    console.log(arr)
}
insertAt([5, 93, 22, 4], 100)





