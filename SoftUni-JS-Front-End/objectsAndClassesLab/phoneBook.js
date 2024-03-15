function phoneBook(array) {
    const phoneBook = {}
    for (const line of array) {
        let [name, number] = line.split(" ")
        phoneBook[name] = number
    }
    for (const [name, number] of Object.entries(phoneBook)) {
        console.log(`${name} -> ${number}`)
    }
}

phoneBook(['Tim 0834212554',
    'Peter 0877547887',
    'Bill 0896543112',
    'Tim 0876566344']
)