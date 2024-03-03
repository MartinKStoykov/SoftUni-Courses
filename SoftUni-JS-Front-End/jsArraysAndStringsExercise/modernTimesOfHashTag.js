function hashTag(string) {
    let splitWords = string.split(" ")
    for(let word of splitWords) {
        if (/^#[a-zA-Z]+$/.test(word)) {
            console.log(word.split("#")[1])
        }
    }
}

hashTag('Nowadays everyone uses # to tag a #special word in #socialMedia')