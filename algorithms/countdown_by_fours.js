// Countdown by Fours:
// Log positive numbers starting st 2016, counting down by fours (exclude 0) without a FOR loop:

function countdownByFours(){
    var i = 2016
    while (i = 2016){
        console.log(i)
        i -= 4
        if (i <= 0){
            break
        }
    }
}
countdownByFours()


// Flexible Countdown:
// Based on earlier "Countdown by Fours" given lowNum, highNum, mult; print multiples of mult from highNum down to lowNum using a FOR loop. for (2, 9, 3) print 9, 6, 3 (on sucessive lines):

function flexCountdown(highNum, lowNum, mult){
    for(var i = highNum; i > lowNum; i--){
        if( i % mult === 0)
        console.log(i)
    }
}
flexCountdown(0, 20, 2)

