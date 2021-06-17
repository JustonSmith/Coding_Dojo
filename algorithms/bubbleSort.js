let bubbleSort = (inputArr) => {
    let len = inputArr.length;
    let swapped;
    do {
        swapped = false;
        for (let i = 0; i < len; i++) {
            if (inputArr[i] > inputArr[i + 1]) {
                let temp = inputArr[i];
                inputArr[i] = inputArr[i + 1];
                inputArr[i + 1] = temp;
                swapped = true;
            }
        }
    } while (swapped);
    return inputArr;
}

console.log(bubbleSort([4,7,2,3,1,9,8]))