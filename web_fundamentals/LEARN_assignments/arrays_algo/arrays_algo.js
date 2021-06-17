//
// 
//  Arrays Algo

// Challenge 1:
// Print values and sum.

function integerPrint(arr){
    var sum = 0
    for(var i = 0; i <= arr.length; i++){
            console.log(i)
            sum = sum + arr[i]
            console.log(sum)
        }
    }
    integerPrint([6, 3, 5, 1, 2, 4])

// Challenge 2:
// Multiply each value in the array by its array position.

function multArray(arr) {
    sum = 0;
    for (let i = 0; i < arr.length; i++) sum += arr[i] * i;
    return sum;
}
console.log(multArray([6, 3, 5, 1, 2, 4]))