function revealWords(string, censoredString) {
    let arrString = string.split(", ")
    let arrCensored = censoredString.split(" ")
    for(let w of arrCensored) {
        if (w.includes("*")) {
            let count = w.length
            for(let c of arrString) {
                if (count === c.length){
                    arrCensored[arrCensored.indexOf(w)] = c
                }
            }

        }
    }
    console.log(arrCensored.join(" "))
}

revealWords('great','softuni is ***** place for learning new programming languages'
)