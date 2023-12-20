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
    const [_, distance] = readline().split(' ').map(Number)
    const arr = readline().split(' ').map(Number)
    let L = 0
    let sum = 0

    // console.log(distance,arr)

    for(let R = 0; R < arr.length; R++) {
        let diff = arr[R] - arr[L]
 
        while (diff > distance) {
            L++
            diff = arr[R] - arr[L]
        }

        sum += L
    }

    console.log(sum)
}

/**
4 4
1 3 5 8


 */