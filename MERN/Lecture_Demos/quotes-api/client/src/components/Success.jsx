import React from 'react';
import {Link} from "@reach/router"


const Success = () => {
    return (
        <div className="container w-50">
            <hr />
            <br />
            <br />
            <br />
            <h1 className="">- Success! Your quote has been posted! -</h1>
            <br />
            <Link to = {"/"} className="card-link" >- See All Posted Quotes -</Link> &nbsp; &nbsp;
            <Link to ={"/quotes/new"} className= "card-link">- Create Another Quote -</Link>
        </div>
    );
};



export default Success;