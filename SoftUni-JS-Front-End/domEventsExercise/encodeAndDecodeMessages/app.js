function encodeAndDecodeMessages() {
    const encodeTextArea = document.getElementsByTagName("textarea")[0]
    const decodeTextArea = document.getElementsByTagName("textarea")[1]
    const encodeButton = document.getElementsByTagName("button")[0]
    const decodeButton = document.getElementsByTagName("button")[1]
    encodeButton.addEventListener("click", () => {
        decodeTextArea.value = encodeTextArea.value
            .split("")
            .map(char => String.fromCharCode(char.charCodeAt(0)+1))
            .join("")
        encodeTextArea.value = ""
    })
    decodeButton.addEventListener("click", () => {
        decodeTextArea.value = decodeTextArea.value
            .split("")
            .map(char => String.fromCharCode(char.charCodeAt(0)-1))
            .join("")
    })
}