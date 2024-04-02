function validate() {
    const inputSection = document.getElementById("email")
    inputSection.addEventListener("change", (event) => {
        const regex = /[a-z]+@[a-z]+\.[a-z]+$/
        if (regex.test(event.target.value)) {
            event.target.className = ""

        } else {
            event.target.className = "error"
        }
        }
    )
}