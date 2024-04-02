function focused() {
    const sections = document.querySelectorAll("input")
    Array.from(sections)
        .forEach(inputSection => inputSection
        .addEventListener("focus", (event) => {
        event.target.parentNode.className = "focused"
    }))
    Array.from(sections)
        .forEach(inputSection => inputSection
        .addEventListener("blur", (event) => {
        event.target.parentNode.className = ""
        }))

}