/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var validPath = function (n, edges, source, destination) {
    const graph = new Map()
    const visited = []

    for (let i = 0; i < n; i++) {
        graph.set(i, [])
        visited.push(false)
    }

    for (let i = 0; i < edges.length; i++) {
        const [from, to] = edges[i]

        graph.set(from, [...graph.get(from), to])
        graph.set(to, [...graph.get(to), from])

        vs

        graph.get(from).push(to)
        graph.get(to).push(from)
    }

    // console.log(graph)

    const stack = [destination]

    visited[destination] = true

    while (stack.length) {
        const node = stack.pop()

        if (node === source) {
            return true
        }

        const neighbours = graph.get(node)

        for (let i = 0; i < neighbours.length; i++) {
            const neighbour = neighbours[i]

            if (!visited[neighbour]) {
                if (neighbour === source) {
                    return true
                }

                stack.push(neighbour)
                visited[neighbour] = true
            }
        }
    }

    return false
};

{
    const n = 3
    const edges = [
        [0, 1],
        [1, 2],
        [2, 0]
    ]
    const source = 0
    const destination = 2
    const expected = true
    const result = validPath(n, edges, source, destination)

    console.log(expected === result)
    console.log('------------------')
}

{
    const n = 6
    const edges = [
        [0, 1],
        [0, 2],
        [3, 5],
        [5, 4],
        [4, 3]
    ]
    const source = 0
    const destination = 5
    const expected = false
    const result = validPath(n, edges, source, destination)

    console.log(expected === result)
    console.log('------------------')
}
