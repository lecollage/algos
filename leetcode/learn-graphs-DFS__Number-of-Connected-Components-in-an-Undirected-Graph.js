/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countComponents = function (n, edges) {
    const graph = []
    const visited = []

    for (let i = 0; i < n; i++) {
        graph.push([])
        visited.push(false)
    }

    for (let i = 0; i < edges.length; i++) {
        const [from, to] = edges[i]

        graph[from].push(to)
        graph[to].push(from)
    }

    // console.log(graph)

    const dfs = startNode => {
        const stack = [startNode]

        while (stack.length) {
            const node = stack.pop()
            const neighbours = graph[node]

            // console.log(node, neighbours)

            for (let i = 0; i < neighbours.length; i++) {
                const neighbour = neighbours[i]

                if (!visited[neighbour]) {
                    stack.push(neighbour)
                    visited[neighbour] = true
                }
            }
        }
    }

    let connectedComponentsCount = 0

    for (let i = 0; i < n; i++) {
        const node = i

        if (!visited[node]) {
            visited[node] = true
            connectedComponentsCount++
            dfs(node)
        }
    }

    return connectedComponentsCount
};

{
    const n = 5
    const edges = [
        [0, 1],
        [1, 2],
        [3, 4]
    ]
    const expected = 2
    const result = countComponents(n, edges)

    console.log(expected === result)
    console.log('------------------')
}

{
    const n = 5
    const edges = [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 4]
    ]
    const expected = 1
    const result = countComponents(n, edges)

    console.log(expected === result)
    console.log('------------------')
}