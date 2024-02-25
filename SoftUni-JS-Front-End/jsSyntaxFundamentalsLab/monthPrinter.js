

function solve(number) {
    let months = [
    "January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"
    ];
    if ((0 < number) && (number < 13)){
        console.log(months[number-1]);
    }else{
        console.log("Error!");
    }
}

solve(16)