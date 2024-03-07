function mathPower(number, power) {
    if (power === 2) {
        return (number* number)
    }else {
        return number * mathPower(number, power -1)
    }
}
console.log(mathPower(2, 8))