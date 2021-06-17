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