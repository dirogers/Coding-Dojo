class Ninja {
    constructor(name, health, speed = 3, strength = 3) {
    this.name = name;
    this.health = health;
    this.speed = speed;
    this.strength = strength;
    }

    sayName(){
        console.log(this.name);
    }

    showStats() {
        console.log("Name: "+ this.name);
        console.log("Health: " + this.health);
        console.log("Speed: " + this.speed);
        console.log("Strength: " + this.strength);
    }

    drinkSake() {
        this.health += 10;
    }
}

class Sensei extends Ninja {
    constructor(name, health, speed, strength, wisdom = 10) {
        super(name, health, speed, strength);
    }
    speakWisdom(){
        super.drinkSake();
        console.log("What one programmer can do in one month, two programmers can do in two months.");
    }
}

const superSensei = new Sensei("Master Splinter", 200, 10, 10);
superSensei.speakWisdom();
superSensei.showStats();

