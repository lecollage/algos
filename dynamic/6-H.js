/**
 * @param {number} N
 * @param {number} M
 * @return {number}
 */
var calcPathsCount = function(N, M) {
    if(N === 0) {
        return 0
    }

    // prepare the matrix (N+3 x M+3) with paddings contain zero 
    const padN = N + 3
    const padM = M + 3
    const mtx = new Array(padN)

    for(let i = 0; i < padN; i++) {
        for(let j = 0; j < padM; j++) {
            mtx[i] = new Array(padM).fill(0)
        }
    }

    // init the position
    mtx[2][2] = 1

    // solution might work, but not finished >> 
    // starting i is fixed, j is changing
    // for(let artI = 2; artI < N - 1; artI++) {
    //     const x = []
    //     for(let i = 2, j = artI; i <= artI && j > 1; i++, j--) {
    //         x.push(`${i},${j}`)

    //         mtx[i][j] += mtx[i-2][j-1] + mtx[i-2][j+1] + mtx[i-1][j-2] + mtx[i+1][j-2]
    //     }
    //     console.log(x.join(';'))
    // }

    // const diffI = M-N

    // for(let artI = M - 1; artI < M + diffI; artI++) {
    //     for(let i = artI, j = 2; i > artI && j > 2; i--, j--) {

    //     }
    // }

    // for(let artJ = 3; artJ < M - 1; artJ++) {
    //     const x = []
    //     for(let i = artJ, j = M - 2; i < N-1 && j > 2; i++, j--) {
    //         x.push(`${i},${j}`)

    //         mtx[i][j] += mtx[i-2][j-1] + mtx[i-2][j+1] + mtx[i-1][j-2] + mtx[i+1][j-2]
    //     }
    //     console.log(x.join(';'))
    // }
    // <<

    // do the calculation
    // the matrix diagonal traversal algorithm is taken from https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/
    for (let line = 1; line <= (N + M - 1); line++) {
        const startCol = Math.max(0, line - N);
        const count = Math.min(line, (M - startCol), N); 

        for (let j = 0; j < count; j++) {
            const I = Math.min(N, line) - j - 1 + 2 // add top padding size 
            const J = startCol + j + 2              // add left padding size 
            mtx[I][J] += mtx[I-2][J-1] + mtx[I-2][J+1] + mtx[I-1][J-2] + mtx[I+1][J-2]
        }
    } 

    // console.log(mtx)

    return mtx[padN-2][padM-2]
};


[
    // [4, 4],
    [7, 15],
].forEach(([n, m]) => {
    const count = calcPathsCount(n, m)
    console.log(count);
    console.log();
})

/*
[
  [
    0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 
    0, 0, 1, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 
  ]
]

[
  [
    0, 0, 0, 0, 0, 0, 0, 0, 0
    0, 0, 0, 0, 0, 0, 0, 0, 0
    0, 0, 1, 0, 0, 0, 0, 0, 0
    0, 0, 0, 0, 1, 0, 0, 0, 0
    0, 0, 0, 1, 0, 0, 1, 2, 0
    0, 0, 0, 0, 0, 2, 0, 0, 0
    0, 0, 0, 0, 0, 0, 0, 0, 0
  ]
]

[
  [
    0, 0, 0, 0, 0, 0, 0
    0, 0, 0, 0, 0, 0, 0
    0, 0, 1, 0, 0, 0, 0
    0, 0, 0, 0, 1, 1, 0
    0, 0, 0, 1, 0, 1, 0
    0, 0, 0, 1, 1, 2, 0
    0, 0, 0, 0, 0, 0, 0
]
*/