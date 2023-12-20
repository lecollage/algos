/*
** <problem_number> - <problem_title>
*/

// Common Template Starts //
//*
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
// Common Template Ends //

// function getMax(k, groups) {
//     // return groups.reduce((acc, value) => acc * value)/k
//     // return Number.MAX_VALUE
// }

function getNumberOfStudents(groups) {
    return groups.reduce((acc, value) => acc + value)
}

function getMax(k, groups) {
    // return getNumberOfStudents(groups) / k
    return 25*1000000000 + 1
}

function canCreateGroups(t, k, groups) {
    let target = t * k

    for (let i = 0; i < groups.length; i++) {
        const group = groups[i]

        target -= Math.min(group, t)

        if (target <= 0) {
            return true
        }
    }

    return false
}

function binarySearch(k, groups) {
    let left = 0
    let right = getMax(k, groups)

    while(left + 1 < right) {
        const middle = Math.floor((left + right)/2)

        if (canCreateGroups(middle, k, groups)) {
            left = middle
        } else {
            right = middle
        }
    }

    return left
}


function main() {
    const k = Number(readline())
    const n = Number(readline())
    const groups = []

    for (let i = 0; i < n; i++) {
        groups.push(Number(readline()))
    }

    // console.log(groups, k, n)

    const result = binarySearch(k, groups)
    console.log( result  )
}
//*/