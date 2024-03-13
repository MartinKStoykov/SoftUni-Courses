function solve(array) {
    let goal = array.shift()
    for (let crystal of array) {
        console.log(`Processing chunk ${crystal} microns`)
        let count = 0
        while (crystal !== goal) {
            if (crystal / 4 >= goal-1) {
                crystal /= 4
                count += 1
                if (crystal / 4 >= goal-1) {
                    continue
                }
                console.log(`Cut x${count}`)
                crystal = Math.floor(crystal)
                console.log("Transporting and washing")
                count = 0
            }else if (crystal * 0.80 >= goal-1) {
                crystal *= 0.80
                count += 1
                if (crystal * 0.80 >= goal-1) {
                    continue
                }
                console.log(`Lap x${count}`)
                crystal = Math.floor(crystal)
                console.log("Transporting and washing")
                count = 0
            }else if (crystal - 20 >= goal-1) {
                crystal -= 20
                count += 1
                if (crystal - 20 >= goal-1) {
                    continue
                }
                console.log(`Grind x${count}`)
                crystal = Math.floor(crystal)
                console.log("Transporting and washing")
                count = 0
            }else if (crystal - 2 >= goal-1) {
                crystal -= 2
                count += 1
                if ((crystal - 2 >= goal-1)) {
                    continue
                }
                console.log(`Etch x${count}`)
                crystal = Math.floor(crystal)
                console.log("Transporting and washing")
                count = 0
            }else if (crystal + 1 === goal) {
                crystal += 1
                count += 1
                console.log(`X-ray x${count}`)
            }
        }
        console.log(`Finished crystal ${crystal} microns`)
    }
}

solve([1000, 4000, 8100])