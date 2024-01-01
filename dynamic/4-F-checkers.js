/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var calcPathsCount = function(posJ, posI) {
    if(posI === 8) {
        return 0
    }

    // prepare the matrix NxM with paddings (0..7 + 2)
    const N = 9, M = 10

    const mtx = new Array(N)

    for(let i = 0; i < N; i++) {
        mtx[i] = new Array(M).fill(0)
    }


    // init the position
    mtx[posI][posJ] = 1

    // calc entire matrix
    for (let i = 1; i < N; i++) {
        for (let j = 1; j < M - 1; j++) {
            mtx[i][j] += mtx[i-1][j-1] + mtx[i-1][j+1]
        }
    }

    // console.log(mtx)

    // sum the last row
    for(let j = 1; j < M - 1; j++) {
        mtx[N-1][j] += mtx[N-1][j-1]
    }

    return mtx[N-1][M-2]
};


[
    [3, 7],
    [3, 6],
    [1, 1],
    [1, 8],
    [8, 1],
    [8, 8],
].forEach(([n, m]) => {
    const count = calcPathsCount(n, m)
    console.log(count);
    console.log();
})
