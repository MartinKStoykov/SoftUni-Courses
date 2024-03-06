function bitcoinMiner(numbers) {
    const goldPrice = 67.51
    const bitcoinPrice = 11949.16
    let ownedMoney = 0
    let ownedBitcoins = 0
    let firstDayBought = 0
    for (let day = 1; day <= numbers.length; ++day) {
        if (day % 3 === 0) {
            ownedMoney += ((goldPrice * numbers[day-1]) * 0.70)
        }else{
            ownedMoney += (goldPrice * numbers[day-1])
        }
        if (ownedMoney >= bitcoinPrice) {
            if (!firstDayBought) {
                firstDayBought = day
            }
            ownedBitcoins += Math.floor(ownedMoney / bitcoinPrice)
            ownedMoney -= (Math.floor(ownedMoney / bitcoinPrice) * bitcoinPrice)
        }
    }
    console.log(`Bought bitcoins: ${ownedBitcoins}`)
    if (firstDayBought) {
        console.log(`Day of the first purchased bitcoin: ${firstDayBought}`)
    }
    console.log(`Left money: ${ownedMoney.toFixed(2)} lv.`)

}

