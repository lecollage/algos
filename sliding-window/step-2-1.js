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
    const [n, s] = readline().split(' ').map(Number)
    const arr = readline().split(' ').map(Number)
    let sum = 0
    let L = 0
    let res = 0

    // console.log(n,s,arr)

    for(let R = 0; R < n; R++) {
        sum += arr[R]

        while (sum > s) {
            sum -= arr[L]
            L++
        }

        res = Math.max(res, R-L+1)
    }
    
    console.log(res)
}