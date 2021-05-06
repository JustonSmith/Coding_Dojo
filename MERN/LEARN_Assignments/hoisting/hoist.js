

// JavaScript Hoisting Assignment

// 1. 
var hello = 'world';
console.log(hello);

// undefined

// 2. 
var needle = 'haystack';
var needle = 'magnet';
function test(){

    test();
    console.log(needle);
}
console.log(needle);

// magnet

// 3.
var brendon = 'super cool';
function print(){
    brendan = 'only okay';
    console.log(brendan);
}
console.log(brendan);

// super cool

// 4.
var food = 'chicken';
console.log(food);
eat();
function eat(){
    food = 'half-chicken';
    var food = 'gone';
}
console.log(food);

// chicken, half-chicken

// 5. 
mean();
console.log(food);
var mean = function() {
    food = "chicken";
    console.log(food);
    var food = "fish";
    console.log(food);
}
console.log(food);

// I'm not sure. Code seems broken.

// 6.
console.log(genre);
var genre = "disco";
rewind();
function rewind() {
    genre = "rock";
    console.log(genre);
    var genre = "r&b";
    console.log(genre);
}
console.log(genre);

// undefined, rock, r&b, disco

// 7. 
var dojo = "burbank";
console.log(dojo);
function learn() {
learn();
    dojo = "seattle";
    console.log(dojo);
    dojo = "san jose";
    console.log(dojo);
}
console.log(dojo);

// burbank, seattle, san jose

// 8.
console.log(makeDojo("Chicago", 65));
console.log(makeDojo("Berkeley", 0));
function makeDojo(name, students){
    const dojo = {};
    dojo.name = name;
    dojo.students = students;
    if(dojo.students > 50){
        dojo.hiring = true;
    }
    else if(dojo.students <= 0){
        dojo = "closed for now";
    }
    return dojo;
}

// console.log(makeDojo("Chicago", 65));
const dojo = {};
dojo.name = 'Chicago';
dojo.students = 65;
dojo.hiring = true;

console.log(makeDojo("Berkeley", 0));
const dojo = {};
dojo.name = 'Berkeley';
dojo.students = 0;
dojo = 'closed for now'; // returns an error because you 
                         // can't assign a value to const
