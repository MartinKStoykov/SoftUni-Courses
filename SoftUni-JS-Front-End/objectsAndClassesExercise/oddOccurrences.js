function solve(string) {
    const words = string.split(" ")
    const occurrences = {}
    for (const word of words) {
        if (!occurrences[word.toLowerCase()]) {
            occurrences[word.toLowerCase()] = 0
        }
        occurrences[word.toLowerCase()] += 1
    }
    let oddWords = ""
    for (const [key, value] of Object.entries(occurrences)) {
        if (value % 2 === 1) {
            oddWords += key + " "
        }
    }
    console.log(oddWords)
}

solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')