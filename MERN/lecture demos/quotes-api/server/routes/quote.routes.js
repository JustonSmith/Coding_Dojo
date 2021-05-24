// const UserController = require('../controllers/user.controller');
// enables routes file to talk to the controller:
const QuoteController = require('../controllers/quote.controller')


module.exports = app => {
app.get("/api/quotes", QuoteController.findAllQuotes)
app.post("/api/quotes/create", QuoteController.createQuote)
app.get("/api/quotes/:_id", QuoteController.findOneQuote)
app.put("/api/quotes/update/:_id", QuoteController.updateOneQuote)
app.delete("/api/quotes/delete/:_id", QuoteController.deleteQuote)
}



//   module.exports = app => {
//     app.get('/api/users' UserController.findAllUsers);
//     app.get('/api/users/:id' UserController.findOneSingleUser);
//     app.get('/api/users/:id' UserController.updateExistingUser);
//     app.get('/api/users' UserController.createNewUser);
//     app.get('/api/users/:id' UserController.deleteAnExistingUser);
// }