function solve(array) {
    const parkingLot = {}
    for (let line of array) {
        line = line.split(", ")
        if (line[0] === "IN") {
            parkingLot[line[1]] = "IN"
        } else {
            delete parkingLot[line[1]]
        }
    }
    for (const key of Object.keys(parkingLot).sort((a, b) => a.localeCompare(b)))
    console.log(key)
}
