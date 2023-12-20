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

const calcMaxCost = (arrA, arrB, maxWeight, weightA, weightB) => {
    if(maxWeight < weightA && maxWeight < weightB) {
        return 0
    }

    // берём только из первого
    const maxA = Math.min(Math.trunc(maxWeight / weightA), arrA.length)
    const prefixSumsA = new Array(maxA)
    let costA = 0

    for(let i = 0; i < maxA; i++) {
        costA += arrA[i]
        prefixSumsA[i] = costA
    }

    // берём только из второго
    const maxB = Math.min(Math.trunc(maxWeight / weightB), arrB.length)
    const prefixSumsB = new Array(maxB)
    let costB = 0

    for(let i = 0; i < maxB; i++) {
        costB += arrB[i]
        prefixSumsB[i] = costB
    }

    // инит суммы
    let maxCost = Math.max(costA, costB)

    // берём из первого и из второго
    for(let i = 0; i < arrA.length; i++) {
        let currentCost = 0, restWeight = maxWeight;

        restWeight -= (i+1) * weightA

        if(restWeight < 0) {
            return maxCost
        }

        currentCost += prefixSumsA[i]

        const j = Math.min(Math.trunc(restWeight / weightB), arrB.length)

        restWeight -= j * weightB

        if(j > 0) {
            currentCost += prefixSumsB[j-1]
        }

        maxCost = Math.max(maxCost, currentCost)
    }


    return Math.max(maxCost, costA, costB)
}

function main() {
    const [, , s, A, B] = readline().split(' ').map(Number)
    const arrA = readline().split(' ').map(Number).sort((a, b) => b - a)
    const arrB = readline().split(' ').map(Number).sort((a, b) => b - a)

    // console.log(s, A, B, arrA, arrB)
    
    console.log(calcMaxCost(arrA, arrB, s, A, B))
}

/**
n, m, s, A, B

входные данные
6 7 23 3 5
7 4 3 1 5 8
10 12 7 3 8 9 7

выходные данные
47



входные данные
6 7 16 3 5
7 4 3 1 5 8
10 12 7 3 8 9 7

выходные данные
37



входные данные
6 7 5 3 5
7 4 3 1 5 8
10 12 7 3 8 9 7

выходные данные
12



входные данные
6 7 4 3 5
7 4 3 1 5 8
10 12 7 3 8 9 7

выходные данные
8




входные данные
6 7 2 3 5
7 4 3 1 5 8
10 12 7 3 8 9 7

выходные данные
0




входные данные
6 7 19 3 5
7 4 3
10 12

выходные данные
36
*/