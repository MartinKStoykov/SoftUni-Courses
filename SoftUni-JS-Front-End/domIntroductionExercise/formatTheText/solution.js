function solve() {
    const text = document.getElementById("input").value.split(".").filter(a => /\S/.test(a))
    const output = document.getElementById("output")
    let paragraph = ""
    for (let i = 0; i < text.length; ++i) {
        if (text[i] !== "") {
            paragraph += text[i]
            if (((i+1) % 3 === 0)||(i+1 === text.length)) {
                output.innerHTML += (`<p>${paragraph}.</p>`);
                paragraph = ""
            }
        }
    }
}