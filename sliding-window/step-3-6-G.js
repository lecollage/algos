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

/*

{
    a: [0,1]
    b: [2,4,5]
    c: [3]
}


aabcbb

sum: 1+2
a:2
ababcbb


*/

const calcRudeness = (str, c) => {
    let countA = 0,
        countB = 0,
        rudeness = 0,
        L = 0,
        strMaxLen = -Infinity

    for (let R = 0; R < str.length; R++) {      
        if (str[R] === 'a') {
            countA++
        } else if(str[R] === 'b') {
            rudeness += countA
            countB++
        }

        while(rudeness > c) {
            if (str[L] === 'a') {
                rudeness -= countB
                countA--
            } else if(str[L] === 'b') {
                countB--
            }
            
            L++
        }

        strMaxLen = Math.max(strMaxLen, R - L + 1)
    }

    return strMaxLen
}


function main() {
    const [n, c] = readline().split(' ').map(Number)
    const str = readline()
    
    console.log(calcRudeness(str, c))
}


/**
входные данные
6 2
aabcbb

6 2
ababcbb
*/