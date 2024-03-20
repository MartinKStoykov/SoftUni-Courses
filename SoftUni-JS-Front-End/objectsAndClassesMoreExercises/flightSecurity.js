function solve(array) {
    const flights = {}
    const arraySectors = array.shift()
    const arrayStatusChanges = array.shift()
    const arrayFlightStatus = array.shift()
    for (const line of arraySectors) {
        const [sector, destination] = line.split(" ")
        flights[sector] = {"Destination": destination, "Status": "Ready to fly"}
    }
    for (const line of arrayStatusChanges) {
        const [sector, status] = line.split(" ")
        if (flights[sector]) {
            flights[sector]["Status"] = "Cancelled"
        }

    }
    for (const object of Object.keys(flights)) {
        if (flights[object]["Status"] === String(arrayFlightStatus)) {
            console.log(flights[object])
        }
    }
}
