import React, { Component } from 'react';
    
    
class PersonCard extends Component {
    render() {
        console.log(this.props.lastname)
        return <div>
            <h1>{this.props.lastname}, {this.props.firstname}</h1>
            <h3>{this.props.age}</h3>
            <h3>{this.props.haircolor}</h3>
            </div>;
    }
}
    
export default PersonCard;