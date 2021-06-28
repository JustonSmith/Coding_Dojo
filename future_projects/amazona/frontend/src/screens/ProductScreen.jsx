import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import LoadingBox from '../components/LoadingBox';
import MessageBox from '../components/MessageBox';
import Rating from '../components/Rating';




const ProductScreen = (props) => {
    const productDetails = useSelector( state => state.productDetails);
    const {loading, error, product} = productDetails;
    return (
        <div>
            { loading ? (
                <LoadingBox></LoadingBox>
            ) : error ? (
                <MessageBox variant="danger">{error}</MessageBox>
            ) : (
        <div>
            <Link to="/" className=""> Back to result </Link>
            <div className= "row top">
                <div className="col-2">
                    <img>
                        className="large"
                        src={product.image} 
                        alt={product.name}
                    </img>
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
                                <div>${product.price}</div>
                                </div>
                            </li>
                            <li>
                                <div className="row">
                                    <div>Status:</div>
                                    <div>
                                        {product.countInStock > 0 ? ( 
                                            <span className= "success"> In Stock</span>
                                        )   :   (
                                            <span className="danger">Unavailable</span>
                                        )}
                                    </div>
                                </div>
                            </li>
                            <li>
                                <button className="primary block">Add to Cart</button>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        )}
        </div>
    );
};

export default ProductScreen;
