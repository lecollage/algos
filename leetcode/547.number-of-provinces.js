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
    const visited = new Set()

    for (let i = 0; i < matrix[0].length; i++) {
        const stack = []

        stack.push(i)

        let isNewProvince = false

        while (stack.length) {
            const node = stack.pop()
            
            if (!visited.has(node)) {
                console.log(`Visited: ${node}`);
                visited.add(node)

                isNewProvince = true

                for (let neighbour = 0; neighbour < matrix[node].length; neighbour++) {
                    if (!visited.has(neighbour) && matrix[node][neighbour] === 1) {
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
    const matrix =     [
        [1,1,0],
        [1,1,0],
        [0,0,1]
    ]

    console.log(findCircleNum(matrix))
}
