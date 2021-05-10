
import React, {useState} from 'react';
import Person from './Person';

const MakePerson = (props) =>{
    const [person, setPerson] = useState(props.people);
    const handleDelete = (delIdx) => {
        const filteredPerson = person.filter((peoples, idx) => {
            return delIdx !== idx;
        });
    
        setPerson(filteredPerson);
    };
    return (
        <div>
            {person.map((personStr, idx)=>{
                return (
                    <div key={idx}>
                        <hr/>
                        <Person>{personStr}</Person>{" "}
                        <button
                            onClick={(event) => {
                                handleDelete(idx);
                            }}
                            >
                            Delete
                        </button>
                    </div>
                );
            })}
            
        </div>
    );
};
export default MakePerson;

