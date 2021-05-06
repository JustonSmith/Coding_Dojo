

class Ninja {
    constructor(name) {
        this.name = name
        this.health = 100
        this.speed = 3
        this.strength = 3
    }
    sayName(){
        console.log( `My name is ${this.name}`)
    }
    showStats(){
        console.log(`Name: ${this.name}, Health: ${this.health}, Speed: ${this.speed}, Strength: ${this.strength}`)
    }
    drinkSake(){
        this.health += 10
    }
}

class Sensei extends Ninja {
    constructor(name){
        super(name, 210, 10, 10)
        this.wisdom = 10
    }
    speakWisdom() {
        super.drinkSake()
        console.log("Anger clouds the mind. Turned inward, it is an unconquoerable enemy.")
    }
}

let ninja = new Ninja("Raphael", 100)
ninja.showStats()
ninja.drinkSake()
ninja.showStats()

let sensei = new Sensei("Master Splinter")
sensei.showStats()
sensei.speakWisdom()
sensei.showStats()