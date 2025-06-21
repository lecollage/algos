const { MinPriorityQueue } = require('@datastructures-js/priority-queue');

/*
 * @lc app=leetcode id=787 lang=javascript
 *
 * [787] Cheapest Flights Within K Stops
 */

// @lc code=start
/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function (n, flights, src, dst, k) {
    // prepare graphs
    const fullGraph = []
    const visited = []
    const cutGraph = []

    for (let i = 0; i < n; i++) {
        fullGraph.push([])
        cutGraph.push([])
        visited.push(false)
    }

    for (let i = 0; i < flights.length; i++) {
        const [from, to, price] = flights[i]

        fullGraph[from].push([to, price])
    }

    // console.log(fullGraph)
    // console.log(cutGraph)

    // cut the graph by K
    const stack = []

    stack.push({ node: src, stops: 0 })
    visited[src] = true

    while (stack.length) {
        const { node, stops } = stack.pop()
        const pricedNeighbours = fullGraph[node]

        // console.log(pricedNeighbours, node, stops)

        for (let i = 0; i < pricedNeighbours.length; i++) {
            const [neighbour, price] = pricedNeighbours[i]

            if (!visited[neighbour] && stops < k || neighbour === dst) {
                stack.push({ node: neighbour, stops: stops + 1 })
                visited[neighbour] = true
                cutGraph[node].push([neighbour, price])
            }
        }
    }

    // console.log(visited)
    // console.log(cutGraph)

    // traverce cutGraph starting from src's neighbours
    const minHeap = new MinPriorityQueue(([node, price]) => price);

    for (let i = 0; i < cutGraph[src].length; i++) {
        const [neigbour, price] = cutGraph[src][i]

        minHeap.push([neigbour, price])
    }

    let sum = 0

    while (!minHeap.isEmpty()) {
        const [node, price] = minHeap.pop()

        sum = sum + price

        if (node === dst) {
            return sum
        }

        const pricedNeighbours = cutGraph[node]

        for (let i = 0; i < pricedNeighbours.length; i++) {
            const [neighbour, price] = pricedNeighbours[i]

            minHeap.push([neighbour, price])
        }
    }

    return -1
};
// @lc code=end

{
    const flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    const src = 0
    const dst = 3
    const k = 1
    const n = 4;

    const expected = 700;
    const result = findCheapestPrice(n, flights, src, dst, k);

    console.log(expected === result, result);
    console.log("------------------");
}

{
    const flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    const src = 0
    const dst = 3
    const k = 2
    const n = 4;

    const expected = 400;
    const result = findCheapestPrice(n, flights, src, dst, k);

    console.log(expected === result, result);
    console.log("------------------");
}

{
    const n = 3;
    const flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    const src = 0
    const dst = 2
    const k = 1

    const expected = 200;
    const result = findCheapestPrice(n, flights, src, dst, k);

    console.log(expected === result, result);
    console.log("------------------");
}

{
    const n = 3;
    const flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    const src = 0
    const dst = 2
    const k = 0

    const expected = 500;
    const result = findCheapestPrice(n, flights, src, dst, k);

    console.log(expected === result, result);
    console.log("------------------");
}