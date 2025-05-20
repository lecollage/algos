/*
 * @lc app=leetcode id=547 lang=javascript
 *
 * [547] Number of Provinces
 */

// @lc code=start
/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(matrix) {
    if(!matrix || !matrix[0]) {
        return 0
    }

    let provinces = 0
    const visited = new Array(matrix.length)
    
    visited.fill(false)

    for (let i = 0; i < matrix[0].length; i++) {
        const stack = []

        stack.push(i)

        let isNewProvince = false

        while (stack.length) {
            const node = stack.pop()

            if (!visited[node]) {
                console.log(`Visited: ${node}`);
                visited[node] = true

                isNewProvince = true

                for (let neighbour = 0; neighbour < matrix[node].length; neighbour++) {
                    if (!visited[neighbour] && matrix[node][neighbour] === 1) {
                        stack.push(neighbour)
                    }
                }
            }
        }

        if (isNewProvince) {
            provinces++
            isNewProvince = false
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

