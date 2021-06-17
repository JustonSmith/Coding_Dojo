// Parens Valid
// Create a function that, given an input string, returns a boolean whether parentheses in that string are valid. Given input "y(3(p)p(3)r)s", return true. Given "n(0(p)3", return false. Given "n)0(t(0)k", return false.

// Pseudocode:
// create a function
// function given an input string []. 
// function returns a boolean. Which means there will be a conditional. 
// IF given input *this*, return True. ELSE IF given *that* return false. ELSE IF given *that* return false. 
//

// EX 1. 

function parensValid2(str){
    var countOpenParens = 0
    var countClosedParens = 0
    var read
    for(var i = 0; i<str.length; i++)
        read = str[i];
        if (read == '('){
            countOpenParens++
        }
        if (read == ')'){
            countClosedParens++
        }
    if(countOpenParens == countClosedParens){
        return true;
    }
    else
        return false;

}