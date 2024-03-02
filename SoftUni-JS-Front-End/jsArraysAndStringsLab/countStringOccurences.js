function countStringOccurences(text, word) {
    let count = 0
    let words = text.split(" ")
    for(let string of words) {
        if (string === word) {
            count +=1
        }
    }
    console.log(count)
}
