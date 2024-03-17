function solve(array) {
    const heroes = []
    for (const line of array) {
        const [Hero, level, items] = line.split(" / ")
        heroes.push(
            {
                Hero,
                level,
                items,
            }
        )
    }
    for (const hero of heroes.sort((a, b) => parseInt(a.level) - parseInt(b.level))) {
        console.log(`Hero: ${hero.Hero}\nlevel => ${hero.level}\nitems => ${hero.items}`)
    }
}

solve([
        'Batman / 2 / Banana, Gun',
        'Superman / 18 / Sword',
        'Poppy / 28 / Sentinel, Antara'
    ]

)