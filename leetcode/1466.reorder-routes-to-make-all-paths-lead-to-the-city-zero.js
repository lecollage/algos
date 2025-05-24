/*
 * @lc app=leetcode id=1466 lang=javascript
 *
 * [1466] Reorder Routes to Make All Paths Lead to the City Zero
 */

// @lc code=start
/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function(n, connections) {
    const directedGraph = new Map()
    const undirectedGraph = new Map()

    for(let i = 0; i < n; i++) {
        directedGraph.set(i, [])
        undirectedGraph.set(i, [])
    }

    for(let i = 0; i < connections.length; i++) {
        const [from, to] = connections[i]

        directedGraph.set(from, [...directedGraph.get(from), to])
        undirectedGraph.set(from, [...undirectedGraph.get(from), to])
        undirectedGraph.set(to, [...undirectedGraph.get(to), from])
    }

    console.log(directedGraph)
    console.log(undirectedGraph)

    const visited = new Set()
    let swapCount = 0
    const dfs = (node) => {
        const neighbours = undirectedGraph.get(node)

        console.log()
        console.log(node, neighbours)

        for(let i = 0; i < neighbours.length; i++) {
            const neighbour = neighbours[i]
            console.log(node, neighbour, directedGraph.get(neighbour))
            
            if(!directedGraph.get(neighbour).includes(node)) {
                swapCount++
                console.log(`swap`, swapCount)
            }

            if(!visited.has(node)) {
                visited.add(node)
                dfs(neighbour)
            }
        }
    }

    dfs(0)


    return swapCount
};
// @lc code=end

{
    const n = 3
    const matrix = [
        [1,0],
        [2,0]
    ]

    const answer = minReorder(n, matrix)
    const expected = 0

    console.log(answer === expected, answer)
}

return;

{
    const n = 6
    const matrix = [
        [0,1],
        [1,3],
        [2,3],
        [4,0],
        [4,5]
    ]

    const answer = minReorder(n, matrix)

    console.log(answer === 3, answer)
}

/*
0: [1]
1: [3]
2: [3]
3: []
4: [0, 5]
5: []

0: [1, 4]
1: [0, 3]
2: [3]
3: [1, 2]
4: [0, 5]
5: [4]

to: 0 from: 1
swap

to: 1 from: 3
swap

to: 3 from: 2
no swap

to: 0 from: 4
no swap

to: 4 from: 5
swap




0, 1, 3, 2






0: [1]
1: [0, 3]
2: [3]
3: [1, 2]
4: [0, 5]


   0 1 2 3 4 5
0  0 1 0 0 0 0
1  0 0 0 1 0 0 
2  0 0 0 1 0 0
3  0 0 0 0 0 0
4  1 0 0 0 0 1
5  0 0 0 0 0 0

   0 1 2 3 4 5
0  0 1 0 0 1 0
1  1 0 0 1 0 0
2  0 0 0 1 0 0
3  0 1 1 0 0 0
4  1 0 0 0 0 1
5  0 0 0 0 1 0

  
  
  
  
  
  



   0 1 2 3 4 5
0  0 0 0 0 0 0
1  1 0 0 0 0 0 
2  0 0 0 1 0 0
3  0 1 0 0 0 0
4  1 0 0 0 0 0
5  0 0 0 0 1 0


1



0 

-> 1

0 <- 1

1 

*/



/*
[
    [1,0],
    [1,2],
    [3,2],
    [3,4]
]

   0 1 2 3 4
0  0 0 0 0 0
1  1 0 1 0 0 
2  0 0 0 0 0
3  0 0 1 0 0
4  0 0 0 0 0

   0 1 2 3 4
0  0 0 0 0 0
1  1 0 0 0 0 
2  0 1 0 0 0
3  0 0 1 0 0 
4  0 0 0 1 0
*/

{
    const n = 5
    const matrix = [
        [1,0],
        [1,2],
        [3,2],
        [3,4]
    ]

    const answer = minReorder(n, matrix)
    const expected = 2

    console.log(answer === expected, answer)
}



{
    const n = 3
    const matrix = [
        [1,0],
        [2,0]
    ]

    const answer = minReorder(n, matrix)
    const expected = 0

    console.log(answer === expected, answer)
}