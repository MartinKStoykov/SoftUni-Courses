function meetings(array) {
    const schedule = {}
    for (const line of array) {
        const [day, name] = line.split(" ")
        if (!schedule[day]) {
            schedule[day] = name
            console.log(`Scheduled for ${day}`)
        } else {
            console.log(`Conflict on ${day}!`)
        }

    }
    for (const [day, name] of Object.entries(schedule)) {
        console.log(`${day} -> ${name}`)
    }

}