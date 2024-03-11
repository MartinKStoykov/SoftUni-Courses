function solve(number) {
    let numbers = number.toString().split("")
    while (true) {
        let total = 0
        for (let i of numbers) {
            total += Number(i)
        }
        if ((total / numbers.length) > 5) {
            return numbers.join("")
        }else (numbers.push("9"))
    }
}

console.log(solve(5835))