/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    // create matrix
    const mtx = new Array(m)

    for(let i = 0; i < m; i++) {
        mtx[i] = new Array(n).fill(0)
    }

    // console.log(`1: `, JSON.stringify(mtx))

    for(let i = 0; i < m; i++) {
        mtx[i][0] = 1
    }

    for(let j = 0; j < n; j++) {
        mtx[0][j] = 1
    }


    for(let i = 1; i < m; i++) {
        for(let j = 1; j < n; j++) {
            mtx[i][j] = mtx[i - 1][j] + mtx[i][j - 1]
        }
    }

    // console.log(`2: `, JSON.stringify(mtx))

    return mtx[m - 1][n - 1]
};

[
    // [0,0],
    [1,1],
    [3,7],
    [3,2],
].forEach(([m,n]) => {
    console.log(uniquePaths(m,n));
})



/*
m = 3, n = 7
28
*/
