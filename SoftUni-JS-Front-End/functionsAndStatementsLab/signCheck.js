function signCheck(numOne, numTwo, numThree) {
    let numbers = [numOne, numTwo, numThree]
    let minusCount = 0
    for (let i of numbers) {
        if ((i).toString().includes("-")) {
            minusCount += 1
        }
    }
    if ((minusCount === 1) ||(minusCount === 3)) {
        return "Negative"
    }else {
        return "Positive"
    }
}

console.log(signCheck(5, -12, -15))