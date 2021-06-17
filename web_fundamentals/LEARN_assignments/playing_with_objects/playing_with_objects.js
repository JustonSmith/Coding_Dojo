// 
// 

// Playing With Objects:

// practice iterating through an array of objects/dictionaries.
// Imagine that you are given an array of objects, for example:

var users = [
        {
            name: "Michael",
            age: 37
        },
        {
            name: "John",
            age: 30
        },
        {
            name: "David",
            age: 27
        }
    ];

// How would you print/log John's Name?

console.log(users[1].name)

// How would you prin/log the name of the first object?

console.log(users[0].name)

// How would you print/log the name and age of each user using a for loop? 

for(var user in users){
    console.log(users.name.age)
}

