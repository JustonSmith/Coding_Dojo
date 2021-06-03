import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom'
import HomeScreen from './screens/HomeScreen';
import ProductScreen from './screens/ProductScreen';


function App() {
    return (
        <BrowserRouter>
            <div className="grid-container">
                <header>
                    <div>
                        <a href="/" className="brand" >amazona</a>
                    </div>
                    <div>
                        <a href="/cart" className= ""> Cart </a> &nbsp; |
                        &nbsp; <a href="/signin" className="">Sign In</a>
                    </div>
                </header>
                <main>
                    <Route path="/product/:id" component={ProductScreen}></Route>
                    <Route path="/" component={HomeScreen} exact></Route>
                </main>
                <footer className="row center">
                All Rights Reserved
                </footer>
            </div>
        </BrowserRouter>
    );
}

export default App;
