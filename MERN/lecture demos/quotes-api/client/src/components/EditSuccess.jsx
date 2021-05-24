import React from 'react';
import {Link} from '@reach/router';

const EditSuccess = () => {
    return (
        <div>
            <div className="container w-50">
            <hr />
            <br />
            <br />
            <br />
            <h1 className="">- Success! Your quote has been edited! -</h1>
            <br />
            <Link to = {"/"} className="card-link" >- See All Posted Quotes -</Link> &nbsp; &nbsp;
            <Link to ={"/quotes/new"} className= "card-link">- Create Another Quote -</Link>
        </div>
        </div>
    );
};



export default EditSuccess;