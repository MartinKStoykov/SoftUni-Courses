function solve(num1, num2) {
    const factorial = function (x, y) {
        if (y <= 1) {
            return x
        }
        return factorial((x * y), y-1)
    }
    return (factorial(num1, num1-1) / factorial(num2, num2-1)).toFixed(2)
}
console.log(solve(2, 1))