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
//     const [n, s] = readline().split(' ').map(Number)
//     const arr = readline().split(' ').map(Number)

//     let count = 0
//     let left = 0
//     let current_sum = 0
//     let prefix_sum = [];

//     for(let i =0; i < n + 1; i++){
//         prefix_sum.push(0)
//     }

//     console.log(prefix_sum)

//     for (let i = 0; i < n; i++) {
//         prefix_sum[i + 1] = prefix_sum[i] + arr[i]
//     }

//     console.log(prefix_sum)

//     for (let right = 0; right < n + 1; right++) {
//         current_sum = prefix_sum[right] - prefix_sum[left]
//         while (current_sum >= s) {
//             count += n - right + 1
//             current_sum -= arr[left]
//             left += 1
//         }
//     }

//     console.log(count)
// }

function main() {
    const [n, s] = readline().split(' ').map(Number)
    const arr = readline().split(' ').map(Number)
    let L = 0
    let count = 0
 
    for(let R = 0; R < n; R++) {
        x += arr[R];
 
        while (x >= s) {
            x -= arr[L]
            L++
        }
 
        count += L
    }
    
    console.log(count)
}

/*
7 20
2 6 4 3 6 8 9
0 1 2 3 4 5 6

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