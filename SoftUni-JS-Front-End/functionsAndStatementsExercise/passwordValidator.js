function solve(password) {
    let regexAlNum = /^[a-zA-Z0-9]+$/
    let array = password.split("")
    let incorrectPassword = false
    let numberCount = 0
    if ((password.length < 6)||(password.length > 10)) {
        incorrectPassword = true
        console.log("Password must be between 6 and 10 characters")
    }
    if (!regexAlNum.test(password)) {
        incorrectPassword = true
        console.log("Password must consist only of letters and digits")
    }
    for (let i of array) {
        if (!isNaN(i)) {
            numberCount += 1
        }
    }
    if (numberCount <= 1) {
        incorrectPassword = true
        console.log("Password must have at least 2 digits")
    }
    if (!incorrectPassword) {
        console.log("Password is valid")
    }
}

solve('My12Pass')
