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
    const [n, m] = readline().split(' ').map(Number)
    const arr1 = readline().split(' ').map(Number)
    const arr2 = readline().split(' ').map(Number)
    
    const map1 = new Map()
    const map2 = new Map()

    arr1.forEach(el => {
        if (map1.has(el)) {
            map1.set(el, map1.get(el) + 1)
        } else {
            map1.set(el, 1)
        }
    })

    arr2.forEach(el => {
        if (map2.has(el)) {
            map2.set(el, map2.get(el) + 1)
        } else {
            map2.set(el, 1)
        }
    })

    let pairs = 0    

    map2.forEach((v2,k2) => {
        if (map1.has(k2)) {
            pairs += v2 * map1.get(k2)
        }
    })
    
    console.log(pairs)
}