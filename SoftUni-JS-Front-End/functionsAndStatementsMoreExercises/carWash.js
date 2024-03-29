function solve(array) {
    let percentageClean = 0
    for (let command of array) {
        switch (command) {
            case "soap": percentageClean += 10;break;
            case "water": percentageClean *= 1.20;break;
            case "vacuum cleaner": percentageClean *= 1.25;break;
            case "mud": percentageClean *= 0.90;break;
        }
    }
    console.log(`The car is ${percentageClean.toFixed(2)}% clean.`)

}
