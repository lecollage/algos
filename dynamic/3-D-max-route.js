/**
 * @param {number} mtx
 * @return {number}
 */
var calcMostExpensivePath = function(mtx) {
    if(!mtx?.length) {
        return {
            sum: 0,
            path: [],
        }
    }

    const m = mtx.length
    const n = mtx[0]?.length || 0

    let path = []

    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            const top = i > 0 ? mtx[i - 1][j] : 0
            const left = j > 0 ? mtx[i][j - 1] : 0

            mtx[i][j] += Math.max(top, left)
        }
    }

    console.log(`2: `, JSON.stringify(mtx))

    return {
        sum: mtx[m - 1][n - 1],
        path,
    }
};

[
    [],
    [[1]],
    [[1, 1]],
    [[1], [1]],
    [
        [9, 9, 9, 9, 9],
        [3, 0, 0, 0, 0],
        [9, 9, 9, 9, 9],
        [6, 6, 6, 6, 8],
        [9, 9, 9, 9, 9]
    ]
].forEach((mtx) => {
    const {sum, path} = calcMostExpensivePath(mtx)
    console.log(sum);
    console.log(path);
    console.log();
})
