import React, {useState, useEffect} from 'react';
import axios from 'axios';



const PokemonDetail = (props) => {
    console.log("logging props here")
    const [pokemonInfo, setPokemonInfo] = useState({})

    useEffect(() => {
        axios.get(`https://pokeapi.co/api/v2/pokemon/${props.pokemonNum}`)
        .then(res=>{
            console.log("*******")
            console.log(res)
            setPokemonInfo(res.data)
        })
        .catch(err=>{
            console.log(err)
        })
    }, [])
    
    return (
        <div>
            <h1>You chose {pokemonInfo.name}!</h1>
            {pokemonInfo.sprites?
            <>
                <img height="250px" src={pokemonInfo.sprites.front_shiny} alt=""/>
                <h3>Abilities:{}</h3>
            </>
            
            
            
            
            :"pokemon not found" }
        </div>
    );
};


export default PokemonDetail;