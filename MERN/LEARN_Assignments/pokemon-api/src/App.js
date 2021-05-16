import React, { useState } from 'react';
import './App.css';


import FetchPokemonButton from './components/FetchPokemonButton'
import PokemonDisplay from './components/PokemonDisplay'


function App() {
  const [pokemon, setPokemon] = useState([])

  return (
    <div className="App container">
      <FetchPokemonButton pokemon = {pokemon} setPokemon = {setPokemon} />
      <PokemonDisplay pokemon = {pokemon} />

    </div>
  );
}

export default App;
