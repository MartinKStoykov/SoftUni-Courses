function solve(num1, num2, num3) {
    let smallestNumber = Infinity
    for (let i of [num1, num2, num3]) {
        if (i < smallestNumber) {
            smallestNumber = i
        }
    }
    console.log(smallestNumber)
}

solve(2, 5, 3)