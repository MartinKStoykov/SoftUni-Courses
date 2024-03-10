function solve(number) {
    let numbers = number.toString().split("")
    let evenSum = 0
    let oddSum = 0
    for (let i of numbers) {
        if (i % 2 === 0) {
            evenSum += Number(i)
        }else {
            oddSum += Number(i)
        }
    }
    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`
}

console.log(solve(1000435))