function calc() {
    const inputNumber1 = document.getElementById("num1")
    const inputNumber2 = document.getElementById("num2")
    const sumOutputSection = document.getElementById("sum")

    sumOutputSection.value = parseInt(inputNumber1.value) + parseInt(inputNumber2.value)

}
