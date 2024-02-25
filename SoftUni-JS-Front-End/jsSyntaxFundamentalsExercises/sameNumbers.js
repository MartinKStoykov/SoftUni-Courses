function isSameNumber(num) {
    let numberSum = 0;
    let number = num.toString();
    let isSame = true
    for (let i = 0; i < number.length; ++i) {
        numberSum += parseInt(number[i])
        if (number[i] !== number[0]) {
            isSame = false
        }
    }
    if (! isSame) {
        console.log(false)
    }

    if (isSame){
        console.log(true)
    }
    console.log(numberSum)
}

isSameNumber(1234)