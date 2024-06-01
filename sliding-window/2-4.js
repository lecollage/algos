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
    let x = 0
    let L = 0
    let count = 0

    for(let R = 0; R < n; R++) {
        x += arr[R];

        while (x >= s) {
            x -= arr[L]
            L++
        }


        console.log(L, R, x)

        count += L
    }
    
    console.log(count)
}
/*
7 20
2 6 4 3 6 8 9

26436
264368
2643689

64368
643689

4368
43689
3689
689
*/
