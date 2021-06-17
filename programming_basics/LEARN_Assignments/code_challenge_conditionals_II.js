// 
// 
// CODE CHALLENGE: Conditionals II
// 
// 
// As a dilligent student, I want to reward myself if I finish my homework. Based on the time of day, I want either a latte if its before 10am, I want hot chocolate if its between 10 and 4pm, and I want ice cream between 4pm and 10pm. If its after 10pm, I dont want anything but sleep!


// Feature 3:


// PSEUDOCODE:
// Design a function (homeworkReward())
// IF its before 10AM, we want to log "Latte".
// IF its between 10AM and 4PM, we want to log "Hot Chocolate".
// IF its between 4pm and 10PM, we want to log "Ice Cream". 
// IF its after 10PM we want to log "Sleep".
// Or ELSE my homework isnt finished.

function homeworkReward(arr){
    if(arr[1] === true){
        if(arr[0] < 1000){
            return 'latte'
        }
        else if(arr[0] >= 1000 && arr[0] <= 1600){
            return 'hot chocolate'
            }
        else if(arr[0] >= 1600 && arr[0] <=2200){
            return 'ice cream'
        }
        else if(arr[0] >= 2200){
            return 'sleep'
        }
        else{
            return 'Youre not finished yet'
        }
    }
}
console.log(homeworkReward([1700, true]))


// Feature 1:
// Building off the MVP, if I'm up for ice cream, I want strawberry if its Wednesday, otherwise i want Vanilla.

// PSEUDOCODE
// I need to introduce a new IF/ELSE block (nested within my 'ice cream' IF block) to my function that tells me to log 'strawberry' if the correct index number in the array is 'Wednesday', and to log 'vanilla' if it says anything else. 


function homeworkReward(arr){
    if(arr[2] === true){
        if(arr[0] < 1000){
            return 'latte'
        }
        else if(arr[0] >= 1000 && arr[0] <= 1600){
            return 'hot chocolate'
        }
        else if(arr[0] >= 1600 && arr[0] <=2200){
            if(arr[1] === 'Wednesday'){
                return 'strawberry ice cream'
            }
            else{
                return 'vanilla ice cream'
            }   
        }
        else{
            return 'sleep'
        }
    }
    else{
        return 'Youre not finished yet'
    }
}
console.log(homeworkReward([1700, 'Wednesday', true]))


// 
// 
// Feature 2: Building off feature 1, I want to adjust the current conditions and add a new option so that if the time is between 3 and 6pm, I pick either ice cream or hot chocolate depending on if its odd or even. 

// PSEUDOCODE
// I need to add a new option that, (given times equal to 1500 and equal to or less than 1800), chooses either 'hot chocolate' or 'ice cream'.
// Choice is based on an odd or even time.


function homeworkReward(arr){
    if(arr[2] === true){
        if(arr[0] < 1000){
            return 'latte'
        }
        else if(arr[0] >= 1000 && arr[0] <= 1600){
            return 'hot chocolate'
        }
        else if(arr[0] > 1500 && arr[0] < 1800){
            if(arr[0] % 2 === 0){
                return 'hot chocolate'
                }
            else if(arr[0] > 1500 && arr[0] < 1800){
                if(arr[0] % 2 === 1){
                    return 'ice cream'
                }
            }
        }
        else if(arr[0] >= 1600 && arr[0] <=2200){
            if(arr[1] === 'Wednesday'){
                return 'strawberry ice cream'
            }
            else{
                return 'vanilla ice cream'
            }   
        }
        else{
            return 'sleep'
        }
    }
    else{
        return 'Youre not finished yet'
    }
}
console.log(homeworkReward([1731, 'Wednesday', true]))