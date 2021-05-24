const express = require("express")
const app = express();
const port = 8000;
const cors = require("cors")


app.use(express.json()); //allows us to use json
app.use(express.urlencoded({extended: true})); // allows the parsing of json
app.use(cors())


// creating API endpoints

// app.get("/api/sup", (req, res) => {
//     res.json({
//         message: "Sup playa? You got this shiz workin'. Gimme some quotes my dude."
//     })
// })


// require our other modularized files(routes and config).
require("./server/config/quote.config")
require("./server/routes/quote.routes")(app)



// make it so that our server can listen for requests on port 8000
app.listen(port, ()=>console.log(`...the server is listening on port number ${port}.`));