// Setting and swapping

function setAndSwap (arr){
    for(i = 0; i < arr.length; i++){
        if (arr[i] = 42){
            arr[i] = "Juston Smith"
        }
        else if (arr[i] !== 42){
            arr[i] = "Fourty Two"
        }
    }
    return arr
}
console.log (setAndSwap([42, 24, 42, 24, 42]))

// Print -52 to 1066

function printIntegers(){
    for(var i = -52; i <= 1066; i++){
        console.log(i)
    }
}
printIntegers()