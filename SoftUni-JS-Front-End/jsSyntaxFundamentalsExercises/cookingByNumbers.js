function cooking(num, op1, op2, op3, op4, op5) {
    let operations = [op1, op2, op3, op4, op5]
    let number = parseInt(num)
    for (let i = 0; i < 5; ++i) {
        switch (operations[i]) {
            case "chop": number /= 2; break;
            case "dice": number = Math.sqrt(number); break;
            case "spice": number += 1; break;
            case "bake": number *= 3; break;
            case "fillet": number *= 0.80; break;
        }
        console.log(number)
    }
}
