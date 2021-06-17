// 
// 
// 
// DECODER RING CHALLENGE:

function DecoderRing(codeArray) {
    var alphabet = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    var decodedString = ""
    for(let i=0; i<code.length; i++){
        decodedString+=alphabet[code[i]]
    }
    console.log(decodedString)
}
var code = [8, 5, 12, 12, 15, 0, 23, 15, 18, 12, 4]
DecoderRing(code)

function encoderRing(string){
    var alphabet = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
var numArr = []
for(var i = 0; i < string.length; i++){
    for(var j = 0; j < alphabet.length; j++){
