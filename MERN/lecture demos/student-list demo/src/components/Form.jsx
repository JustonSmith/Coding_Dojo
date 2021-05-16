
// import React and {useState}.
import React, {useState} from 'react';
import styling from './Form.Module.css'


// state variable to store the form information as an object.{}. These names MUST match the names of the inputs in the form. 
const Form = () => {
    const [formInfo, setFormInfo] = useState({
        firstName:"",
        lastName:"",
        profilePicture:"",
        favoriteColor:"",
        description:"",
        numberOfBelts:"",
    })


    // state variable to store the SUBMITTED form information into an array.[{}{}{}]
    const [allStudents, setAllStudents] = useState([])


    // changeHandler handles onChange events in the form. Ex: typing in the form. onChange is called in the input of the form. This is a synthetic event or an event listener. Make sure to use the spread operator (...) after setter.
    const changeHandler = (event)=> {
        console.log("...typing in the form.")
        console.log(event.target.name)
        console.log(event.target.value)
        setFormInfo({
            ...formInfo,
            [event.target.name]: event.target.value
        })
    }


    // submitHandler handles onSubmit events in the form. onSubmit is called inside the form tag. This is a synthetic event or an event listener.
    const submitHandler = (event)=> {
        event.preventDefault()
        console.log("...form has been submitted")
        // now i want the array containing all the form submissions. (aka all the students) to add this new form information. Make sure to use [] inside setter's parenthesis, and the spread (...) operator.
        setAllStudents([...allStudents, formInfo])

        // reset the form to be empty.
        setFormInfo({
            firstName:"",
            lastName:"",
            profilePicture:"",
            favoriteColor:"",
            description:"",
            numberOfBelts:"",
        })
    }
    // delete student with the splice method using spread.
    const deleteStudent = (event, idxnum) => {
        console.log("...deleting student.", idxnum)
        // let students = [...allStudents]
        // students.splice(idxnum, 1)
        // setAllStudents(students)

        // delete student using the .filter method.
        let result = allStudents.filter((student, idx)=>{
            return idx !== idxnum
        })
        setAllStudents(result)
    }



    // the form should be inside the return parenthesis.
    return (
        <div className="container">
            <div >
                <br />
                <h3 className= {styling.title}>Add a student below:</h3>
                <br />
                <div className= {styling.newstudent}>
                    <form onSubmit={submitHandler}> 
                        <div className="form-group">
                            <label htmlFor="">First Name</label>
                            <input onChange={changeHandler} name="firstName" type="text" className="form-control" value= {formInfo.firstName}/>
                        </div>
                        <div className="form-group">
                            <label htmlFor="">Last Name</label>
                            <input onChange={changeHandler} name="lastName" type="text" className="form-control"value= {formInfo.lastName}/>
                        </div>
                        <div className="form-group">
                            <label htmlFor="">Upload Profile Picture</label>
                            <input onChange={changeHandler} name="profilePicture" type="text" className="form-control"value= {formInfo.profilePicture}/>
                        </div>
                        <div className="form-group">
                            <label htmlFor="">Favorite Color</label>
                            <input onChange={changeHandler} name="favoriteColor" type="text" className="form-control"value= {formInfo.favoriteColor}/>
                        </div>
                        <div className="form-group">
                            <label htmlFor="">Description</label>
                            <textarea onChange={changeHandler} name="description" id="" cols="30" rows="10" className="form-control"value= {formInfo.description}></textarea>
                        </div>
                        <div className="form-group">
                            <label htmlFor="">Number of Belts</label>
                            <select onChange={changeHandler} name="numberOfBelts" id="" className="form-control"value= {formInfo.numberOfBelts}>
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                            </select>
                        </div>
                        <button type="submit" className="btn btn-primary">Submit</button>
                    </form>
                    <hr />
                    <hr />
                    <hr />
                </div>
            <div/>
        <div/>
                {



                // This is where you iterate with .map to make the results of the form appear on the page. 
                allStudents.map((student,idx)=>{
                    let size = ""
                    student.numberOfBelts >2? size="big": size="small"

                    return(
                        <span key={idx} className= "text-center">
                            <div className={`card ${styling.studentCard}`} style = {{backgroundColor: student.favoriteColor, width: student.numberOfBelts>2? "100%":"50%"}}>
                                <img className={styling.profilePicture} src={student.profilePicture} alt="profile pic" height="200" width="200"/>
                                <h4 className="card-title">{student.firstName} {student.lastName}</h4>
                                <div className="card-body">
                                    <p className="card-text">
                                    {student.description}
                                    </p>
                                    <p>Favorite color: {student.favoriteColor}</p>
                                    <p>Number of belts: {student.numberOfBelts}</p>
                                    <p>Index number: {idx} </p>
                                    <button onClick={event => deleteStudent(event, idx)}>Remove</button>
                            </div>
                            </div>
                        </span>)
                    })  
                }
            </div>
        </div>
    );
};


export default Form;