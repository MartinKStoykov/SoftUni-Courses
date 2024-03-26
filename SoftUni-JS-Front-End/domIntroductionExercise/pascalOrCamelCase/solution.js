function solve() {
    let input = document.getElementById("text").value
    let requestedCase = document.getElementById("naming-convention").value
    let finalWord = ""
    for (const word of input.split(" ")) {
        if (requestedCase === "Pascal Case") {
            finalWord += word[0].toUpperCase() + word.slice(1).toLowerCase()
        } else if (requestedCase === "Camel Case") {
            if (input.indexOf(word) !== 0) {
                finalWord += word[0].toUpperCase() + word.slice(1).toLowerCase()
            } else {
                finalWord += word.toLowerCase()
            }
        } else {
            finalWord = "Error!"
        }

    }
    const element = document.getElementById("result")
    element.textContent = finalWord
}
