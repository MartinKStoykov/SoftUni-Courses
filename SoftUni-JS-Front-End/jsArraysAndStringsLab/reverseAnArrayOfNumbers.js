function reverseArray(number, array) {
    let reversedArray = []
    for(let i = 0; i<number; ++i) {
        reversedArray.push(array[i])
    }
    console.log(reversedArray.reverse().join(" "))
}
