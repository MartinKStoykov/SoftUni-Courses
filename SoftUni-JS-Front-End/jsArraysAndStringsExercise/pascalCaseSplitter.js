function caseSplitter(string) {
    let splitWord
    let wordArray = []
    for (let char of string) {
        if (/[A-Z]/.test(char)) {
            wordArray.push(splitWord)
            string = string.replace(splitWord, "")
            splitWord = char
        }else {
            splitWord += char
        }
    }
    wordArray.push(string)
    wordArray.shift(0)
    console.log(wordArray.join(", "))
}

caseSplitter('SplitMeIfYouCanHaHaYouCantOrYouCan')