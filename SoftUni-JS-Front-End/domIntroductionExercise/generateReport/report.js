function generateReport() {
    const table = document.getElementsByTagName("table")[0]
    const requestedSections = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    const outputSection = document.getElementById("output")
    const sectionNames = {}
    const employeeData = []
    for (let i = 0; i < 1; ++i) {
        const row = table.rows[i]
        for (let j = 0; j < row.cells.length; ++j) {
            const cell = row.cells[j]
            if (cell.querySelector("input").checked) {
                sectionNames[j] = cell.querySelector("input").name
                requestedSections[j] = 1
            }
        }
    }
    for (let i = 1; i < table.rows.length; ++i) {
        const row = table.rows[i]
        let info = {}
        for (let j = 0; j < row.cells.length; ++j) {
            const cell = row.cells[j]
            if (requestedSections[j]) {
                const sectionName = sectionNames[j]
                info[sectionName] = row.cells[j].textContent
            }

        }
        employeeData.push(info)
    }
    outputSection.textContent = JSON.stringify(employeeData)
}