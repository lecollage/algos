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
//     let sum = 0
//     let L = 0
//     let count = 0

//     // console.log(n,s,arr)

//     for(let R = 0; R < n; R++) {
//         sum += arr[R];

//         while (sum > s) {
//             sum -= arr[L]
//             L++
//         }

//         if (sum < s) {
//             const length = L + R - 1

//             count += ((1 + length) * length ) / 2
//         }
//     }
    
//     console.log(count)
// }

function main() {
    const [n, s] = readline().split(' ').map(Number)
    const arr = readline().split(' ').map(Number)
    let sum = 0
    let L = 0
    let count = 0

    // console.log(n,s,arr)

    for(let R = 0; R < n; R++) {
        sum += arr[R];

        while (sum > s) {
            sum -= arr[L]
            L++
        }

        count += R - L + 1
    }
    
    console.log(count)
}

/*
2 6 4 3 6 8 9

R = 0 -> 2
R = 1 -> 26 6
R = 2 -> 264 64 4
R = 3 -> 2643 643 43 3
R = 4 -> 6436 436 36 6

Каждый элемент - отдельный отрезок, т.е: 2, 6, 4, 3, 6, 8, 9

Сочетания: 26, 264, 64, 2643, 643, 43, 6436, 436, 36, 368, 68, 89, 

Кол-во сочетаний в хорошем отрезке - это сумма ариф.прогрессии. Арифметическая прогрессия от 1 до длины наидленнейшего хорошего подотрезка: L + R - 1

Получается, что к общему кол-ву хороших подотрезков прибавляем сумму ариф.прогрессии: 
const length = L + R - 1
count += ((1 + length) * length ) / 2

Проблема в том, что отрезки могут пересекаться: 2 6 4 3 и 6 4 3 6.
Получается, что не нужно дважды для каждого хорошего отрезка считать сумму ариф.прогрессии. Как избежать подсчёта одних и тех же подотрезков дважды?
*/