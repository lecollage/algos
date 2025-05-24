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
    const directedGraph = []
    const undirectedGraph = []

    for (let i = 0; i < n; i++) {
        directedGraph.push(new Array(n).fill(0))
        undirectedGraph.push(new Array(n).fill(0))
    } 

    for (let i = 0; i < connections.length; i++) {
        let [from, to] = connections[i]

        directedGraph[from][to] = 1

        undirectedGraph[from][to] = 1
        undirectedGraph[to][from] = 1
    }

    console.log(directedGraph)
    console.log(undirectedGraph)

    const visited = new Set()
    const stack = [{el: 0, to: 0}]
    let swapCount = 0

    while(stack.length) {
        const {el, to} = stack.pop()

        if(!visited.has(el)) {
            for(let i = 0; i < n; i++) {
                if(undirectedGraph[el][i] === 1) {
                    stack.push({el: i, to: el})

                    if(directedGraph[el][to] === 1) {
                        console.log(el, to)
                        swapCount++
                    }
                }
            }
        }

        visited.add(el)
    }

    console.log(visited)

    return swapCount
};
// @lc code=end

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