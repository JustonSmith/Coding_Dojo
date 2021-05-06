// Variables

const daysInAWeek = 7;

var firstName = "Rob";

for(let i = 0; i<firstName.length; i++){
    console.log(i)
}

console.log("**********")
console.log(i)

for var i = 0; i<firstName.length; i++){
    console.log(i)
}

// "var" is able to exist outside the scope of the for loop. "let" only exists within the scope of a code block. (block scoped)


// This is a number.
var number = 1;

//This is a string.
var name = "Benny Bob";

//This is a boolean.
var isWorking = true;

//This is an array with different variable types.
var arr = [1,3,6,"Mr. Nibbles",true];

//This is an object
var dojo = {
    instructors: ["Will","Adrien"],
    numberOfNinjas: 50,
    stack : "MERN"
}

var num = "banana";//This var num is accessible anywhere with in the index file.

function eatBanana(){

     var num = 19; // this var num is only accessible with in the function eatBanana, it is also a different variable than the one declared up above.

    for(let i = 0; i < num; i++){

         // We can print i + num here and get it's value

        console.log(i + num);
    }
     //If we print out i here, we will get a reference error.
    console.log(i);
    if(num == 19)
    {
        let sum = num + num;//sum is only available within the if statement.
    }
}
eatBanana();

// var isn't the only keyword we can use to define variables.
// We can also use let and const.

// There are three different scopes:

// Global - we use var
// Function - we also use var
// Block - we use let and const

// But what about the constkey word?

// The difference between let and const is that const won't be reassigned and let maybe reassigned.

// Hoisting

// It's important to know that hoisting only works on the var key word. let and const do not get hoisted.

// When we declare variables with var, they get hoisted to the top of the file or function.

console.log(name);//This will print out undefined.

function doSomething(){
    console.log(pudding);// This will print out undefined.
    for(let i = 0; i < 10; i++){
        var pudding = "fruity pebbles";
    }
}

var name = "Mr. Nibbles";
console.log(name); // This will print out Mr. Nibbles.

// Destructuring is a fancy expression that allows us to unpack values from arrays and properties from objects into their own distinct variables.

// Array Destructuring
// We can pull variables out of an array and assign them to others in one single line.
// We can also selected which indices we want to pull from by using , when we declare our variables.
// With arrays we can name our new variables anything we want.

var instructors = ["Will","Adrien","Anne","Phil"];

// Old way . . .
var first = instructors[0];
var third = instructors[2];
var fourth = instructors[3];

// or . . . 

// Destructuring syntax
var [first,,third,fourth] = instructors;

// the extra commas indicate index position. For instance, "third" is in position 2.

// Object Destructuring
// With objects we need to call the key names within the destructure brackets in order to pull the values out.

var spaceCrab = {
    name : "Obi WanCrabnobi",
    weapon: "Claw Light Saber",
    isWanted: false,
    spaceCraft : "Aluminum Falcon"
}

// Old way . . . 
var name = spaceCrab.name;
var spaceCraft = spaceCrab.spaceCrab;

// or . . . 

// Destructured syntax 
// These variable names must match up to the key names in the object.
var { name , spaceCraft } = spaceCrab;

// If we want to assign a new variable name
var { ship : spaceCraft } = spaceCrab;

