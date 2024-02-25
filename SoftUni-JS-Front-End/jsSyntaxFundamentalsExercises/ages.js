function ageGuesser(age){
    let result;
    switch(true) {
        case age < 0: result = "out of bounds"; break;
        case age <= 2:result = "baby"; break;
        case age <= 13:result = "child"; break;
        case age <= 19:result = "teenager"; break;
        case age <= 65:result = "adult"; break;
        case age >= 66:result = "elder"; break;
    }
    console.log(result)
}

ageGuesser(-5)