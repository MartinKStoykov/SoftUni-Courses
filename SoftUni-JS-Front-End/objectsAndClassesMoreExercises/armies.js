function solve(array) {
    const armies = {}
    for (const line of array) {
        if (line.indexOf("arrives") !== -1) {
            const leader = line.split(" arrives")[0]
            armies[leader] = {}
        } else if (line.indexOf(": ") !== -1) {
            const [leader, army] = line.split(": ")
            if (armies[leader]) {
                const [armyName, armyCount] = army.split(", ")
                armies[leader][armyName] = parseInt(armyCount)
            }

        } else if (line.indexOf(" + ") !== -1) {
            const [armyName, armyCount] = line.split(" + ")
            Object.keys(armies).forEach(leader => {
                if (armies[leader][armyName]) {
                    armies[leader][armyName] += parseInt(armyCount)
                }
            })

        } else if (line.indexOf("defeated") !== -1) {
            const leader = line.split(" defeated")[0]
            if (armies[leader]) {
                Object.keys(armies).forEach(army => {
                    delete armies[leader][army]
                })
                delete armies[leader]
            }
        }
    }
    const sortedLeaders = Object.keys(armies).sort((a, b) => {
        const armyAPoints = Object.keys(armies[a]).length === 0 ? 0 :
            Object.values(armies[a]).reduce((sum, points) => sum + parseInt(points))
        const armyBPoints = Object.keys(armies[b]).length === 0 ? 0 :
            Object.values(armies[b]).reduce((sum, points) => sum + parseInt(points))
        return armyBPoints - armyAPoints
    })
    for (const leader of sortedLeaders) {
        let totalArmyCount = 0
        Object.values(armies[leader]).forEach(count => {
            totalArmyCount += parseInt(count)
        })
        console.log(`${leader}: ${totalArmyCount}`)
        Object.keys(armies[leader])
            .sort((a, b) => {
                const armyAPoints = parseInt(armies[leader][a])
                const armyBPoints = parseInt(armies[leader][b])
                return armyBPoints - armyAPoints
            })
            .forEach((army) => {
            console.log(`>>> ${army} - ${armies[leader][army]}`)
        })
    }
}

solve(['Rick Burr arrives', 'Findlay arrives', 'Rick Burr: Juard, 1500', 'Wexamp arrives', 'Findlay: Wexamp, 34540', 'Wexamp + 340', 'Wexamp: Britox, 1155', 'Wexamp: Juard, 43423', "brbr arrives"])
