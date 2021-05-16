// import './App.css';
import MenuItem from './components/MenuItem';
function App() {
  return (
    <div className="App">
      <h1 className= "text-center">Hello Everybody, welcome to the MERN restaurant. </h1>
      <br/>
      <MenuItem name= {"Calamari"} price= {12.50} desc= {"Its grass fed tho."} likes= {0}>
        <p>*Gluten free</p>
        <p>*Contains nuts</p>
      </MenuItem>
      <MenuItem name= {"Basil Salmon Salad"} price= {200} desc= {"The basil comes from the deep trenches of Java, its grass fed, and its data type is FreeRange."} likes= {0}/>
      <MenuItem name= {"Nepali treats from my fam"} price= {12.00} desc = {"Rob be alvin and the chipmunks in week 3 after eating this."} likes={10}/>
      
    </div>
  );
}

export default App;
