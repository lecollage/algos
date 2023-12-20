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
/*


*/

const calcMaxCost = (arrA, arrB, maxWeight, w1, w2) => {
    let i = 0, j = 0, restWeight = maxWeight, cost = 0

    while((restWeight >= w1 || restWeight >= w2) && (i < arrA.length || j < arrB.length)) {
        if((i < arrA.length && restWeight >= w1 && arrA[i]*w2 >= arrB[j]*w1) || j === arrB.length || w2 > restWeight) {
            cost += arrA[i]
            restWeight -= w1
            i++
        } else {
            cost += arrB[j]
            restWeight -= w2
            j++
        }
    }

    console.log(i, j, arrA[i], arrB[j])

    // if (arrA[i] * w2 < arrB[j] * w1) {
    //     restWeight += w1
    //     cost -= arrA[i]

    //     restWeight -= w2
    //     cost += arrB[j]
    // } else {
    //     restWeight += w2
    //     cost -= arrB[j]

    //     restWeight -= w1
    //     cost += arrA[i]
    // }


    return cost
}
/**
23 - 5 = 18; 12
18 - 5 = 13; 22
13 - 5 = 7;  31
7  - 3 = 4;  39
4  - 3 = 1;  46

23 - 3 - 5 - 3 - 5 - 5 = 2
8 + 12 + 7 + 10 + 9 = 46
 */


function main() {
    const [, , s, A, B] = readline().split(' ').map(Number)
    const arrA = readline().split(' ').map(Number).sort((a, b) => b - a)
    const arrB = readline().split(' ').map(Number).sort((a, b) => b - a)

    console.log(s, A, B, arrA, arrB)
    
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
*/