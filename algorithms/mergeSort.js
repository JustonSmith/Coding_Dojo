

let combine = (arr1, arr2) => {
    let result = [],
        leftLen = arr1.length,
        rightLen = arr2.length,
        toThaLeft = 0,
        toThaRight = 0;
    while (toThaLeft < leftLen && toThaRight < rightLen) {
        if (arr1[toThaLeft] < arr2[toThaRight]) {
            result.push (arr1[toThaLeft])
            toThaLeft++
        } else {
            result.push (arr2[toThaRight])
            toThaRight++
        }
    }
    return result.concat(arr1.slice(toThaLeft)).concat(arr2.slice(toThaRight))
}

let mergeSort = (arr) => {
    let len = arr.length
    if (len < 2) {
        return arr
    }
    let middle = Math.floor(len / 2)
        arr1 = arr.slice(0, middle),
        arr2 = arr.slice(middle)
    return mergeSort(mergeSort(arr1), mergeSort(arr2))
}

console.log(combine([4,6,7], [1,3,6,9]))

