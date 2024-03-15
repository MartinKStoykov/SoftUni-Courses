function addressBook(array) {
    const addresses = {};
    for (const line of array) {
        const [name, address] = line.split(":");
        addresses[name] = address;
    }

    const sortedKeys = Object.keys(addresses).sort((a, b) => a.localeCompare(b));
    for (const name of sortedKeys) {
        const address = addresses[name];
        console.log(`${name} -> ${address}`);
    }
}
