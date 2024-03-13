function solve(length) {
    let rows = 0
    let sequence = ["A", "T", "C", "G", "T", "T", "A", "G", "G", "G"]
    while(rows < length) {
        console.log(`**${sequence[0]}${sequence[1]}**`)
        rows += 1
        sequence.push(sequence.shift())
        sequence.push(sequence.shift())
        if (rows < length) {
            console.log(`*${sequence[0]}--${sequence[1]}*`)
            rows += 1
            sequence.push(sequence.shift())
            sequence.push(sequence.shift())
        }if (rows < length) {
            console.log(`${sequence[0]}----${sequence[1]}`)
            rows += 1
            sequence.push(sequence.shift())
            sequence.push(sequence.shift())
        }if (rows < length) {
            console.log(`*${sequence[0]}--${sequence[1]}*`)
            rows += 1
            sequence.push(sequence.shift())
            sequence.push(sequence.shift())
        }
    }
}

solve(10)