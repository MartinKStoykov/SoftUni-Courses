function operation (numX, numY, operator) {
    
    let result
    switch (operator) {
        case "+": result = numX + numY; break;
        case "-": result = numX - numY; break;
        case "*": result = numX * numY; break;
        case "/": result = numX / numY; break;
        case "%": result = numX % numY; break;
        case "**": result = numX ** numY; break;
    }
    console.log(result)
}

operation(5, 5, "*")