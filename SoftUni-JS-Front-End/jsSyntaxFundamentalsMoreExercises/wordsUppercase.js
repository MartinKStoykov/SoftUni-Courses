function makeUppercase(string) {
    let words = string.match(/\w+/g);
    let result = []
    for (let i = 0; i < words.length; ++i) {
        result.push(words[i].toUpperCase())
    }
    console.log(result.join(", "))
}

makeUppercase('Hi, how are you?')