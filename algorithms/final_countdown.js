// 
// 

// The Final Countdown:

// This is based on the "flexible countdown". The parameter names are not as helpful but the problem is essentially identical; dont be thrown off. Given four parameters (param1, param2, param3, param4), print the multiples of param1, starting at param2 and extending to param3. one exception: if a multiple is equal to param4, then skip (dont print) it. Do this using a WHILE loop. Given (3, 5, 17, 9) print 6, 12, 15 (which are all of the multiples of 3 between 5 and 17 and expluding the value 9).

function finalCountDown(num1, num2, num3, num4){
    while(num2 < num3){
    if(num2 % num4 ==! 0){
        if(num2 % num1 === 0){
        console.log(num2)
        }
    }
    num2++
    }
}
console.log(finalCountDown(3, 5, 17, 9))

