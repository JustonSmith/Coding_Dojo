// allows this file to talk to models.
const { request } = require("express");
const Quote = require("../models/quote.model");

module.exports.findAllQuotes = (req, res) => {
    Quote.find()
        .then(allQuotes => {
            res.json({results: allQuotes})
        })
        .catch(err => {
            res.json(err)
        })
    }

module.exports.createQuote = (req, res) => {
    console.log("...request body.", req.body)
    Quote.create(req.body)
        .then(newQuote=>{
            res.json({results: newQuote})
        })
        .catch(err => {
            console.log(err)
            res.json(err)
        })
    }

module.exports.findOneQuote = (req, res) => {
    Quote.findOne({_id: req.params._id})
        .then(oneQuote=> {
            res.json({results: oneQuote})
        })
        .catch(err =>{
            console.log(err)
            res.json(err)
            })
    }

module.exports.updateOneQuote = (req, res) => {
    Quote.findOneAndUpdate({_id: req.params._id},
        req.body, 
        {new:true, runValidators:true}
        )
        .then(updatedQuote => {
            res.json({results: updatedQuote})
        })
        .catch(err => {
            console.log(err)
            res.json(err)
        })
    }

module.exports.deleteQuote = (req, res) => {
    Quote.deleteOne({
        _id: req.params._id
        })
        .then(deletedQuote => {
            res.json({results: deletedQuote})
        })
        .catch(err => {
            console.log(err)
            res.json(err)
        })
    }