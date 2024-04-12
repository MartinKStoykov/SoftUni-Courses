function attachEvents() {
    const baseURL = "http://localhost:3030/jsonstore/phonebook"

    const loadButton = document.getElementById("btnLoad")
    const createButton = document.getElementById("btnCreate")

    const phonebookList = document.getElementById("phonebook")

    const personInput = document.getElementById("person")
    const phoneInput = document.getElementById("phone")

    loadButton.addEventListener("click", async() => {
        phonebookList.innerHTML = ""
        const phonesResponse = await fetch(baseURL)
        const phones = await phonesResponse.json()

        for (const phone of Object.values(phones)) {
            const newLiElement = document.createElement("li")
            newLiElement.textContent = `${phone.person}: ${phone.phone}`

            const newButton = document.createElement("button")
            newButton.textContent = "Delete"

            newLiElement.appendChild(newButton)
            phonebookList.appendChild(newLiElement)

            newButton.addEventListener("click", async() => {
                const phoneId = phone._id
                await fetch((baseURL + `/${phoneId}`), {
                    method: "DELETE"
                })

                newLiElement.remove()
            })
        }
    })

    createButton.addEventListener("click", async() => {
        const newPhone = {
            person: personInput.value,
            phone: phoneInput.value,
        }

        await fetch(baseURL, {
            method: "POST",
            body: JSON.stringify(newPhone),
        })

        personInput.value = ""
        phoneInput.value = ""
    })


}

attachEvents();