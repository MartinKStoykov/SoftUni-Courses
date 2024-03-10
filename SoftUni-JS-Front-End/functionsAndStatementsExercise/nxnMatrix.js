function solve(size) {
    let row = [(size.toString()+ " ").repeat(size)]
    for (let i = 0; i < size; ++i) {
        console.log(row.join(" "))
    }
}

solve(10)