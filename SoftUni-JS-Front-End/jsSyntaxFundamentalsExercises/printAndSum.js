function sum(numX, numY) {
    numbers = []
    numberSum = 0
    for (let i = numX; i <= numY; ++i) {
        numbers.push(i)
        numberSum += i
    }
    console.log(numbers.join(" "))
    console.log(`Sum: ${numberSum}`)
}

sum(5, 10)