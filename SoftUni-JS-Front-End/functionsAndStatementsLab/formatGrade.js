function formatGrade(grade) {
    let writtenGrade = ""
    switch (true) {
        case (grade < 3): writtenGrade = "Fail";break;
        case (grade < 3.5): writtenGrade = "Poor";break;
        case (grade < 4.50): writtenGrade = "Good";break;
        case (grade < 5.5): writtenGrade = "Very good";break;
        case (grade >= 5.5): writtenGrade = "Excellent";break;
    }
    if (grade < 3) {
        console.log(`${writtenGrade} (${parseInt(grade)})`)
    }else{
        console.log(`${writtenGrade} (${grade.toFixed(2)})`)
    }

}

formatGrade(2.99)