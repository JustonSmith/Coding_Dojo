import Trip from './components/Trip.png';
import './App.css';
import Bio from './components/Bio'
import Calender from './components/Calender'
import {Router, Link} from '@reach/router'


function App() {
  return (
    <>
      <div className="App">
        <br></br>
        <img className="Trip" src= {Trip} alt="logo" height="200px" width="200px"></img>
        <img className="mr-5 ml-5" src="https://www.metal-archives.com/images/3/5/4/0/3540359789_logo.png?3933" alt="" height="200px" width="600px"></img>
        <img className="Trip" src={Trip} alt="" height="200px" width="200px"></img>
        <br></br>
        <hr/>
        <Link to="/store" className= "">store</Link> 
        <Link to="/media" className= "ml-5">media</Link> 
        <Link to= "/bio" className= "ml-5">bio</Link> 
        <Link to="/calender" className= "ml-5">calender</Link> 
        <Link to="/press" className="ml-5">press</Link>
        <Link to="/" className="ml-5">home</Link>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <img className="border border-primary rounded mr-1" src="https://scontent-dfw5-2.xx.fbcdn.net/v/t1.18169-9/18119232_1544493425595499_9193281935273504420_n.jpg?_nc_cat=108&ccb=1-3&_nc_sid=8bfeb9&_nc_ohc=lBZB-_xMCl0AX_Tv8WS&_nc_ht=scontent-dfw5-2.xx&oh=408489312c7390daaf55d20c1678f88c&oe=60D89F0B" alt="" height="180px"></img>
        <img className="border border-primary rounded mr-1" src="https://scontent-dfw5-1.xx.fbcdn.net/v/t1.6435-9/68351135_2737493902962106_5228391271424327680_n.jpg?_nc_cat=109&ccb=1-3&_nc_sid=8bfeb9&_nc_ohc=nBozrxk_qJcAX_g5miQ&_nc_ht=scontent-dfw5-1.xx&oh=dc62a61dfc37e703a5e1565fbd2b333c&oe=60D8856B" alt="" height="180px"></img>
        <img className="border border-primary rounded mr-1" src="https://scontent-dfw5-2.xx.fbcdn.net/v/t1.6435-9/72439999_10156651213818106_7584474866741411840_n.jpg?_nc_cat=107&ccb=1-3&_nc_sid=8bfeb9&_nc_ohc=ANp2XDzFPwsAX_EH5fW&_nc_ht=scontent-dfw5-2.xx&oh=7b2f206feda2936b39502d6535f15f92&oe=60D8B692" alt="" height="180px"></img>
        <img className="border border-primary rounded mr-1" src="https://scontent-dfw5-2.xx.fbcdn.net/v/t1.6435-9/91323735_3258907894154035_2904947877073649664_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=8bfeb9&_nc_ohc=8R3FI2OQctUAX_eHmrj&_nc_ht=scontent-dfw5-2.xx&oh=7ab2a9b400ec560a3e12d6e516c6d80c&oe=60D5F26F" alt="" height="180px"></img>
        <img className="border border-primary rounded mr-1" src="https://scontent-dfw5-1.xx.fbcdn.net/v/t31.18172-8/19468018_10213528079938961_4421553233100915395_o.jpg?_nc_cat=103&ccb=1-3&_nc_sid=cdbe9c&_nc_ohc=92QEtGk-48kAX_wIZWW&_nc_ht=scontent-dfw5-1.xx&oh=6f48aa30ae54cc7f0a8561f4d80309d3&oe=60D7392B" alt="" height="180px"></img>
        <img className="border border-primary rounded mr-1" src="https://scontent-dfw5-2.xx.fbcdn.net/v/t1.6435-9/53003689_10218916442168484_8236945716866449408_n.jpg?_nc_cat=104&ccb=1-3&_nc_sid=730e14&_nc_ohc=evL5xlP6BFoAX8Wz0VV&_nc_ht=scontent-dfw5-2.xx&oh=9803348eddf4f3f0cc205fc5124b8c1b&oe=60D527E3" alt="" height="180px"></img>
        <img className="border border-primary rounded mr-1" src="https://scontent-dfw5-2.xx.fbcdn.net/v/t1.6435-9/65012952_2637921889585975_2914882686185111552_n.jpg?_nc_cat=104&ccb=1-3&_nc_sid=8bfeb9&_nc_ohc=CRhJmrYzOSIAX_kb_8l&_nc_ht=scontent-dfw5-2.xx&oh=963535af39cdcd94cec57d38608567fa&oe=60D7368E" alt="" height="180px"></img>
        <br />
        <br />
        <br />
        <Router>
          <Bio path= "/bio"></Bio>
            <Calender path= "/calender"></Calender>
        </Router>
        <br></br>
        <div className="Intro">
          <h1>...The spectacle before us was indeed sublime ...</h1>
          <br></br>
          <h3 className= "container w-50">"...we had reached a great height in the atmosphere, for the sky was a dead black, and the stars had ceased to twinkle. By the same illusion which lifts the horizon of the sea to the level of the spectator on a hillside, the sable cloud beneath was dished out, and they seemed to float in the middle of an immense dark sphere, whose upper half was strewn with silver. Peering down into the dark gulf below, I could see a ruddy light streaming through a rift in the clouds."</h3>
        <br></br>
        <br></br>
        <br></br>
        <h1>... Look towards the sky for The Mothership ...</h1>
        </div>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <img src="" alt=""></img> // instagram icon
        <img src="" alt=""></img> // twitter icon
        <img src="" alt=""></img> // facebook icon
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
      </div>
    </>
  );
}

export default App;
