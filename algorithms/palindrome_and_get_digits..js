function getDigits(str) {
    let newString = ''
    for(let i = 1; i <str.length; i++){
        if(str[i] >= 0 && str[i] <= 9){
            newString += str[i]
        }
    }
    return newString
}
console.log(getDigits('z4d2g5s2'))

// should log 4252

function isPalindrome(str) {
    let newString = ''
    for( let i = str.length - 1; i >= 0; i--){
        newString += str[i]
    }
    if(str === newString){
        return true
    }
        return false
}
console.log(isPalindrome('Tuesday'))
// false

console.log(isPalindrome('tacocat'));
// true