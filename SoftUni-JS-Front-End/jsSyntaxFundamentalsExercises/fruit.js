function fruitPrice(fruitType, grams, pricePerKilo) {
    console.log(`I need $${(pricePerKilo * (grams /1000)).toFixed(2)} to buy ${(grams/1000).toFixed(2)} kilograms ${fruitType}.`)
}