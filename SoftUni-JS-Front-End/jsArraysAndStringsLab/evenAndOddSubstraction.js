function evenOddSum(array) {
    let evenSum = 0
    let oddSum = 0
    for(let i = 0; i<array.length; ++i) {
        if (Number(array[i]) % 2 === 0) {
            oddSum += Number(array[i])
        }else {
            evenSum += Number(array[i])
        }
    }
    console.log(oddSum - evenSum)
}