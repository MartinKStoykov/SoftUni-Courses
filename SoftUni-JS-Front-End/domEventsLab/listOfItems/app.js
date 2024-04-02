function addItem() {
    const addItemInput = document.getElementById("newItemText")
    const itemList = document.getElementById("items")
    const newItem = document.createElement("li")
    newItem.textContent = addItemInput.value
    itemList.appendChild(newItem)
}