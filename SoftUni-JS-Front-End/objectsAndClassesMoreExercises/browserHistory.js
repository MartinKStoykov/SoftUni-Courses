function solve(object, array) {
    for (const command of array) {
        const [action, site] = command.split(" ")
        if (action === "Open") {
            object["Open Tabs"].push(site)
            object["Browser Logs"].push(`${action} ${site}`)
        }else if (action === "Close") {
            if (object["Open Tabs"].includes(site)) {
                const siteIndex = object["Open Tabs"].indexOf(site)
                object["Open Tabs"].splice(siteIndex, 1)
                object["Recently Closed"].push(site)
                object["Browser Logs"].push(`${action} ${site}`)
            }
        }else if (action === "Clear") {
            object = {"Browser Name": object["Browser Name"],"Open Tabs":[],
                "Recently Closed":[],
                "Browser Logs":[]}

        }

    }
    console.log(object["Browser Name"])
    console.log(`Open Tabs: ${object["Open Tabs"].join(", ")}`)
    console.log(`Recently Closed: ${object["Recently Closed"].join(", ")}`)
    console.log(`Browser Logs: ${object["Browser Logs"].join(", ")}`)
}