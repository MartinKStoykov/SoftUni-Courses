function extractText() {
    const listItems = document.getElementById("items").textContent
    const inputSection = document.getElementById("result")

    inputSection.value = listItems
}