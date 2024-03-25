function sumTable() {
    const sum = document.getElementById("sum")
    const table = document.getElementsByTagName("table")[0]
    const rows = table.rows

    let totalSum = 0
    for (let i = 1; i < rows.length-1; ++i) {
        const cells = rows[i].cells
        totalSum += parseFloat(cells[1].textContent)
    }
    let sumSection = document.getElementById("sum")
    sumSection.textContent = totalSum.toString()
}