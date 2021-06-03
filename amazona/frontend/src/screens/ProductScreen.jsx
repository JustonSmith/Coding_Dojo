import React from 'react';
import Product from '../components/Product';
import Data from '../Data';



const ProductScreen = (props) => {
    const product = Data.products.find((x) => x._id === props.match.params.id);
    if(!product){
        return <div> Product Not Found</div>;
    }
    return (
        <div>
            <div className= "row">
                <div className="col-2">
                    <img className="large" src={product.image} alt={product.name}/>
                </div>
                <div className="col-1">
                    <ul>
                        <li>
                            <h1>{product.name}</h1>
                        </li>
                        <li>
                            <Rating 
                                rating={product.rating}
                                numReviews={product.numReviews}
                            ></Rating>
                        </li>
                        <li>
                            Price: ${product.price}
                        </li>
                        <li>
                            Description:
                            <p>{product.description}</p>
                        </li>
                    </ul>
                </div>
                <div className= "col-1">
                    <div className= "card card-body">
                        <ul>
                            <li>
                                <div className="row">
                                <div>Price</div>
                                <div>{product.description}</div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>

            </div>
        </div>
    );
};

export default ProductScreen;

