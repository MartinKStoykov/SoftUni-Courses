function solve(array) {
    for (const line of array) {
        let [town, latitude, longitude] = line.split(" | ")
        latitude = parseFloat(latitude).toFixed(2)
        longitude = parseFloat(longitude).toFixed(2)
        let townData = {
            town,
            latitude,
            longitude,
        }
        console.log(townData)
    }
}

solve(['Sofia | 42.696552 | 23.32601',
    'Beijing | 39.913818 | 116.363625']
)