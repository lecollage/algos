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
    const [n, p] = readline().split(' ').map(Number)
    const arr = readline().split(' ').map(Number)
    let x = arr[0]
    let c = 1
    let R = 1
    let res_L
    let res = +Infinity

    // console.log(n,p,arr)

    const sumCommon = arr.reduce((acc, el) => acc + el)

    // console.log(sumCommon)

    const countRounds = (Math.floor(p / sumCommon) - 1)

    if (countRounds > 0) {
        x += (countRounds * sumCommon)
        c += countRounds * n
    }
    
    for(let L = 0; L < n; L++) {
        while(x < p) {
            x += arr[R]
            c++
            R = (R + 1) % n
        }

        if(res > c) {
            res = c
            res_L = L
        }
        
        x -= arr[L]
        c--
    }

    console.log(res_L + 1, res)
}