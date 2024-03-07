function simpleCalculator(numberA, numberB, operator) {
    function calculation(operator, a, b) {

        const operations = {
            "multiply": (a, b) => a * b,
            "divide": (a, b) => a / b,
            "add": (a, b) => a + b,
            "subtract": (a, b) => a - b,
        }
        return operations[operator](a, b)
    }
    return calculation(operator, numberA, numberB)
}