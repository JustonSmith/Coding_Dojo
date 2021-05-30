import React from 'react'
import './App.css';
import {Router, Link} from '@reach/router';
import Register from './components/Register';
import SignIn from './components/SignIn'
import PokemonDetail from './components/PokemonDetail'


function App() {
  return (
    <div className="App">
      {/* {/* <img src="https://cdn2.bulbagarden.net/upload/4/4b/Pok%C3%A9dex_logo.png" alt=""></img> */}
      {/* <a href="/signin">Sign In</a> &nbsp;|| &nbsp;  */}
      <a href="/">Home</a> &nbsp;|| &nbsp;
      <a href="/signup">Sign Up</a>
      <br />
      <Link to="/signin">Sign In</Link> &nbsp;|| &nbsp;
      <Link to="/">Home</Link> &nbsp;|| &nbsp;
      <Link to="/signup">Sign Up</Link>
      <hr className= "w-50"/>
      <Router>
        <Register path="/signup"></Register>
        <SignIn path="/signin"></SignIn>
        <img className="container" path="/" src= "http://assets1.ignimgs.com/2016/05/12/tk2g5hdyx8h6xkq2helcpng-6da69e.png" alt=""></img>
        <PokemonDetail path="pokemon/:pokemonNum"/>
      </Router>

    </div>
  );
}

export default App;
