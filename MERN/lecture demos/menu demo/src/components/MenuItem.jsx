import React, { useState } from 'react';


const MenuItem = props => {
    // initialize my state variables.

    const [likesCount, setLikesCount] = useState(props.likes);
    const [dislikesCount, setDislikesCount] = useState(props.likes);




    console.log("*********", props)
    let {name, price, desc, children, likes  } = props
    
    const likeItem = ()=>{
        setLikesCount(likesCount + 1)
    }
    const dislikeItem = ()=>{
        setDislikesCount(dislikesCount + 1)
    }
    
    
    return(
        <span className="text-center">
            <div className= "card">
                <div className= "card-body">
                    <h1 className= "card-title">Name: {name}</h1>
                    <div className= "card-subtitle mb-2 text-muted">
                        {children}
                    </div>
                    <div>
                        <h3>Price: {price}</h3>
                        <p>Description: {desc}</p>
                        <p><button type= "button" className="btn btn-success" onClick={likeItem}>Like</button> Likes: {likesCount} </p>
                        <p><button type= "button" className="btn btn-danger" onClick={dislikeItem}>Dislike</button> Dislikes: {dislikesCount} </p>
                    </div>
                </div>
            </div>
        </span>
    )




    // Class based component:





// class MenuItem extends Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//             likesState: props.likes,
//             dislikesState: 0
//         }
//     }
// render() {
// You can do regular JavaScript here inside the render(){} function body but before the return.
//     console.log("*************",this.props)
// const {name, price, desc, children, likes, dislikes} = this.props
// let likeItem = ()=>{
//     this.setState({likesState: this.state.likesState +1}) 
//     console.log("clicked the like button, this is the likes variable ---->", likes)
// }

// let dislikeItem = ()=>{
//     this.setState({dislikesState: this.state.dislikesState +1}) 
//     console.log("clicked the like button, this is the likes variable ---->", likes)
}
//         return(
//             <span className="text-center">
//                 <div className= "card">
//                     <div className= "card-body">

//                         <h1 className= "card-title">Name: {name}</h1>
//                         <div className= "card-subtitle mb-2 text-muted">
//                         {children}
//                         </div>
//                         <h3>Price: {price}</h3>
//                         <p>Description: {desc}</p>

//                         <p><button type= "button" className="btn btn-success" onClick={likeItem}>Like</button> Likes: {this.state.likesState}</p>
//                         <p><button type= "button" className="btn btn-danger" onClick={dislikeItem}>Dislike</button> Dislikes: {this.state.dislikesState}</p>


//                     </div>
//                 </div>
//             </span>
//         )
//     }
// }



// example of state:




// class LightSwitch extends Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//             position: "On"
//         };
//     }
//     render() {
//         return (
//             <fieldset>
//                 <p>The light is currently { this.state.position }</p>
//                 <button>Flip Switch</button>
//             </fieldset>
//         );
//     }
// }

// export default LightSwitch;

export default MenuItem;