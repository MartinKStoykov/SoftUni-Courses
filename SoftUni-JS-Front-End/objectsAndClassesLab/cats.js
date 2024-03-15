
function cats(array) {
    class Cat {
        constructor(name, age) {
            this.name = name
            this.age = age
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`)
        }

    }
    for (const line of array) {
        const [name, age] = line.split(" ")
        const cat = new Cat(name, age)
        cat.meow()
    }
}

