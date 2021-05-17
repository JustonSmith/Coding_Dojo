import React from 'react';

import {Router} from '@reach/router';
import Home from './components/Home';
import BingBong from './components/BingBong';
import Closing from './components/Closing';


const MixIt = () => {
    return (
        <div>
            <Router>
                <Home path="/home/"/>
                <BingBong path="/:id/"/>
                <Closing path="/:id/:color/:bgColor"/>
            </Router>
        </div>
    );
};



export default MixIt;