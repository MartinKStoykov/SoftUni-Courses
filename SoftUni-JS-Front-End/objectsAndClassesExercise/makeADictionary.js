function solve(array) {
    const dictionary = {}
    for (const line of array) {
        const words = line.split("\"")
        const term = words[1]
        const definition = words[3]
        dictionary[term] = (`Term: ${term} => Definition: ${definition}`)
    }
    for (const [key, value] of Object.entries(dictionary).sort((a, b) => a[0].localeCompare(b[0]))) {
        console.log(value)
    }
}


solve([
        '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
        '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
        '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
        '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
        '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}'
    ]
)