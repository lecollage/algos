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

// function main() {
//     const [n, m] = readline().split(' ').map(Number)
//     const arr1 = readline().split(' ').map(Number)
//     const arr2 = readline().split(' ').map(Number)
//     const result = new Array(n + m)

//     // console.log(arr1, arr2)

//     let i = 0
//     let j = 0

//     while (i < n || j < m) {
//         if (j === m || (i < n && arr1[i] < arr2[j])) {
//             result[i + j] = arr1[i]
//             i++
//         } else {
//             result[i + j] = arr2[j]
//             j++
//         }
//     }

//     console.log(result.join(' '))
// }

function main() {
    const [n, m] = readline().split(' ').map(Number)
    const arr1 = readline().split(' ').map(Number)
    const arr2 = readline().split(' ').map(Number)
    const results = []
    // console.log(arr1, arr2)

    let i = 0
    let j = 0

    while (i < n || j < m) {
        if (j === m || (i < n && arr1[i] < arr2[j])) {
            i++
        } else {
            results.push(i)
            j++
        }
    }

    console.log(results.join(' '))
}
