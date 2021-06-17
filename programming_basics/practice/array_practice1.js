var lastName = "Smith"
var firstName = "Juston"
var age = 33
var phoneNumber = "940-367-1802"
var eMail = "test@gmail.com"

var test = ["Smith", "Juston", "test@gmail.com", 33]
    console.log(test[2])
    
var meArray = ["Smith", "Juston", "test@gmail.com", 33]
    console.log(meArray)
meArray[4] = meArray[3]
meArray[3] = meArray[2]
meArray[2] = "940-367-1802"
    console.log(meArray)
    