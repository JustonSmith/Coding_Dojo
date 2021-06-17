// Algorithm Challenge: Min to Front
// minToFront(arr)
// Given an array of comparable values, move the lowest element to array's front, shifting backward any elements previously ahead of it. Do not otherwise change the array's order. 

//  Given [4, 2, 1, 3, 5], change it to [1, 4, 2, 3, 5].

// For example: minToFront([5, 93, 22, 4]) should return [4, 5, 93, 22]

function minToFront(arr){
    var min = arr[0]
    var minIdx = 0
    for (var i = 0; i < arr.length; i++){
        if (arr[i] < min){
            min = arr[i]
            minIdx = i
        }
    }
    for (var j = minIdx; j < arr.length; j++){
        arr[j] = arr[j+1]
    }
    arr.pop()
    pushFront(arr, min)
    console.log(arr)
}