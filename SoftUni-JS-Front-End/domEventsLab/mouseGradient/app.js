function attachGradientEvents() {
    const gradientBox = document.getElementById("gradient")
    const result = document.getElementById("result")
    gradientBox.addEventListener("mousemove", function(event){
        let mouseX = event.offsetX
        const targetWidth = gradientBox.clientWidth
        result.textContent = `${Math.floor((mouseX / targetWidth) * 100)}%`
    })
}