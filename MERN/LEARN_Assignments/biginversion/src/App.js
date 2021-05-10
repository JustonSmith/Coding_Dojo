import React from 'react';
import './App.css';
import BigInversion from './components/BigInversion';

function App() {
  return (
    <div className="App">
      <BigInversion firstName={"Jack"} lastName={"Black"} age={43} hairColor={"Black"}/>
      <BigInversion firstName={"Harry"} lastName={"Potter"} age={53} hairColor="Brown"/>
      <BigInversion firstName={"Hillary"} lastName={"Duff"} age={64} hairColor={"Blonde"}/>
      <BigInversion firstName={"Randy"} lastName={"Newman"} age={22} hairColor={"White"}/>
    </div>
  );
}

export default App;
