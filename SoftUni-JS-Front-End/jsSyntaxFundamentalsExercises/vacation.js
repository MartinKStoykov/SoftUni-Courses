function vacationPrice(groupSize, groupType, day) {
    price = 0
    if((groupType == "Business") && (groupSize >= 100)) {
        groupSize -= 10 
    }
    switch(day) {
        case "Friday":
            switch(groupType) {
                case "Students":
                    price = 8.45 * groupSize; break;
                case "Business":
                    price = 10.90 * groupSize; break;
                case "Regular":
                    price = 15 * groupSize; break;
            }break;
        case "Saturday":
            switch(groupType) {
                case "Students":
                    price = 9.80 * groupSize; break;
                case "Business":
                    price = 15.60 * groupSize; break;
                case "Regular":
                    price = 20 * groupSize; break;
            }break;
        case "Sunday":
            switch(groupType) {
                case "Students":
                    price = 10.46 * groupSize; break;
                case "Business":
                    price = 16 * groupSize; break;
                case "Regular":
                    price = 22.50 * groupSize; break;
            }break;
    }
     if ((groupType == "Students") && (groupSize >= 30)) {
        price *= 0.85
     }else if((groupType == "Regular") && ((groupSize >= 10)&&(groupSize<=20))) {
        price *= 0.95
     }


    console.log(`Total price: ${price.toFixed(2)}`)
}

vacationPrice(40, "Regular", "Saturday")