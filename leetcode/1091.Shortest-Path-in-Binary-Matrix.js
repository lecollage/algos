class MyQueue {
    array = []
    length = 0

    constructor(node) {
        this.array.push(node)
        this.length++
    }

    pop() {
        const node = this.array.shift()
        this.length--

        return node
    }

    push(node) {
        this.array.push(node)
        this.length++
    }
}

/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function (grid) {
    if (grid[0][0] === 1) {
        return -1
    }

    const directions = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1],
    ]
    const isValidCoordinate = (i, j) => {
        const isIValid = i >= 0 && i < grid.length

        if (!isIValid) {
            return false
        }

        const isJValid = j >= 0 && j < grid[i].length

        if (!isJValid) {
            return false
        }

        return true
    }
    const queue = new MyQueue({ i: 0, j: 0, depth: 0 })

    grid[0][0] = 1

    while (queue.length) {
        const { i, j, depth } = queue.pop()

        if (i === grid.length - 1 && j === grid[i].length - 1) {
            return depth + 1
        }

        for (const [di, dj] of directions) {
            const newI = i + di
            const newJ = j + dj

            if (isValidCoordinate(newI, newJ) && grid[newI][newJ] === 0) {
                grid[newI][newJ] = 1

                queue.push({ i: newI, j: newJ, depth: depth + 1 })
            }
        }
    }

    // console.log(grid)

    return -1
};

{
    const grid = [[0, 1], [1, 0]]
    const expected = 2
    const result = shortestPathBinaryMatrix(grid)

    console.log(expected === result)
    console.log('------------------')
}

{
    const grid = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    const expected = 4
    const result = shortestPathBinaryMatrix(grid)

    console.log(expected === result)
    console.log('------------------')
}

{
    const grid = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    const expected = 8
    const result = shortestPathBinaryMatrix(grid)

    console.log(expected === result, result)
    console.log('------------------')
}

{
    const grid = [
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    const expected = -1
    const result = shortestPathBinaryMatrix(grid)

    console.log(expected === result)
    console.log('------------------')
}