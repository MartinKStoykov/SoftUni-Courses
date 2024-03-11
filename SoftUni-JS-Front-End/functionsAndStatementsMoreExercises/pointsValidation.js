function solve(array) {
    let x1 = array[0]
    let y1 = array[1]
    let x2 = array[2]
    let y2 = array[3]
    let value = "invalid"
    if (Number.isInteger(Math.sqrt(x1 **2 + y1**2))) {
        value = "valid"
    }
    console.log(`{${x1}, ${y1}} to {0, 0} is ${value}`)
    value = "invalid"
    if (Number.isInteger(Math.sqrt(x2**2 + y2**2))) {
        value = "valid"
    }
    console.log(`{${x2}, ${y2}} to {0, 0} is ${value}`)
    value = "invalid"
    if (Number.isInteger(Math.sqrt((x2 - x1)**2 + (y2 - y1)**2))) {
        value = "valid"
    }
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${value}`)
}

solve([2, 1, 1, 1])