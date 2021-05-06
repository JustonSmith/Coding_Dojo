

function Ninja (name) {
    this.name = name
    this.health = 100
    this.speed = 3
    this.strength = 3

    Ninja.prototype.sayName = () => console.log(`Hello ${this.name}`)

    // Ninja.prototype.sayName = function(){
    //     console.log("Hi my name is "+name+"!");

    Ninja.prototype.showStats = () => console.log(`Name: ${this.name}, Health: ${this.health}, Speed: ${this.speed}, Strength: ${this.strength}`)

    // Ninja.prototype.showStats = function(){
    //     console.log(`Name: ${this.name}, Strength: ${this.strength}, Speed: ${this.speed}, Health: ${this.health}`)

    Ninja.prototype.drinkSake = () => this.health = this.health + 10

    // Ninja.prototype.drinkSake = function(){
    //     this.health = this.health + 10
    }

class Ninja {
    constructor(name) {
        this.name = name
        this.health = 100
        this.speed = 3
        this.strength = 3
    }
    sayName() {
        console.log(`Hiyah! This is ${this.name} - son`)
    }
    showStats() {
        console.log(`Name: ${this.name}, Health: ${this.health}, Speed: ${this.speed}, Strength: ${this.strength}`)
    }
    drinkSake() {
        this.health += 10
    }
}