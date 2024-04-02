function deleteByEmail() {
    const table = document.getElementsByTagName("tbody")[0]
    const rows = table.rows
    const searchedEmail = document.getElementsByName("email")[0]
    const result = document.getElementById("result")
    for (let i = 0; i < rows.length; ++i) {
        if (rows[i].cells[1].textContent === searchedEmail.value) {
            rows[i].remove()
            return result.textContent = "Deleted"
        }
    }
    return result.textContent = "Not found."

}