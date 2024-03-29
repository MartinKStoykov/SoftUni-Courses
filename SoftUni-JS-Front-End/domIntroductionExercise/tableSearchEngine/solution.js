function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

    function onClick() {
       const searchedWord = document.getElementById("searchField").value
       const table = document.getElementsByTagName("table")[0]
       const rows = table.rows
       for (let i = 1; i < rows.length; ++i) {
            rows[i].classList.remove("select")
            if (rows[i].textContent.includes(searchedWord)) {
               rows[i].classList.add("select")
            }
       }
    }
}