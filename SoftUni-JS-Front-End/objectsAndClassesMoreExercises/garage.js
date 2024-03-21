function solve(carArray) {
    const garages = {}
    let carCount = 1
    for (const carInfo of carArray) {

        const [garageNum, info] = carInfo.split(" - ")
        const carDetails = info.split(", ")
        for (const line of carDetails) {
            const [key, value] = line.split(": ")
            if (!garages[garageNum]) {
                garages[garageNum] = {}
            }
            if (!garages[garageNum][carCount]) {
                garages[garageNum][carCount] = {}
            }

            garages[garageNum][carCount][key] = value

        }
        carCount += 1
    }
    for (const [key1, value1] of Object.entries(garages)) {
        console.log(`Garage № ${key1}`);
        for (const [key2, value2] of Object.entries(value1)) {
            console.log(`---${Object.entries(value2).map((k) => ` ${k[0]} - ${k[1]}`)}`)
        }
    }
}

solve(['1 - color: blue, fuel type: diesel', '1 - color: red, manufacture: Audi', '2 - fuel type: petrol', '4 - color: dark blue, fuel type: diesel, manufacture: Fiat'])