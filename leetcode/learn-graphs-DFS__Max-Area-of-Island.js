/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
    const visited = []

    for (let i = 0; i < grid.length; i++) {
        visited.push([])

        for (let j = 0; j < grid[i].length; j++) {
            visited[i].push(false)
        }
    }

    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    const m = grid.length
    const n = grid[0].length
    const valid = (row, col) => 0 <= row && row < m && 0 <= col && col < n && grid[row][col] == 1
    const dfs = (startI, startJ) => {
        let area = 0
        const stack = [[startI, startJ]]

        while (stack.length) {
            const [row, col] = stack.pop()

            area++

            // console.log(row, col)

            for (const [dx, dy] of directions) {
                const nextRow = row + dy
                const nextCol = col + dx

                if (valid(nextRow, nextCol) && !visited[nextRow][nextCol]) {
                    visited[nextRow][nextCol] = true
                    stack.push([nextRow, nextCol])
                }
            }
        }

        return area
    }

    let maxArea = 0

    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === 1 && !visited[i][j]) {
                visited[i][j] = true

                const area = dfs(i, j)

                // console.log(`area: ${area}`)

                maxArea = area > maxArea ? area : maxArea
            }
        }
    }

    // console.log(maxArea)
    // console.log(visited)

    return maxArea
};

{
    const grid = [
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ]
    const expected = 6
    const result = maxAreaOfIsland(grid)

    console.log(expected === result, `result: ${result}`)
    console.log('------------------')
}

{
    const grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    const expected = 6
    const result = maxAreaOfIsland(grid)

    console.log(expected === result, `result: ${result}`)
    console.log('------------------')
}

{
    const grid = [
        [0, 0, 1],
        [0, 0, 0],
        [0, 1, 1],
        [0, 1, 0],
    ]
    const expected = 3
    const result = maxAreaOfIsland(grid)

    console.log(expected === result)
    console.log('------------------')
}


{
    const grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    const expected = 0
    const result = maxAreaOfIsland(grid)

    console.log(expected === result)
    console.log('------------------')
}

return 
