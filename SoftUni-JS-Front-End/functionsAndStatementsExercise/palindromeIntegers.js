function solve(array) {
    for (let i of array) {
        let isPalindrome = true
        let string = i.toString()
        for (let j = 0; j <= Math.ceil(string.length/2); ++j) {
            if (string.charAt(j) !== string.charAt(string.length-1 - j)) {
                isPalindrome = false
                break;
            }
        }
        console.log(isPalindrome)
    }
}
solve([32,2,232,1010])