import './App.css';
import AllQuotes from './components/AllQuotes';
import QuoteDetails from './components/QuoteDetails';
import Create from './components/Create';
import Edit from './components/Edit';
import Success from './components/Success';
import EditSuccess from './components/EditSuccess';
import {Router, Link} from "@reach/router";

function App() {
  return (
    <div className="App">
      <br/>
      <h1>-- Famous Quotes --</h1>
      <Link to="/">- Home -</Link> &nbsp;| | &nbsp;
      <Link to= "/quotes/new">- New Quote -</Link> &nbsp; 
      <Router>
        <>
          <AllQuotes path= "/"></AllQuotes>
          <Create path="quotes/new"></Create>
          <Edit path= "/quotes/edit/:_id"></Edit>
          <Success path="quotes/success"></Success>
          <EditSuccess path="quotes/editsuccess"></EditSuccess>
          <QuoteDetails path = "/quotes/:_id"></QuoteDetails>
        </>
      </Router>
    </div>
  );
}

export default App;
