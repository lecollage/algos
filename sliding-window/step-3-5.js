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
3
1 2 3

2
1 3

2
3 4

2
2 3
*/

let n1, arr1, n2, arr2, n3, arr3, n4, arr4

const pointers = [0, 0, 0, 0]
let arrs

const getMinMaxIndexes = () => {
    let minIndex = 0
    let maxIndex = 0

    pointers.forEach((p, index) => {
        const currArr = arrs[index]
        const minArr = arrs[minIndex]
        const maxArr = arrs[maxIndex]
        
        if(currArr[p] < minArr[pointers[minIndex]]) {
            minIndex = index
        }

        if(currArr[p] > maxArr[pointers[maxIndex]]) {
            maxIndex = index
        }
    })

    // console.log(`getMinMax 2 >> `, minIndex, maxIndex)

    return [minIndex, maxIndex]
}

const isNextMinIndexOk = (minIndex) => pointers[minIndex] + 1 !== arrs[minIndex].length

function main() {
    n1 = readline().split(' ').map(Number)[0]
    arr1 = readline().split(' ').map(Number)
    arr1.sort((a, b) => a - b)
    
    n2 = readline().split(' ').map(Number)[0]
    arr2 = readline().split(' ').map(Number)
    arr2.sort((a, b) => a - b)

    n3 = readline().split(' ').map(Number)[0]
    arr3 = readline().split(' ').map(Number)
    arr3.sort((a, b) => a - b)

    n4 = readline().split(' ').map(Number)[0]
    arr4 = readline().split(' ').map(Number)
    arr4.sort((a, b) => a - b)

    // console.log(n1, arr1)
    // console.log(n2, arr2)
    // console.log(n3, arr3)
    // console.log(n4, arr4)

    arrs = [arr1, arr2, arr3, arr4]

    let minIndex = 0, maxIndex = 0, diff = +Infinity

    let results = []

    while(pointers[minIndex] !== arrs[minIndex].length) {
        [minIndex, maxIndex] = getMinMaxIndexes()

        const nextDiff = arrs[maxIndex][pointers[maxIndex]] - arrs[minIndex][pointers[minIndex]]

        if(nextDiff < diff) {
            diff = nextDiff
            results = [...pointers]
        }

        // console.log(`pointers >> `, pointers, minIndex, maxIndex)

        pointers[minIndex]++
    }


    // result
    // console.log(`final pointers >> `, pointers, minIndex)
    console.log(results.map((p, index) => arrs[index][p]).join(' '))
}

/** 
3
1 2 3
2
1 3
2
3 4
2
2 3

1
5
4
3 6 7 101
6 3
1
3
1
4
1
3

4
18 3 9 11
1
20


1
3
1
3
1
4
1
3

1
6 3
1
3
1
4
1
3


1
6 3
1
8 10
1
4 100
1
3 2

3 8 4 3



1 3 2
1 3
3 4
2 3

5
3 6 7 10
3 9 11 18
20
*/