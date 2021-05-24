const mongoose = require('mongoose');
const db_name = "quotes_db"

mongoose.connect(`mongodb://localhost/${db_name}`, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
    .then(() => console.log('I mean. yeah. JoJo and stuff..'))
    .catch(() => console.log('Something went wrong when connectiong to the database.', err))