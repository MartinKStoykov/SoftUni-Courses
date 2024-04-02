function solve() {
    const boughtItems = []
    const addButtons = document.querySelectorAll(".add-product")
    const textArea = document.getElementsByTagName("textarea")[0]
    const checkoutButton = document.querySelector(".checkout")
    Array.from(addButtons).forEach(button => {
        button.addEventListener("click", (event) => {
            const price = button.parentNode.parentNode.querySelector(".product-line-price").textContent
            const product = button.parentNode.parentNode.querySelector(".product-title").textContent
            boughtItems.push({product: product, price: parseFloat(price)})

            textArea.textContent += `Added ${product} for ${price} to the cart.\n`
        })
    })
    let listener = true
    checkoutButton.addEventListener("click", (event) => {
        if (!listener) return;
        Array.from(addButtons).forEach(button => {
            button.disabled = true
        })
        let total = 0
        let products = []
        boughtItems.forEach(key => {
            total += key.price
            products.push(key.product)
        })
        textArea.textContent += `You bought ${Array.from(new Set(products)).join(", ")} for ${total.toFixed(2)}.`
        listener = false
    })


}