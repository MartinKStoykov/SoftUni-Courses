function solve(array) {
    const schoolRegister = {}
    for (const line of array) {
        const [name, grade, avgScore] = line.split(", ")
        const studentName = name.split(": ")[1]
        const studentGrade = grade.split(": ")[1]
        const studentScore = avgScore.split(": ")[1]
        if (studentScore >= 3) {
            if (!schoolRegister[parseInt(studentGrade) + 1]) {
                schoolRegister[parseInt(studentGrade) + 1] = {students: [], score: []}
            }
            schoolRegister[parseInt(studentGrade) + 1].students.push(studentName)
            schoolRegister[parseInt(studentGrade) + 1].score.push(parseFloat(studentScore))
        }
    }
    for (const [key, value] of Object.entries(schoolRegister)) {
        console.log(`${key} Grade`)
        console.log(`List of students: ${value.students.join(", ")}`)
        console.log(`Average annual score from last year: ${((value.score.reduce((n1, n2) => n1+ n2)) / value.students.length).toFixed(2)}`)
        console.log()
    }
}
