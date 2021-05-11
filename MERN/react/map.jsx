// Working with lists (arrays in JavaScript) is a big part of a developer's life. Accordingly, we'll often need to iterate through arrays of data and render some JSX for each item. While some frameworks supply framework-specific ways to loop through arrays, React instead leans on a built-in array method: map. Let's briefly cover how the map method works. Consider the following code snippet:

const nums = [1, 2, 3, 4, 5];

const newNums = [];

for(let i = 0; i < nums.length; i++) {
    newNums.push( nums[i] * 2 );
}

console.log( newNums ); // logs [2, 4, 6, 8, 10]

// While this works, it isn't very clean. Note that we had to create the local variable i as an iterator to reference the appropriate index in the array. Also, we continuously mutated the newNums array. In recent years, functional programming has become increasingly popular. Although we're not going to take a detour into functional programming, the functional paradigm holds that functions should have the following characteristics:

// Let's see how we could accomplish the above using the map method for arrays in JavaScript.

const nums = [1, 2, 3, 4, 5];

function double(num) {
    return num * 2;
}

const newNums = nums.map( double );

console.log( newNums ); // logs [2, 4, 6, 8, 10]

// We created a pure and transparent function that will always return double the supplied argument, given that the argument is a number. Next, we create a new constant variable called newNums that is assigned to the result of invoking the map method on nums with an argument of double. Notice that we were able to pass in the entire definition of double when we called map. Functions are "first-class citizens" in JavaScript: that is, they can be passed around in the same way as other values. In general, you can use the map method whenever you want to transform each element of an array according to a function. An important thing to note is that the result of calling the map method is a new array; it doesn't change the original.



