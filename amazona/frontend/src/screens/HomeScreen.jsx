import React from 'react';
import Data from '../Data';
import Product from '../components/Product'

const HomeScreen = () => {
    return (
        <div>
            <div className="row center">
                {Data.products.map((product) => (
                    <Product key={product._id} product= {product}></Product>
                ))}
            </div>
        </div>
    );
};

export default HomeScreen;