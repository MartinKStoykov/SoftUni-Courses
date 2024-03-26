function subtract() {
    const number1 = document.getElementById("firstNumber").value
    const number2 = document.getElementById("secondNumber").value
    const result = document.getElementById("result")

    result.textContent = parseFloat(number1) - parseFloat(number2)
}