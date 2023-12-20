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

const map = new Map()

let num = 0

const add = (x) => {
    if(map.has(x)) {
        map.set(x, map.get(x)+1)
    } else {
        map.set(x, 1)
    }

    if(map.get(x) === 1) {
        num++
    }
}

const remove = (x) => {
    if(map.has(x)) {
        map.set(x, map.get(x)-1)
    }

    if(map.get(x) === 0) {
        num--
    }
}

const good = (k) => {
    return num <= k
}

function main() {
    const [n, k] = readline().split(' ').map(Number)
    const arr = readline().split(' ').map(Number)
    let L = 0
    let count = 0
 
    for(let R = 0; R < n; R++) {
        add(arr[R])
        
        while (!good(k)) {
            remove(arr[L])
            L++
        }

        // console.log(L, R, count)
 
        count += R - L + 1
    }
    
    console.log(count)
}

/*

7 3
2 6 4 3 6 8 3

*/