function solve(number) {
    let total = 0
    for (let i = 0; i < number; ++i) {
        if (number % i === 0) {
            total += i
        }
    }
    if (total === number) {
        return "We have a perfect number!"
    }else {
        return "It's not so perfect."
    }
}

console.log((solve(1236498)))