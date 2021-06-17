// 
// 

// Basic Functions 1:

// Predict the output of the following code snippets. Please DO NOT run any of this code directly, but first predict the output using the T - diagram. Once youve predicted the output for all of the codes, then run the code one by one and compare the two.

// Snippet 1:

function a(){
    return 35;
}
console.log(a())

// console will log 35.

// Snippet 2:

function a(){
    return 4;
}
console.log(a()+a());

// console will log 8.

// Snippet 3:

function a(b){
    return b;
}
console.log(a(2)+a(4));

// Console will log 6.

// Snippet 4:

function a(b){
        console.log(b);
        return b*3;
    }
    console.log(a(3));

// console will log 3 and 9.

// Snippet 5:

function a(b){
    return b*4;
    console.log(b);
}
console.log(a(10));

// The console will log 40.

// Snippet 6:

function a(b){
    if(b<10) {
        return 2;
    }
    else     {
        return 4;
    }
    console.log(b);
}
console.log(a(15));

// The console will log 4.

// Snippet 7:

function a(b,c){
    return b*c;
}
console.log(10,3);
console.log( a(3,10) );

// The console will log 10, 3, and 30.

// Snippet 8:

function a(b,c){
    for(var i=b; i<c; i++){
        console.log(i);
    }
    return b*c;
}
a(0,10);
console.log(a(0,10));

// The console will log 0 - 9 twice.

// Snippet 9:

function a(){
    for(var i=0; i<10; i++){
        i = i +2;
        console.log(i);
    }
}
a();

// The console will log 2, 5, 8, 11.

// Snippet 10:

function a(b){
    for(var i=0; i<10; i++){
        console.log(i);
    }
    return i;
}
console.log(3);
console.log(4);

// The console will log 3 and 4.

// Snippet 11: 

function a(){
    for(var i=0; i<10; i++){
        for(var j=0; j<10; j++){
            console.log(j);
        }
        console.log(i);
    }
}

// The console will log nothing.

// Snippet 12:

var z = 10;
function a(){
    var z = 15;
    console.log(z);
}
console.log(z);

// The console will log 10.

// Snippet 13:

var z = 10;
function a(){
    var z = 15;
    console.log(z);
}
a();
console.log(z);

// The console will log 15 and then 10.

// Snippet 14:

var z = 10;
function a(){
    var z = 15;
    console.log(z);
    return z;
}
z = a();
console.log(z);

// The console will log 15 and then 15.