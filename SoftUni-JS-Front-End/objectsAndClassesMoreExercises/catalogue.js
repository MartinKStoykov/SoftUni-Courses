function solve(array) {
    const catalogue = {}
    for (const line of array) {
        const [product, price] = line.split(" : ")
        if (!catalogue[product[0]]) {
            catalogue[product[0]] = {}
        }
        catalogue[product[0]][product] = price
    }
    for (const letter of Object.keys(catalogue).sort((a, b) => a.localeCompare(b))) {
        console.log(letter)
        for (const product of Object.keys(catalogue[letter]).sort((a, b) => a.localeCompare(b))) {
            console.log(`  ${product}: ${catalogue[letter][product]}`)
        }
    }
}

solve([
        'Appricot : 20.4',
        'Fridge : 1500',
        'TV : 1499',
        'Deodorant : 10',
        'Boiler : 300',
        'Apple : 1.25',
        'Anti-Bug Spray : 15',
        'T-Shirt : 10'
    ]
)