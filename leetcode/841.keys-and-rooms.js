/*
 * @lc app=leetcode id=841 lang=javascript
 *
 * [841] Keys and Rooms
 */

// @lc code=start
/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function (rooms) {
    const graph = new Map()

    for (let i = 0; i < rooms.length; i++) {
        graph.set(i, rooms[i])
    }

    // console.log(graph)

    const stack = [0]
    const visited = new Set()

    visited.add(0)

    while (stack.length) {
        const node = stack.pop()
        const neighbours = graph.get(node)

        for (let i = 0; i < neighbours.length; i++) {
            const neighbour = neighbours[i]
            
            if (!visited.has(neighbour)) {
                visited.add(neighbour)
                stack.push(neighbour)
            }
        }
    }

    // console.log(visited)

    return visited.size === rooms.length
};
// @lc code=end





{
    const rooms = [
        [1],
        [2],
        [3],
        []
    ]
    const expected = true
    const result = canVisitAllRooms(rooms)

    console.log(expected === result)
}

{
    const rooms = [
        [1, 3],
        [3, 0, 1],
        [2],
        [0]
    ]
    const expected = false
    const result = canVisitAllRooms(rooms)

    console.log(expected === result)
}