function sortingNumbers(arr) {
    arr.sort((a,b) => a - b)
    for(let n = 1; n < arr.length; n+=2) {
        arr.splice(n, 0, arr.pop())
    }
    return arr
}

console.log(sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))