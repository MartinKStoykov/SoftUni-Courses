function solve(array) {
    const movies = {}
    for (const line of array) {
        if (line.includes("addMovie")) {
            const movie = line.split("addMovie ").join("")
            if (!movies[movie])
                movies[movie] = {name: ""}
            movies[movie].name = movie
        } else if (line.includes("directedBy")) {
            const [movie, person] = line.split(" directedBy ")
            if (movies[movie]){
                movies[movie].director = person
            }
        } else if (line.includes("onDate")) {
            const [movie, day] = line.split(" onDate ")
            if (movies[movie]){
                movies[movie].date = day
            }
        }
    }
    for (const movie in movies) {
        {
            if ((movies[movie].director) && (movies[movie].date))
                console.log(JSON.stringify(movies[movie]))
        }
    }
}

solve([
        'addMovie Fast and Furious',
        'addMovie Godfather',
        'Inception directedBy Christopher Nolan',
        'Godfather directedBy Francis Ford Coppola',
        'Godfather onDate 29.07.2018',
        'Fast and Furious onDate 30.07.2018',
        'Batman onDate 01.08.2018',
        'Fast and Furious directedBy Rob Cohen'
    ]
)