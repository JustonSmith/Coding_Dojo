// Validations
// Validating new entries for Mongoose models is a breeze. Let's say, for our users we wanted to make the first name, last name, and the email required. We can add our validation in Mongoose Model like this:

import { Mongoose } from "mongoose";

const UserSchema = new Mongoose.Schema(
    {
        first_name: {
            type: String,
            required: [true, "First name is required"],
            minlength: [2, "First name must be at least 2 characters long"]
        },
        last_name: {
            type: String,
            required: [true, "Last name is required"],
            minlength: [, "Last name must be at least 2 characters long"]
        },
        age: {
            type: Number,
            min: [1, "You must be at least 1 year old to register"],
            max: [150, "You must be at most 149 years old to register"]
        },
        email: {type: String, required:[true, "Email is required"]}
    },
    { timestamps: true }
);

// What you'll notice is that the validation methods in Mongoose are pretty one-dimensional; we pretty much have to validate things using optional parameters in our schema definition. Making required fields is easy, but more intricate validations (email strings, dates, etc) can get ugly. We can validate our data just fine, but the code gets kind of messy. That's a bummer, but there are some things that JavaScript isn't very good for, and this is one of them. To make life a little easier, Mongoose has added a lot of new validation options to help us validate many options.
