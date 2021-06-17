// 
// 

// Array: Nth-Largest:
// Liam has n number of Green Belt stickers for excellent Python projects. Given array arr and n, return the nth-largest element, where (n-1) elements are larger. Return null if needed.

function nthLargest(arr, num){
    arr.sort()
    if(arr.length <= 2){
        console.log("null")
    }
    if(arr.length > 2){
        console.log(arr[arr.length - num])
    }
}
nthLargest([1, 2, 3, 4, 5, 6], 3)

function nthLargest(arr, num) {
    for (let i = 0; i < num; i++) { // Runs the outer loop as many times as num.
        let maxIdx = i // Must keep track of the index of current max value.
        let temp = arr[i] // Create temp for later swap.

        for (let j = i + 1; j < arr.length; j++) { // Inner loop checks for max value.
            if (arr[j] > arr[maxIdx]) { // Conditional for comparison against current max.
                maxIdx = j // If I find a new max, save the index.
            }
        }

        arr[i] = arr[maxIdx] // Safely overwrite the old max with the new max.
        arr[maxIdx] = temp // Overwrite with saved value.
        console.log(`The array is: ${arr}`)
    }

    console.log(`The ${num}-th largest value is: ${arr[num - 1]}.`)
}

nthLargest([1, 2, 3, 4, 5, 6, 7, 8], 2)