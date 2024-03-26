function search() {
    const townList = document.getElementsByTagName("li")
    const searchedSubstring = document.getElementById("searchText").value
    const matchesFound = document.getElementById("result")
    let count = 0
    for (const town of townList) {
        if (town.textContent.includes(searchedSubstring)) {
            town.style.textDecoration = "underline"
            town.style.fontWeight = "bold"
            count += 1
        }
    }
    matchesFound.textContent = `${count} matches found`
}
