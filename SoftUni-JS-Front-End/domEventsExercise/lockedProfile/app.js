function lockedProfile() {
    const profiles = document.querySelectorAll(".profile")
    Array.from(profiles).forEach(profile => {
        const button = profile.querySelector("button")
        button.addEventListener("click", () => {
            if (!profile.querySelector("input").checked) {
                if (button.textContent === "Show more") {
                    profile.querySelector("div").style.display = "inline"
                    button.textContent = "Hide it"
                } else {
                    profile.querySelector("div").style.display = "none"
                    button.textContent = "Show more"
                }
            }
        })
    })
}