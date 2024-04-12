function solution() {
    const baseURL = "http://localhost:3030/jsonstore/advanced/articles/list"
    const additionalInfoURL = "http://localhost:3030/jsonstore/advanced/articles/details/"

    const mainSection = document.getElementById("main")


    async function startingLayout() {
        const topicsResponse = await fetch(baseURL)
        const topics = await topicsResponse.json()

        for (const topic of topics) {
            const accordion = `
                <div class="head">
                    <span>${topic.title}</span>
                    <button class="button" id="${topic._id}">More</button>
                </div>
                <div class="extra">
                    <p></p>
                </div>`
            const newDiv = document.createElement("div")
            newDiv.className = "accordion"
            newDiv.innerHTML = accordion
            mainSection.appendChild(newDiv)

            const button = document.getElementById(`${topic._id}`)

            let isExpanded = false

            button.addEventListener("click", async () => {
                const infoResponse = await fetch(additionalInfoURL + topic._id)
                const info = await infoResponse.json()
                const additionalInfoDiv = newDiv.querySelector(".extra")

                additionalInfoDiv.querySelector("p").textContent = info.content
                if (!isExpanded) {
                    additionalInfoDiv.style.display = "block"
                    button.textContent = "LESS"
                    isExpanded = true
                } else {
                    additionalInfoDiv.style.display = "none"
                    button.textContent = "MORE"
                    isExpanded = false
                }
            })
        }
    }

    startingLayout()
}
solution()