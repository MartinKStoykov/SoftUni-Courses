function solve() {
    const table = document.querySelector("tbody")
    const inputSection = document.querySelector("textarea")
    const outputSection = document.getElementsByTagName("textarea")[1]
    const generateButton = document.querySelector("button")
    const buyButton = document.getElementsByTagName("button")[1]
    generateButton.addEventListener("click", () => {
        const products = JSON.parse(inputSection.value)
        products.forEach(product => {
            const order = ["name", "price", "decFactor"]
            const row = document.createElement("tr")
            const img = document.createElement("img")
            let cell = document.createElement("td")
            img.src = product["img"]
            cell.appendChild(img)
            row.appendChild(cell)
            const newCheckBox = document.createElement("input")
            for (const element of order) {
                const cell = document.createElement("td")
                const paragraph = document.createElement("p")
                paragraph.textContent = product[element]
                cell.appendChild(paragraph)
                row.appendChild(cell)
            }
            cell = document.createElement("td")
            newCheckBox.type = "checkbox"
            cell.appendChild(newCheckBox)
            row.appendChild(cell)
            table.appendChild(row)
        })
    })
    buyButton.addEventListener("click", () => {
        const rows = table.rows
        let furnitureBought = []
        let totalPrice = 0
        const averageDecoration = [0, 0]
        for (const row of Array.from(rows)) {
            if (row.querySelector("input").checked) {
                furnitureBought.push(row.getElementsByTagName("p")[0].textContent)
                totalPrice += parseInt(row.getElementsByTagName("p")[1].textContent)
                averageDecoration[0] += parseFloat(row.getElementsByTagName("p")[2].textContent)
                averageDecoration[1] += 1
            }
        }
        outputSection.value = `Bought furniture: ${furnitureBought.join(", ")}\nTotal price: ${totalPrice.toFixed(2)}\nAverage decoration factor: ${averageDecoration[0] / averageDecoration[1]}`
    })
}