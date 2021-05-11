import React, { useState } from 'react';
import './App.css';
import BoxMaker from './components/BoxMaker';

function App() {
  return (
    <div className="App">
      <h1>Box Generator</h1>
      <p>Pick the color and size of your boxes</p>
      <BoxMaker/>
    </div>
  );
}

export default App;
