function ticketSale(dayType, age) {
    let price = ""
    if ((age >= 0) && (age <= 18)) {
        if (dayType == "Weekday"){
            price = "12$"
        }else if  (dayType == "Weekend"){
            price = "15$"
        }else{
            price = "5$"
        }
    }else if((age > 18) && (age <= 64)) {
        if (dayType == "Weekday"){
            price = "18$"
        }else if  (dayType == "Weekend"){
            price = "20$"
        }else{
            price = "12$"
        }
    }else if((age > 64) && (age <= 122)) {
        if (dayType == "Weekday"){
            price = "12$"
        }else if  (dayType == "Weekend"){
            price = "15$"
        }else{
            price = "10$"
        }
    }else {
        price = "Error!"
    }
    console.log(price)
    }