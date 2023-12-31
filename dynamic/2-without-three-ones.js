/*
Определите количество последовательностей из нулей и единиц длины n, в которых никакие три единицы не стоят рядом.

Формат входных данных
    Вводится натуральное число n, не превосходящее 40.
Формат выходных данных
    Выведите количество искомых последовательностей. Гарантируется, что ответ не превосходит 2^31−1

Ввод
3
Вывод
7
*/

const calc = (n) => {
    if(n === 0) {
        return 0
    }

    const dp = []

    dp[0] = 2
    dp[1] = 4
    dp[2] = 7

    if(n < 3) {
        return dp[n-1]
    }

    for(let i = 3; i < n; i++) {
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    }

    console.log(dp)

    return dp[n-1]
}


[1, 2, 3, 4].forEach(n => {
    console.log(calc(n));
})

/*
0000
0001
1001
0101
0011
0010
0110
0100
1100
1000
1001
1011
1101
*/