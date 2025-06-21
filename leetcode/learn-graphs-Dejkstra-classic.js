const { MinPriorityQueue } = require('@datastructures-js/priority-queue');


// process.stdin.resume();
// process.stdin.setEncoding("utf-8");

// let inputArray = [];
// let inputString = "";
// let currentLine = 0;

// process.stdin.on("data", (inputStdin) => {
//     inputArray.push(inputStdin)
// });

// process.stdin.on("end", (_) => {
//     inputString = inputArray.join('')
//     inputString = inputString
//         .trim()
//         .split("\n")
//         .map((string) => {
//             return string.trim();
//         });

//     main();
// });

// function readline() {
//     return inputString[currentLine++];
// }

/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var dijkstra = function (weightedEdges, n, m) {
    const N = n + 1

    // prepare graphs
    const graph = []
    const sums = []

    for (let i = 0; i < N; i++) {
        graph.push([])
        sums.push(Infinity)
    }

    for (let i = 0; i < weightedEdges.length; i++) {
        const [from, to, wieght] = weightedEdges[i]

        graph[from].push([to, wieght])
    }

    sums[1] = 0

    console.log(graph)

    for (let node = 1; node < N; node++) {
        
    }

    // const wieghtedNeighbours = graph[node]

    // for (let j = 0; j < wieghtedNeighbours.length; j++) {
    //     const [from, to, weight] = wieghtedNeighbours[j]


    // }

};
// @lc code=end

{
    // 5 6
    const weightedEdges = [
        [1, 2, 2],
        [2, 5, 5],
        [2, 3, 4],
        [1, 4, 1],
        [4, 3, 3],
        [3, 5, 1]
    ]
    const n = 5
    const m = 6;
    const expected = [1, 4, 3, 5] // output;
    const result = dijkstra(weightedEdges, n, m);

    console.log(expected === result, result);
    console.log("------------------");
}
