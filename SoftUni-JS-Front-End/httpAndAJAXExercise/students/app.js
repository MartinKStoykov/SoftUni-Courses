function attachEvents() {
    const baseURL = "http://localhost:3030/jsonstore/collections/students"

    const inputFirstName = document.getElementsByName("firstName")[0]
    const inputLastName = document.getElementsByName("lastName")[0]
    const inputFacultyNumber = document.getElementsByName("facultyNumber")[0]
    const inputGrade = document.getElementsByName("grade")[0]

    const table = document.querySelector("tbody")

    const submitButton = document.getElementById("submit")

    async function addExistingStudents() {
        await fetch(baseURL)
            .then(response => response.json())
            .then(data => Object.values(data)
                .forEach(student => addStudent(student)))
    }
    addExistingStudents()
    submitButton.addEventListener("click", async() => {
        const student = await fetch(baseURL, {
            method: "POST",
            body: JSON.stringify({
                firstName: inputFirstName.value,
                lastName: inputLastName.value,
                facultyNumber: inputFacultyNumber.value,
                grade: inputGrade.value,
            })
        })
        await addStudent(student.json())


        inputFirstName.value = ""
        inputLastName.value = ""
        inputFacultyNumber.value = ""
        inputGrade.value = ""

    })
    async function addStudent(student) {
        const newTr = document.createElement("tr")

        const firstNameCell = document.createElement("td")
        firstNameCell.textContent = student.firstName
        newTr.appendChild(firstNameCell)

        const lastNameCell = document.createElement("td")
        lastNameCell.textContent = student.lastName
        newTr.appendChild(lastNameCell)

        const facultyNumberCell = document.createElement("td")
        facultyNumberCell.textContent = student.facultyNumber
        newTr.appendChild(facultyNumberCell)

        const gradeCell = document.createElement("td")
        gradeCell.textContent = student.grade
        newTr.appendChild(gradeCell)

        table.appendChild(newTr)
    }
}

attachEvents();