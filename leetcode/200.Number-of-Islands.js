/*
 * @lc app=leetcode id=200 lang=javascript
 *
 * [200] Number of Islands
 */

// @lc code=start
const explore = (startI, startJ, matrix) => {
    const stack = []

    stack.push([startI, startJ])

    while(stack.length) {
        const [i, j] = stack.pop()

        if (matrix[i-1] && matrix[i-1][j] === '1') {
            matrix[i-1][j] = '0'
            stack.push([i-1, j])
        }

        if (matrix[i+1] && matrix[i+1][j] === '1') {
            matrix[i+1][j] = '0'
            stack.push([i+1, j])
        }

        if (matrix[i][j-1] === '1') {
            matrix[i][j-1] = '0'
            stack.push([i, j-1])
        }

        if (matrix[i][j+1] === '1') {
            matrix[i][j+1] = '0'
            stack.push([i, j+1])
        }
    }
}

/**
 * @param {string[][]} isConnected
 * @return {number}
 */
var numIslands = function(matrix) {
    if(!matrix || !matrix[0]) {
        return 0
    }

    let islands = 0

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] === '1') {
                explore(i, j, matrix)
                islands++
            }
        }
    }

    return islands
};
// @lc code=end

{
    const matrix = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
      ]

    console.log(numIslands(matrix) === 1)
}

{
    const matrix = [
    ]

    console.log(numIslands(matrix) === 0)
}

{
    const matrix = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","1"]
      ]

    console.log(numIslands(matrix) === 3)
}
