import React, { Component } from 'react';
    
    
class PersonCard extends Component {
    constructor(props){
        super(props);
        this.state = {
            levelUp: props.age
        }
    }
    clickHandler = () => {
        this.setState({
            levelUp: this.state.levelUp + 1
        })
    }
    render() {
        const {firstname, lastname, haircolor} = this.props; 
        return <div>
            <h1>{lastname}, {firstname}</h1>
            <h3>age: {this.state.levelUp}</h3>
            <h3>{haircolor}</h3>
            <button onClick={this.clickHandler}> Birthday button for {firstname} {lastname}</button>
            </div>;
    }
}
    
export default PersonCard;