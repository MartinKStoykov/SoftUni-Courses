function login(array) {
    let username = array[0]
    let password = username.split("").reverse().join("")
    for (let i = 1; i < array.length; ++i) {
        if (array[i] !== password) {
            if (i === 4) {
                console.log(`User ${username} blocked!`)
                break
            }
            console.log("Incorrect password. Try again.")

            continue
        }
        console.log(`User ${username} logged in.`)
    }
}