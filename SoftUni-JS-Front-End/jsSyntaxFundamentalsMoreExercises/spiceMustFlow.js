function spiceExtraction(startingYield) {
    let totalSpice = 0
    let days = 0
    while (startingYield >= 100) {
        totalSpice += startingYield
        days += 1
        startingYield -= 10
        if (totalSpice >= 26) {
            totalSpice -= 26
        }
    }
    if (totalSpice >= 26) {
        totalSpice -= 26
    }
    console.log(days)
    console.log(totalSpice)

}

spiceExtraction(450)