import React, { useState } from 'react';
import TinderCard from "react-tinder-card"
import "./TinderCards.css";

function TinderCards() {
// const [people, setPeople] = useState([
    {
        name: "Elon Musk",
        url: " https://s.yimg.com/ny/api/res/1.2/WrPAlgL0M.Np4p7wRVl8.Q--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTU0MA--/https://s.yimg.com/uu/api/res/1.2/JLI.F0NwAcr8_5nN1Lh1jA--~B/aD0xMDgwO3c9MTkyMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/gobankingrates_644/c7819312b1bc81ac7c2d68bd1593e05e"
    },
    {
        name: "Jeff Bezos",
        url: "https://i.guim.co.uk/img/media/332baa8afa46c6ce4696dcf8171f882514ff7f14/0_238_3290_1975/master/3290.jpg?width=445&quality=45&auto=format&fit=max&dpr=2&s=524528e7060d33cfd614ad9637cd2550"
    },
    {
        name: "Mark Cuban",
        url: " https://i.insider.com/5a3bf59d4aa6b509048b680f?width=804&format=jpeg"
    }
]);

    const swiped = (direction, nameToDelete) => {
        console.log("removing " +nameToDelete);
    };

    const outOfFrame = (name) => {
        console.log(name + " left the screen!");
    }

    return (
        <div className="tinderCards">
            <div className="tinderCards_cardContainer">
            {people.map((person) => (
                <TinderCard
                className="swipe"
                key={person.name}
                preventSwipe={["up", "down"]}
                onSwipe={(dir) => swiped(dir, person.name)}
                onCardLeftScreen={() => outOfFrame(person.name)}
                >

                <div
                    style= {{ backgroundImage: `url(${person.url})` }}
                    className="card"
                    >
                    <h3>{person.name}</h3>
                </div>

                </TinderCard>
            ))}
            </div>
        </div>
    )
}

export default TinderCards
