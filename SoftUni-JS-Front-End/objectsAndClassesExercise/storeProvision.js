function solve(currentStock, orderedStock) {
    const products = {}
    let currProduct = ""
    for (let i = 0; i < currentStock.length; ++i) {
        if (i % 2 === 0) {
            currProduct = currentStock[i]
        } else {
            products[currProduct] = parseInt(currentStock[i])
        }
    }

    for (let i = 0; i < orderedStock.length; ++i) {
        if (i % 2 === 0) {
            currProduct = orderedStock[i]
        } else {
            if (products[currProduct]) {
                products[currProduct] += parseInt(orderedStock[i])
            } else {
                products[currProduct] = parseInt(orderedStock[i])
            }
        }
    }
    for (const [item, quantity] of Object.entries(products)) {
        console.log(`${item} -> ${quantity}`)
    }
}
