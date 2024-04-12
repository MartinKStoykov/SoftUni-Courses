function lockedProfile() {
    const baseURL = "http://localhost:3030/jsonstore/advanced/profiles"
    let counter = 1
    async function createProfile() {
        const profilesResponse = await fetch(baseURL)
        const profiles = await profilesResponse.json()
        const mainBody = document.getElementById("main")

        for (const profile of Object.values(profiles)) {
            const profileHTML = `
                <img src="./iconProfile2.png" class="userIcon" />
                <label>Lock</label>
                <input type="radio" name="user${counter}Locked" value="lock" checked>
                <label>Unlock</label>
                <input type="radio" name="user${counter}Locked" value="unlock"><br>
                <hr>
                <label>Username</label>
                <input type="text" name="user${counter}Username" value="${profile.username}" disabled readonly />
                <div class="user${counter}Username">
                    <hr>
                    <label>Email:</label>
                    <input type="email" name="user${counter}Email" value="${profile.email}" disabled readonly />
                    <label>Age:</label>
                    <input type="email" name="use${counter}Age" value="${profile.age}" disabled readonly />
                </div>
                <button>Show more</button>`
            const profileDiv = document.createElement("div")

            profileDiv.innerHTML = profileHTML
            profileDiv.className = "profile"
            const additionalInfo = profileDiv.querySelector(`.user${counter}Username`)
            mainBody.appendChild(profileDiv)
            const button = profileDiv.querySelector("button")
            additionalInfo.style.display = "none"
            button.addEventListener("click", () => {
                if (profileDiv.querySelector('input[value="unlock"]').checked) {
                    if (button.textContent === "Show more") {
                        additionalInfo.style.display = "block"
                        button.textContent = "Hide it"
                    } else {
                        additionalInfo.style.display = "none"
                        button.textContent = "Show more"
                    }
                }
            })
            counter += 1
        }
        const redundantProfile = document.getElementsByClassName("profile")[0]
        redundantProfile.remove()
    }
    createProfile()


}