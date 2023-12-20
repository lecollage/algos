process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputArray = [];
let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
    inputArray.push(inputStdin)
});

process.stdin.on("end", (_) => {
    inputString = inputArray.join('')
    inputString = inputString
        .trim()
        .split("\n")
        .map((string) => {
            return string.trim();
        });

    main();
});

function readline() {
    return inputString[currentLine++];
}

function main() {
    const [n, maxWeight] = readline().split(' ').map(Number)
    const weights = readline().split(' ').map(Number)
    const costs = readline().split(' ').map(Number)
    let L = 0
    let weight = 0
    let sum = 0
    let maxSum = -Infinity

    // console.log(distance,arr)

    for(let R = 0; R < n; R++) {
        weight += weights[R]
        sum += costs[R]

        while(weight > maxWeight) {
            weight -= weights[L]
            sum -= costs[L]
            L++
        }

        maxSum = Math.max(maxSum, sum)
    }

    console.log(maxSum)
}

/**
6 20
9 7 6 5 8 4
7 1 3 6 8 3
*/