function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      let restaurants = document.getElementsByTagName("textarea")[0].value
          .trim()
          .slice(1, -1)
          .trim()
          .slice(1, -1)
          .split('","')
      const restaurantSalaries = {}
      for (const r of restaurants) {
         const [name, workers] = r.split(" - ")
         if (!restaurantSalaries[name]) {
            restaurantSalaries[name] = []
         }
         const people = workers.split(", ")
         for (const p of people) {
            const [person, wage] = p.split(" ")
            restaurantSalaries[name].push({[person]: parseInt(wage)})
         }
      }
      const bestRestaurantOutput = document.getElementsByTagName("p")[0]
      const bestWorkersOutput = document.getElementsByTagName("p")[1]
      let bestRestaurant = ["None", 0, 0]
      let bestWorkers = {}
      for (const [restaurant, workers] of Object.entries(restaurantSalaries)) {
         const numbers = workers.map(num => parseInt(Object.values(num)));
         const currentSum = numbers.reduce((a, b) => a + b);
         const currentMax = numbers.reduce((max, num) => Math.max(max, num), 0)
         if (currentSum === bestRestaurant[1]) {
            continue
         } else if ((currentSum / workers.length) > bestRestaurant[1]) {
            bestRestaurant.unshift(restaurant, (currentSum / workers.length), currentMax)
            bestWorkers = workers
         }
      }
      bestRestaurantOutput.textContent = `Name: ${bestRestaurant[0]} Average Salary: ${bestRestaurant[1].toFixed(2)} Best Salary: ${bestRestaurant[2].toFixed(2)}`
      for (const line of bestWorkers.sort((a, b) => Object.values(b) - Object.values(a))) {
         for (const [key, value] of Object.entries(line)) {
            bestWorkersOutput.textContent += `Name: ${key} With Salary: ${value} `
         }
      }

   }
}