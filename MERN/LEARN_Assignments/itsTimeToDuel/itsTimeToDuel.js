

class Player {
    constructor(name) {
        this.name = name
    }
}

class Ninja extends Player {
    constructor(name){
        super(name)
        this.gold = 10
        this.power = 10
        this.resilience = 10
        this.cost = 0
    }
    redBeltNinja() {
        this.cost = 3
        if (this.gold >= this.gold - this.cost) {
            this.gold -= this.cost
            this.power += 3
            this.resilience += 4
            console.log(`${this.name} played the Red Belt Ninja card.`)
        } else {
            console.log("not enough gold.")
        }
    }
    blackBeltNinja() {
        this.cost = 4
        if (this.gold >= this.gold - this.cost) {
            this.gold -= this.cost
            this.power += 5
            this.resilience += 4
            console.log(`${this.name} played the Black Belt Ninja card.`)
        } else {
            console.log("not enough gold.")
        }
    }
}

class cardDuel extends Ninja {
    constructor(name) {
        super(name, 10, 10, 10)
        this.cost = 0
    }
    hardAlgorithm() {
        this.cost = 2
        if (this.gold >= this.gold - this.cost) {
            this.gold -+ this.cost
            this.resilience += 3
            console.log( `${this.name} increased resilience by 3.`)
        } else {
            console.log("not enough gold.")
        }
    }
    pairProgramming(){
        this.cost = 3;
        if (this.coins >= this.coins - this.cost){
            this.coins -= this.cost;
            this.power += 2;
            console.log(`${this.name} incresed their Power by 3`)
        } else {
            console.log("Can not afford card");
        }
    }

    unhandledPromiseRejection(target) {
        this.cost = 3
        if (this.gold >= this.gold - this.cost) {
            this.gold -= this.cost
            this.power += 2
            console.log( `${this.name} increased power by 3`)
        } else {
            console.log("not enough gold.")
        }
    }
    attack(target) {
        target.resilience -= this.power;
        console.log(`${this.name} attacked ${target.name} for ${this.power} damage`)
        if (target.resilience > this.power) {
            console.log(`${target.name} survives attack.`)
        } else {
            console.log(`${target.name} has been defeated.`)
        }
    }
}

const player1 = new cardDuel("Sludge")
console.log(player1)

player1.redBeltNinja()
console.log(player1)

player1.hardAlgorithm()
console.log(player1)

const player2 = new cardDuel ("Slob Dylan")
console.log(player2)

player2.blackBeltNinja()
console.log(player2)

player2.unhandledPromiseRejection(player1)
console.log(player1)

player1.pairProgramming()
console.log(player1)

player1.attack(player2)


