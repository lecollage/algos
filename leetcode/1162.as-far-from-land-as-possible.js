/*
 * @lc app=leetcode id=1162 lang=javascript
 *
 * [1162] As Far from Land as Possible
 */

// @lc code=start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxDistance = function (grid) {
    const queue = []
    const visited = []

    for (let i = 0; i < grid.length; i++) {
        visited.push([])

        for (let j = 0; j < grid[i].length; j++) {
            visited[i].push(false)

            if (grid[i][j] === 1) {
                queue.push({ index: [i, j], layer: 0 })
                visited[i][j] = true
            }
        }
    }


    // console.log(queue)

    let maxLayer = -1

    while (queue.length) {
        const { index: [i, j], layer } = queue.shift()

        if (i > 0) {
            if (!visited[i - 1][j]) {
                queue.push({ index: [i - 1, j], layer: layer + 1 })
                visited[i - 1][j] = true
                maxLayer = maxLayer > layer + 1 ? maxLayer : layer + 1
            }
        }

        if (j > 0) {
            if (!visited[i][j - 1]) {
                queue.push({ index: [i, j - 1], layer: layer + 1 })
                visited[i][j - 1] = true
                maxLayer = maxLayer > layer + 1 ? maxLayer : layer + 1
            }
        }

        if (i < grid.length - 1) {
            if (!visited[i + 1][j]) {
                queue.push({ index: [i + 1, j], layer: layer + 1 })
                visited[i + 1][j] = true
                maxLayer = maxLayer > layer + 1 ? maxLayer : layer + 1
            }
        }

        if (j < grid[i].length - 1) {
            if (!visited[i][j + 1]) {
                queue.push({ index: [i, j + 1], layer: layer + 1 })
                visited[i][j + 1] = true
                maxLayer = maxLayer > layer + 1 ? maxLayer : layer + 1
            }
        }

        // console.log(queue)
    }

    return maxLayer
};
// @lc code=end


{
    const grid = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]
    const expected = 2
    const result = maxDistance(grid)

    console.log(expected === result)
    console.log('------------------')
}



{
    const grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    const expected = 4
    const result = maxDistance(grid)

    console.log(expected === result)
    console.log('------------------')
}