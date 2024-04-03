function attachEventsListeners() {
    const buttons = document.querySelectorAll("[value = 'Convert']")
    const inputDays = document.querySelector("#days")
    const inputHours = document.querySelector("#hours")
    const inputMinutes = document.querySelector("#minutes")
    const inputSeconds = document.querySelector("#seconds")

    Array.from(buttons).forEach(button => {
        button.addEventListener("click", (event) => {
            let time = ""
            for (const button of buttons) {
                const inputElement = button.parentNode.querySelector("input")
                if (inputElement.value) {
                    time = inputElement
                    break
                }
            }
            if (time.getAttribute("id") === "days") {
                inputHours.value = time.value * 24
                inputMinutes.value = inputHours.value * 60
                inputSeconds.value = inputMinutes.value * 60
            } else if (time.getAttribute("id") === "hours") {

                inputDays.value = time.value / 24
                inputMinutes.value = time.value * 60
                inputSeconds.value = inputMinutes.value * 60
            } else if (time.getAttribute("id") === "minutes") {
                inputSeconds.value = time.value * 60
                inputHours.value = time.value / 60
                inputDays.value = inputHours.value / 24

            } else if (time.getAttribute("id") === "seconds") {
                inputMinutes.value = time.value / 60
                inputHours.value = inputMinutes.value / 60
                inputDays.value = inputHours.value / 24
            }
        })
    })
}