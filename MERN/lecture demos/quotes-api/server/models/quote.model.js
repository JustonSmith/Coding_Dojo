const mongoose = require('mongoose')

const QuoteSchema = new mongoose.Schema({
    content:{
        type: String,
        required: [true, "Please provide a quote."],
        minLength: [3, "Quote must contain at least three characters."],
        maxLength: [150, "Please select a shorter quote."]
    },
    author: {
        type: String,
        required: [true, "Please provide an author."],
        minLength: [3, "Author name must be at least 3 characters."],
        maxLength: [25, "Please provide a shorter name."]

    },
    quotedOn: {
        type: Date,
        required: [true, "Please provide date."]
    },


    
}, {timestamps: true})


const Quote = mongoose.model("Quote", QuoteSchema);

module.exports = Quote;