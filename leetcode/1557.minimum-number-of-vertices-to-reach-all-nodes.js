/*
 * @lc app=leetcode id=1557 lang=javascript
 *
 * [1557] Minimum Number of Vertices to Reach All Nodes
 */

// @lc code=start
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findSmallestSetOfVertices = function (n, edges) {
    const vertices = new Array(n).fill(false)

    for (let i = 0; i < edges.length; i++) {
        const [_, to] = edges[i]

        vertices[to] = true
    }

    const minVerticesSet = []
    
    for (let i = 0; i < n; i++) {
        if(!vertices[i]) {
            minVerticesSet.push(i)
        }
    }
    
    // console.log(vertices)
    // console.log(minVerticesSet)

    return minVerticesSet
};
// @lc code=end


{
    const n = 6
    const edges = [
        [0, 1],
        [0, 2],
        [2, 5],
        [3, 4],
        [4, 2]
    ]
    const expected = [0, 3]
    const result = findSmallestSetOfVertices(n, edges)
    let isEqual = true

    for (let i = 0; i < expected.length; i++) {
        const node = expected[i]

        if (!result.includes(node)) {
            isEqual = false
        }
    }

    if (expected.length !== result.length) {
        isEqual = false
    }

    console.log(isEqual)
}


{
    const n = 5
    const edges = [
        [0, 1],
        [2, 1],
        [3, 1],
        [1, 4],
        [2, 4]
    ]
    const expected = [0, 2, 3]
    const result = findSmallestSetOfVertices(n, edges)
    let isEqual = true

    for (let i = 0; i < expected.length; i++) {
        const node = expected[i]

        if (!result.includes(node)) {
            isEqual = false
        }
    }

    if (expected.length !== result.length) {
        isEqual = false
    }

    console.log(isEqual)
}


{
    const n = 3
    const edges = [
        [1, 2],
        [1, 0],
        [0, 2]
    ]
    const expected = [1]
    const result = findSmallestSetOfVertices(n, edges)
    let isEqual = true

    for (let i = 0; i < expected.length; i++) {
        const node = expected[i]

        if (!result.includes(node)) {
            isEqual = false
        }
    }

    if (expected.length !== result.length) {
        isEqual = false
    }

    console.log(isEqual)
}

return
