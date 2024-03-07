function repeatString(string, count) {
    if (count === 1) {
        return string
    } else {
        return string + repeatString(string, count-1)
    }
}
console.log(repeatString("abc", 3))