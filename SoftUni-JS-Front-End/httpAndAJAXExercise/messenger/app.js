function attachEvents() {
    const url = "http://localhost:3030/jsonstore/messenger"

    const sendButton = document.getElementById("submit")
    const refreshButton = document.getElementById("refresh")
    const nameInput = document.getElementsByName("author")[0]
    const messageInput = document.getElementsByName("content")[0]

    const textArea = document.querySelector("textarea")

    sendButton.addEventListener("click", async() => {
        const newMessage = {
            author: nameInput.value,
            content: messageInput.value,
        }

        await fetch(url, {
            method: "POST",
            body: JSON.stringify(newMessage),
        })

    })
    refreshButton.addEventListener("click", async () => {
        const allMessagesResponse = await fetch(url)
        const allMessages = await allMessagesResponse.json()
        const messageExport = []
        for (const message of Object.values(allMessages)) {
            messageExport.push(`${message.author}: ${message.content}`)
        }
        textArea.textContent = messageExport.join("\n")
    })
}

attachEvents();