function howMuchLeftoverCake(){
    var numberOfPieces = 12
    var numberOfPeople = 5
    var remainingCake =  numberOfPieces% numberOfPeople
    if(remainingCake =0){
        return ("No leftovers for you!")
    }
    if (remainingCake<=2){
        return ("you have some left overs")
    }
    if (remainingCake>=3||remainingCake<=5){
        return ("You have leftovers to share")
    }
    else {
        return ("hold another party")
    }
}
console.log(howMuchLeftoverCake())