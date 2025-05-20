/*
 * @lc app=leetcode id=547 lang=javascript
 *
 * [547] Number of Provinces
 */

// @lc code=start
const explore = (startI, startJ, matrix) => {
    const stack = []

    stack.push([startI, startJ])

    while(stack.length) {
        const [i, j] = stack.pop()

        if (matrix[i-1] && matrix[i-1][j] === 1) {
            matrix[i-1][j] = 0
            stack.push([i-1, j])
        }

        if (matrix[i+1] && matrix[i+1][j]) {
            matrix[i+1][j] = 0
            stack.push([i+1, j])
        }

        if (matrix[i][j-1]) {
            matrix[i][j-1] = 0
            stack.push([i, j-1])
        }

        if (matrix[i][j+1]) {
            matrix[i][j+1] = 0
            stack.push([i, j+1])
        }
    }
}

const isConnected = (i, j, matrix) => {
        if (matrix[i-1] && matrix[i-1][j]) {
            return true
        }

        if (matrix[i+1] && matrix[i+1][j]) {
            return true
        }

        if (matrix[i][j-1]) {
            return true
        }

        if (matrix[i][j+1]) {
            return true
        }

        return false
}


/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(matrix) {
    if(!matrix || !matrix[0]) {
        return 0
    }

    let provinces = 0

    for (let i = 0; i < matrix[0].length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] === 1) {
                if (isConnected(i, j, matrix)) {
                    explore(i, j, matrix)
                    provinces++
                } else {
                    matrix[i][j] = 0
                }
            }
        }
    }

    return provinces
};
// @lc code=end

{
    const matrix = [
        [1,1,0],
        [1,1,0],
        [0,0,1]
    ]

    console.log(findCircleNum(matrix))
}

{
    const matrix = [
    ]

    console.log(findCircleNum(matrix))
}

{
    const matrix = [
        [1,1,0,1,1,0,1],
        [1,1,0,1,1,0,1],
        [0,0,1,0,0,0,1],
        [0,0,1,1,1,0,1],
        [0,0,1,0,0,0,1],
        [0,0,1,0,1,0,1],
        [0,0,1,0,1,0,1]
    ]

    console.log(findCircleNum(matrix))
}

{
    const matrix = [
        [1,0,0,1],
        [0,1,1,0],
        [0,1,1,1],
        [1,0,1,1]
    ]

    console.log(findCircleNum(matrix))
}

{
    [
        [1,1,0],
        [1,1,0],
        [0,0,1]
    ]
}


i j == 1 -> neighbour

0: [0, 1]
1: [0, 1]
2: [2]




0: Set(0,1)

const set = new Set()

if (set.has(matrix[i][j])) {
    set.add()
}

