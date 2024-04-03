function create(words) {
   const outputSection = document.getElementById("content")
   for (const string of words) {
      let newDivElement = document.createElement("div")
      let newParagraphElement = document.createElement("p")
      newParagraphElement.textContent = string
      newParagraphElement.style.display = "none"
      newDivElement.appendChild(newParagraphElement)
      newDivElement.addEventListener("click", () => {
         newParagraphElement.style.display = "inline"
      })
      outputSection.appendChild(newDivElement)
   }
}