//
// 
// Rockin’ the Dojo Sweatshirt:
// 
// 
// Ever since you arrived at the Dojo, you wanted one of those cool Coding Dojo sweatshirts – maybe even more than one. Let’s say they cost $20 (including tax), but friendly Josh gives a 9% discount if you buy two, a nice 19% discount if you buy three, or a sweet 35% discount if you buy four or more. He only accepts cash and says he doesn’t have coins, so you should round up to the nearest dollar. Build function sweatshirtPricing(num) that, given a number of sweatshirts, returns the cost.

function sweatShirtPricing(num){
    var cost = 20
    if(num === 1){                                                
        return cost
    }
    else if(num === 2){
        cost = (cost * 2) - (cost * 2 * .09)
            return Math.ceil(cost)
    }
    else if(num === 3){
        cost = (cost * 3) - (cost * 3 * .19)
            return Math.ceil(cost)
    }
    else if(num === 4){
        cost = cost * 4 - (cost * 4 * .35)
            return Math.ceil(cost)
    }
}
console.log(sweatShirtPricing(4))

// 
// 
// ***OR***
// 
// 

function sweatshirtPricing(num){
    var $money= null
    var sweatshirtCost = 20
    if(num == 1){
        $money = sweatshirtCost
    }
    if(num == 2){
        $money = Math.ceil(num*(sweatshirtCost*.91))
    }
    if(num == 3){
        $money = Math.ceil(num*(sweatshirtCost*.81))
    }
    if(num>=4){
        $money = Math.ceil(num*(sweatshirtCost*.65))
    }
    return $money
}
console.log(sweatshirtPricing(2))
