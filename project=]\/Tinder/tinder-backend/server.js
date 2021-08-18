import express from 'express';
import mongoose from 'mongoose';

// App config
const app = express();
const port = process.env.PORT || 8001


// Middlewares

// DB config

// API endpoints
app.get("/", (req, res) => res.status(200).send("Tinder clone y'all."));

// Listener
app.listen(port, () => console.log(`listening on localhost: ${port}`));

