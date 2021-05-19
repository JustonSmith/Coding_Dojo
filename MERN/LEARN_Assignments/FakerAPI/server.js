const express = require("express");
const cors = require("cors");
var faker = require('faker');
const port = 8000;
const app = express();

app.use(cors());
app.use(express.json());

class User {
    constructor() {
        this._id = faker.finance.routingNumber(),
        this.firstName  = faker.name.firstName(),
        this.lastName = faker.name.lastName(),
        this.phoneNumber = faker.phone.phoneNumber(),
        this.email = faker.internet.email(),
        this.password = faker.finance.creditCardNumber()
    }
}

class Company {
    constructor() {
        this._id = faker.datatype.uuid()
        this.name = faker.company.companyName()
        this.address = {
            street: faker.address.streetName(),
            city: faker.address.cityName(),
            state: faker.address.state(),
            zipCode: faker.address.zipCode(),
            country: faker.address.country()
        }
    }
}

const company1 = new Company()
console.log(company1._id)
console.log(company1.name)
console.log(company1.address)

const user1 = new User()
console.log(user1._id)
console.log(user1.firstName)
console.log(user1.lastName)
console.log(user1.phoneNumber)
console.log(user1.email)
console.log(user1.password)




app.get("/api/hello", (req, res) => {
    console.log("******")
    console.log("...hello. ");
    res.json({message: "...hello."})
})

// console.log(faker.address.city())
// console.log(faker.animal.horse())

app.get("api/user/new", (req, res) => {
    const user1 = new User()
    return res.json({result: user1})
})

app.get("/api/companies/new", (req, res) => {
    const company1 = new Company()
    return res.json({ result: company1})
})

app.get("api/user/company", (req, res) => {
    const user1 = new User()
    const company1 = new Company()
    return res.json({
        newcompany:company1,
        newuser: user1
    })
})



app.listen(port, () => console.log(`...they're listening. ...port ${port}`))