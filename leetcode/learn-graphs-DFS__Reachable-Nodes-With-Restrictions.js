/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} restricted
 * @return {number}
 */
var reachableNodes = function (n, edges, restricted) {
    const graph = []

    for (let i = 0; i < n; i++) {
        graph.push([])
    }

    for (let i = 0; i < edges.length; i++) {
        const [from, to] = edges[i]

        graph[from].push(to)
        graph[to].push(from)
    }

    // console.log(JSON.stringify(graph))

    for (let i = 0; i < restricted.length; i++) {
        const restrictedNode = restricted[i]

        // One level removal
        const neighbours = graph[restrictedNode]

        for (const neighbour of neighbours) {
            graph[neighbour] = graph[neighbour].filter(n => n !== restrictedNode)
        }

        graph[restrictedNode] = []
    }

    // console.log(JSON.stringify(graph, null, 1))

    // DFS from 0

    let visitedCount = 1
    const visited = new Array(n).fill(false)
    const dfs = start => {
        const stack = [start]

        while (stack.length) {
            const node = stack.pop()
            const neighbours = graph[node]

            for (const neighbour of neighbours) {
                if (!visited[neighbour]) { 
                    stack.push(neighbour)
                    visited[neighbour] = true
                    visitedCount++
                }
            }
        }
    }

    visited[0] = true
    dfs(0)

    // console.log(visited)

    return visitedCount
};

{
    const n = 7
    const edges = [
        [0, 1],
        [1, 2],
        [3, 1],
        [4, 0],
        [0, 5],
        [5, 6]
    ]
    const restricted = [4, 5]
    const expected = 4
    const result = reachableNodes(n, edges, restricted)

    console.log(expected === result)
    console.log('------------------')
}
/*
[
    0: [1,4,5],
    1: [0,2,3],
    2: [1],
    3: [1],
    4: [0],
    5: [0,6],
    6: [5]
]

[
    0: [1],
    1: [0,2,3],
    2: [1],
    3: [1],
    4: [],
    5: [],
    6: []
]
*/

{
    const n = 7
    const edges = [
        [0, 1],
        [0, 2],
        [0, 5],
        [0, 4],
        [3, 2],
        [6, 5]
    ]
    const restricted = [4, 2, 1]
    const expected = 3
    const result = reachableNodes(n, edges, restricted)

    console.log(expected === result)
    console.log('------------------')
}