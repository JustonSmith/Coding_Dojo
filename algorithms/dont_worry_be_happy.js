
// Dont worry be happy. Create a function that calls "good morning!" 98 times.

function beCheerful(){
    for(var i = 1; i <=98; i++)
    console.log("good morning!")
}
beCheerful()

function beCheerful(num){
    for(var i = 0; i <= num; i++){
        console.log("Good Morning!")
    }
}
beCheerful(98)

// Multiples of three, -300 to 0. Skip -3 and -6.


for(var i = -300; i <= 0; i+=3){
    if( i === - 3 || i === -6){
        continue
    }
    else {
        console.log(i)
    }
}

function multsOfThree(){
    for (let i=-300;i<0;i++){
        if(i % 3 == 0 && i !==-3 && i !==-6){
            console.log(i);
            }
        }
    }
multsOfThree()