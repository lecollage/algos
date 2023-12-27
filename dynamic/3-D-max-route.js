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
    const paths = new Array(m)

    for(let i = 0; i < m; i++) {
        const row = new Array(n)

        for(let j = 0; j < n; j++) {
            row[j] = ({
                prevI: -1,
                prevJ: -1,
                direction: ''
            })
        }

        paths[i] = row
    }


    // calc max; fill paths matrix 
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            const top = i > 0 ? mtx[i - 1][j] : 0
            const left = j > 0 ? mtx[i][j - 1] : 0

            if(top > left) {
                mtx[i][j] += top
                paths[i][j] = {
                    prevI: i - 1,
                    prevJ: j,
                    direction: 'D'
                }
            } else {
                mtx[i][j] += left
                paths[i][j] = {
                    prevI: i,
                    prevJ: j - 1,
                    direction: 'R'
                }
            }
        }
    }
    
    // reverse paths and calc the most expensive path
    const mostExpensivePath = []

    let i = m - 1, j = n - 1

    while(i > 0 || j > 0) {
        const curr = paths[i][j]

        mostExpensivePath.push(curr.direction)

        i = curr.prevI
        j = curr.prevJ
    }
    

    // console.log(`2: `, JSON.stringify(mtx))
    // console.log(`2: `, JSON.stringify(paths))

    return {
        sum: mtx[m - 1][n - 1],
        path: mostExpensivePath.reverse(),
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
