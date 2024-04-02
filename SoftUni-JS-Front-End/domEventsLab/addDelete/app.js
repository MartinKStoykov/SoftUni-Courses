function addItem() {
    const addItemInput = document.getElementById("newItemText")
    const itemList = document.getElementById("items")
    const newItem = document.createElement("li")
    const deleteButton = document.createElement("a")

    deleteButton.setAttribute("href", "#")
    newItem.textContent = addItemInput.value
    deleteButton.textContent = "[Delete]"
    newItem.appendChild(deleteButton)
    itemList.appendChild(newItem)
    deleteButton.addEventListener("click", () => newItem.remove())

}
