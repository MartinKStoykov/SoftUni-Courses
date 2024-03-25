function extract(content) {
    const pageText = document.getElementById(content)
    const matchedWords = pageText.textContent.matchAll(/\(([a-zA-Z ]+)\)/g)
    return [...matchedWords].join("; ")
}

let text = extract("content");