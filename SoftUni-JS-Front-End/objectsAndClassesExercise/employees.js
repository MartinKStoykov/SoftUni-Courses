function solve(array) {
    const people = {}
    for (const name of array) {
        people[name] = name.length
    }
    for (const [person, number] of Object.entries(people)) {
        console.log(`Name: ${person} -- Personal Number: ${number}`)
    }
}