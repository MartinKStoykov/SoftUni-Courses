function solve(array) {
    let sequences = [];
    for (const line of array) {
        const sublists = JSON.parse(`[${line}]`);
        for (const subline of sublists) {
            let duplicate = false
            const list = subline.sort((a, b) => b - a)

            for (const lst of sequences) {
                if (lst.every(element => list.includes(element))){
                    duplicate = true
                }
            }
            if (!duplicate) {
                sequences.push(list)
            }

        }
    }

    sequences.sort((a, b) => a.length - b.length)
    for (const list of sequences) {
        console.log("["+list.join(", ")+"]");
    }
}


solve(["[7.14, 7.180, 7.339, 80.099]",
    "[7.339, 80.0990, 7.140000, 7.18]",
    "[7.339, 7.180, 7.14, 80.099]"]



)