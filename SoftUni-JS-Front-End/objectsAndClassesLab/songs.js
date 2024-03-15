function solve(input) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList
            this.name = name
            this.time = time
        }
    }
    const songs = {}
    const songCount = input.shift()
    const requestedType = input.pop()
    for (const song of input) {
        const [type, name, length] = song.split("_")
        const s = new Song(type, name, length)
        if ((s.typeList === requestedType)||(requestedType === "all")) {
            console.log(s.name)
        }
    }
}