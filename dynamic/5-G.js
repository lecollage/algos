/**
 * @param {number} N
 * @param {number} M
 * @return {number}
 */
var calcPathsCount = function(N, M) {
    if(N === 0) {
        return 0
    }

    // prepare the matrix (N+2xM+2) with paddings contain zero 
    N += 2
    M += 2

    const mtx = new Array(N)

    for(let i = 0; i < N; i++) {
        mtx[i] = new Array(M).fill(0)
    }

    // init the position
    mtx[2][2] = 1

    // do the calculation
    for(let i = 2; i < N; i++) {
        for(let j = 2; j < M; j++) {
            mtx[i][j] += mtx[i-2][j-1] + mtx[i-1][j-2]
        }
    }

    console.log(mtx)

    return mtx[N-1][M-1]
};


[
    [4, 4],
    [6, 5],
].forEach(([n, m]) => {
    const count = calcPathsCount(n, m)
    console.log(count);
    console.log();
})

/*
[
  [
    0, 0, 0, 0, 0, 0, 0
    0, 0, 0, 0, 0, 0, 0
    0, 0, 1, 0, 0, 0, 0
    0, 0, 0, 0, 1, 0, 0
    0, 0, 0, 1, 0, 0, 1
    0, 0, 0, 0, 0, 2, 0
    0, 0, 0, 0, 1, 0, 0
    0, 0, 0, 0, 0, 0, 3
  ]
]
*/