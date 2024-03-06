function pyramid(base, increment) {
    let currentStone = 0
    let currentMarble = 0
    let currentLapis = 0
    let currentGold = 0
    let currentBase = base
    for (let step = 1; currentGold === 0; ++step) {
        if (currentBase <= 2) {
            currentGold += currentBase * currentBase
            console.log(`Stone required: ${Math.ceil(currentStone * increment)}`)
            console.log(`Marble required: ${Math.ceil(currentMarble * increment)}`)
            console.log(`Lapis Lazuli required: ${Math.ceil(currentLapis * increment)}`)
            console.log(`Gold required: ${Math.ceil(currentGold * increment)}`)
            console.log(`Final pyramid height: ${Math.floor(step * increment)}`)
            break
        }else if (step % 5 === 0) {
            currentLapis += ((currentBase -2) * 4) + 4
        }else {
            currentMarble += ((currentBase -2) * 4) + 4
        }
        currentStone += ((currentBase - 2) * (currentBase - 2))

        currentBase -= 2

    }
}
pyramid(12, 1)