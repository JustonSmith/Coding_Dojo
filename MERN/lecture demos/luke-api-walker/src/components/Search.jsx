import React, {useState, useEffect} from 'react';
import axios from 'axios';

const Search = () => {

    const [categories, setCategories]= useState([])

    const [formInfo, setFormInfo] = useState({
        category: "",
        id: ""
})

    useEffect(() => {
        axios.get("https://swapi.dev/api/")
            .then(res => {
                console.log("**********")
                console.log(res)
                console.log(Object.keys(res.data))
                setCategories(Object.keys(res.data))
            })
            .catch(err => console.log(err))

        }, [])

        const changeHandler = (event) => {
            console.log("...changing inputs.")
            console.log(event.target)
            setFormInfo({
                ...formInfo,
                [event.target.name]: event.target.value
            })
        }

        const submitHandler = (event) => {
            event.preventDefault();
            console.log("...submitting form.")
        }

    return (
        <div className= "container">
            <form onSubmit={submitHandler} className= "form-inline">
                <div className="input-group">
                    <label htmlFor="">Search for:&nbsp;</label>
                    <select onChange= {changeHandler} name="category" id="" className="form-control">
                        {
                            categories.map((category, i) => {
                                return <option key={i} value={category}>{category}</option>
                            })
                        }
                    </select>
                </div>
                <div className="input-group"> &nbsp; &nbsp;
                    <label htmlFor="">ID:&nbsp;</label>
                    <input onChange={changeHandler} className="form-control" type="number" name="id" />
                </div> &nbsp; | | | &nbsp;
                <input type="submit" value="May the force be with you"/> &nbsp; | | |
            </form>
        </div>
    );
};



export default Search;