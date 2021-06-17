// Arrays Loops and Functions Review    
// [] Square Brackets
// Construct a "for" Loop.
var arr = [1,2,3,4,5]
for(var i = 0; i < arr.length; i++){
    // CODE BLOCK
    console.log(arr[i])
}

var j = 0
while(j < arr.length){
        console.log(arr[j])
        j++
}

// In general, we use 'for' loops when we know how many times a loop should run. We use 'while' loops when we are not sure.

// Write a loop that logs the intetegers 1 throught 255 to the console.

for(var i = 1; i <= 255; i++){0
    console.log(i)
}

var j = 1
while(j <= 255){
    console.log(j)
    j++
}


var favoriteMovies = ["The Princess Bride", "A Fish Called Wanda", "Jaws"]

console.log(favoriteMovies[1])

favoriteMovies.push("One Cut of the Dead")
console.log(favoriteMovies)

favoriteMovies.pop()

// write a finction that, given a movie title, will add to my list of movies.

function addMovie(title){
    favoriteMovies.push(title)
}

addMovie("Anchorman")
addMovie("Die Hard")

console.log(favoriteMovies)

// Write an array. pop two entries. Write a dynamic function to add food when given input.

var favoriteFoods = ["Steak", "Mac N Cheese", "Bacon", "Broccoli", "Lettuce"]

favoriteFoods.pop()
favoriteFoods.pop()
    console.log(favoriteFoods)
    
function addFood(food){
    favoriteFoods.push(food)    }

    addFood("Pizza")

console.log(favoriteFoods)

// Write a function that, given an array, logs "Negative" to the console for every negative number and "positive" for every positive number.

var arr = [7,14,21,-28,-35,-42, "Sludge"]
    function posNeg(arr){
        for(var i = 0; i < arr.length; i++){
            if (typeof(arr[i]) === 'number'){
            if(arr[i] < 0){
                console.log("Negative")
        }
        else{
                console.log("Positive")
        }
    }
        else{
                console.log("Not a number")
            }
        }
    }

    posNeg(arr)



var arr = [2, -5, 9, -10, "Sludge", 5]
    function posNeg(arr){
        for(var i = 0; i < arr.length; i++){
            if (typeof(arr[i]) === 'number'){
                if(arr[i] < 0){
                    console.log("Negative")
                }
                else{
                    console.log("Positive")
                }
            }
            else{
                console.log("Not a number.")
            }
        }
    }
    
    posNeg(arr)

// Write a function that logs every even number from 2 - 20 to the console.

// PSEUDOCODE
// Name the function.
// Start counting every other number starting at 2. 
// End at 20.
// Print each number.

    function evenNum(){
        for(var i = 2; i <= 20; i+=2)
            console.log(i)
    }

    evenNum()

// Write a function that logs every integer to the console starting at 25 down to 0.

    function countdown(){
        for(var i = 25; i >= 0; i--)
            console.log(i)
    }
    countdown()

// Write a function that only logs multiples of 3, from 1 - 100.

    function multiples(){
        for(var i = 1; i <= 100; i++){
            if(i*3 > 100){
                break;
            }
        console.log(i*3)
        }
    }
    multiples()

// Write a function that takes in an array with two numbers as its parameter. Print the first value and return the second.

    function print1srReturn2nd(num1,num2){
        console.log(num1)
        return num2
    }

    print1srReturn2nd(7,13)



// Design a function, that given a string, counts the number of 'E's in that string.

var counter = 0
var string = "Butte stuffe"
function findMyE(string){ 
for(var i=0;i < string.length;i++){
    if(string[i]=="e"||string[i]=="E"){
        console.log("is fun")
        counter++
        continue
        }
}
}
findMyE(string)
console.log(counter)


// Design a function that given an array, returns the counts of number above 15 inside that array.

var butts = [10, 30, 100, 69, 420]
    function bigbutts(butts)
        for(var i = 0; i > butts.length; i++){
            if (butts[i] > 15){
            return i
        }
        return butts
}




// Design a function that given a string, changes each "s" into a "z" or "S" into "Z".

// Design a function that given a string, returns the string backwards.