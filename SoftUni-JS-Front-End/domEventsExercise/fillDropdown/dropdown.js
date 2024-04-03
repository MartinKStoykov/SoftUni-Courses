function addItem() {
    let newItemText = document.querySelector("#newItemText").value
    let newItemValue = document.querySelector("#newItemValue").value
    const newOptionElement = document.createElement("option")
    const menu = document.querySelector("#menu")
    newOptionElement.textContent = newItemText
    newOptionElement.value = newItemValue
    menu.appendChild(newOptionElement)
    newItemValue = document.querySelector("#newItemValue").value = ""
    newItemText = document.querySelector("#newItemText").value = ""
}