function solve(char1, char2) {
    let start = char1.charCodeAt(0)
    let end = char2.charCodeAt(0)
    let charactersBetween = []
    if (end < start) {
        let temp = end
        end = start
        start = temp
    }
    for (let i = start+1; i < end; ++i) {
        charactersBetween.push(String.fromCharCode(i))
    }
    return charactersBetween.join(" ")
}

console.log(solve("C", "#"))