function solve(array) {
    const searchedWords = array.shift().split(" ")
    const words = {}
    for (const word of searchedWords) {
        words[word] = 0
    }
    for (const string of array) {
        for (const word of searchedWords) {
            if (string === word) {
                words[word] += 1

            }
        }
    }
    for (const [key, value] of Object.entries(words).sort((a, b) => b[1] - a[1])) {
        console.log(`${key} - ${value}`)
    }
}

solve([
        'this sentence',
        'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ]
)