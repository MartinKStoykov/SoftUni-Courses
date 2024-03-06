function listOfNames(arr) {
    arr.sort((a,b) => a.localeCompare(b))
    for (let i = 0; i < arr.length; ++i) {
        console.log(`${i+1}.${arr[i]}`)
    }
}

listOfNames(["1", "2john", "10john", "John", "john", "john", "john", "john", "john", "john", "john", ])