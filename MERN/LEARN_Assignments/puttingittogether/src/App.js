import './App.css';
import PersonCard from './components/PersonCard';

function App() {
  return (
    <div className="App">
      <h1>Hello. Welcome to Person Card.</h1>
      <PersonCard lastname= {"Doe"} firstname= {"Jane"} age= {45} haircolor= {"Black"}></PersonCard>
      <PersonCard lastname= {"Smith"} firstname= {"John"} age= {88} haircolor= {"Green"}></PersonCard>
      <PersonCard lastname= {"Fillmore"} firstname= {"Millard"} age= {50} haircolor= {"Brown"}></PersonCard>
      <PersonCard lastname= {"Smith"} firstname= {"Maria"} age= {62} haircolor= {"Blonde"}></PersonCard>
    </div>
  );
}

export default App;
