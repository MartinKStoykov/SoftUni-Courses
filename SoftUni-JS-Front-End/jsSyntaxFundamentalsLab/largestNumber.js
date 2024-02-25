function largestNumber(numX, numY, numZ) {
    let biggestNumber = -Infinity 

    if(numX > biggestNumber) {
        biggestNumber = numX;
    }
    if(numY > biggestNumber) {
        biggestNumber = numY;
    }
    if(numZ > biggestNumber) {
        biggestNumber = numZ;
    }
    console.log(`The largest number is ${biggestNumber}.`)
}


largestNumber(-5, -5, -20)