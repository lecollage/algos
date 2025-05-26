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
    const undirectedGraph = new Map()

    for (let i = 0; i < n; i++) {
        undirectedGraph.set(i, [])
    }

    const roads = new Set()
    const getHash = (from, to) => `${from},${to}`

    for (let i = 0; i < connections.length; i++) {
        const [from, to] = connections[i]

        undirectedGraph.set(from, [...undirectedGraph.get(from), to])
        undirectedGraph.set(to, [...undirectedGraph.get(to), from])
        roads.add(getHash(from, to))
    }

    // console.log(undirectedGraph)

    let swapCount = 0
    const visited = new Array(n).fill(false)

    visited[0] = true

    const dfs = (node) => {
        const neighbours = undirectedGraph.get(node)

        for (let i = 0; i < neighbours.length; i++) {
            const neighbour = neighbours[i]

            if(!visited[neighbour]) {
                visited[neighbour] = true

                const wrongDirection = getHash(node, neighbour)

                if(roads.has(wrongDirection)) {
                    swapCount++

                    // console.log(`swap`, wrongDirection, node, neighbour, swapCount)
                }

                dfs(neighbour)
            }
        }
    }

    dfs(0)

    return swapCount
};
// @lc code=end

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

/*
0<-1->2<-3->4

*/


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

roads
[0,1]
[1,3]
[2,3]
[4,0]
[4,5]


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
