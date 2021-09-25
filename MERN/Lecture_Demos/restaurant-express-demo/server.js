// MUST be done in this order:
const express = require("express");
const cors  = require("cors"); 
const port = 8000;



const app = new express();

app.use(cors());
app.use(express.json());
app.use( express.urlencoded({ extended: true}));

const menu = [
    {name: "calamari", price: 12.00, calories: 400},
    {name: "Shrimp Linguine", price: 15.00, calories: 1400},
    {name: "Baked Ziti", price: 50.00, calories: 500},
    {name: "Pizza", price: 18.00, calories: 1000},
    {name: "Angel Hair Pasta with Shrimp", price: 13.00, calories: 700},
]

// creating API endpoints:

app.get("/api/hello", (req, res)=> {
    res.json({message: "...congratulations. This works."})
})


// GET ALL menu items:


app.get("/api/menu", (req,res) => {
    res.json({message: menu})
})


// GET one item:


app.get("/api/menu/:id", (req, res) => {
    if(req.params.id > menu.length-1){
        res.json({result: "Wazzuu talkin bount linguine"})
    }
    else {

    }
    res.json({ result:menu[req.params.id]})
})

// POST one item:

app.post("/api/menu", (req, res) => {
    console.log("*********")
    console.log(req.body)
    console.log("*********")
    menu.push(req.body)
    res.json({message: "...posted"})
})

// PUT (update) one item:


app.put("/api/menu/:id", (req, res) => {
    console.log(req.params.id)
    console.log(req.body)
    menu[req.params.id] = req.body
    res.json({ message: menu})
})


// DELETE one item:


app.delete("/api/menu/:id", (req, res) => {
    menu.splice(req.params.id, 1)
    res.json({message: menu})
})






// code to ensure the server can listen for requests on port 8000:

app.listen(port, ()=> console.log(`...listening on port number ${port}`)
);