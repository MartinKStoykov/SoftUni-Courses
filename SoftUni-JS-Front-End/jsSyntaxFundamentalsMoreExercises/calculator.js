function calculator(operand1, operator, operand2) {
    let result
    switch(operator) {
        case "+": result = operand1 + operand2;break;
        case "-": result = operand1 - operand2;break;
        case "/": result = operand1 / operand2;break;
        case "*": result = operand1 * operand2;break;
    }
    console.log(result.toFixed(2))
}