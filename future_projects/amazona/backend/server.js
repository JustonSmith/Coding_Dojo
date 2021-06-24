import express from 'express';
import data from './data.js'

const app = express();

app.get('/api/products/:id', (req, res) => {
    const product = data.products.find( x => x._id === )
})

app.get('/api/products', (req, res) => {
    res.send(data.products);
});

app.get('/', (req, res) => {
    res.send('server is ready');
});

const port = process.env.PORT || 5000;

app.listen(port, () => {
    console.log(`serve at http://localhost:${port}`);
});

