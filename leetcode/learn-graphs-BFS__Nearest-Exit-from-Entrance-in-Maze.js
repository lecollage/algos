class Node {
    next
    value

    constructor(value) {
        this.value = value
    }
}

class MyQueue {
    _head = null
    _tail = null

    length = 0

    constructor() { }

    push(value) {
        const node = new Node(value)

        if (!this._head) {
            this._head = node
            this._tail = node
            this.length++

            return
        }

        this._tail.next = node
        this._tail = this._tail.next
        this.length++
    }

    pop() {
        if (!this._head) {
            return null
        }

        const node = this._head

        if (this._tail === this._head) {
            this._tail = null
            this._head = null
        } else {
            this._head = this._head.next
        }

        this.length--

        return node.value
    }
}


/**
 * @param {character[][]} maze
 * @param {number[]} entrance
 * @return {number}
 */
var nearestExit = function (maze, entrance) {
    const [startI, startJ] = entrance

    maze[startI][startJ] = '+'

    const queue = new MyQueue()

    queue.push(entrance)

    const directions = [
        [-1, 0],
        [1, 0],
        [0, 1],
        [0, -1],
    ]
    const isValid = (i, j) => {
        if (i < 0) {
            return false
        }

        if (i >= maze.length) {
            return false
        }

        if (j < 0) {
            return false
        }

        if (j >= maze[i].length) {
            return false
        }

        return true
    }

    while (queue.length) {
        const [i,j] = queue.pop()

        for(const direction of directions) {
            const [di, dj] = direction
            const newI = i + di
            const newJ = j + dj

            if(isValid(newI, newJ) && maze[newI][newJ] !== '+') {
                queue.push([newI, newJ])
                maze[newI][newJ] = '+'
            }
        }
    }

    console.log(maze)
};

{
    const maze = [
        ["+", "+", ".", "+"],
        [".", ".", ".", "+"],
        ["+", "+", "+", "."]
    ]
    const entrance = [1, 2]
    const expected = 1
    const result = nearestExit(maze, entrance)

    console.log(expected === result)
    console.log('------------------')
}

{
    const maze = [
        ["+", "+", "+"],
        [".", ".", "."],
        ["+", "+", "+"]
    ]
    const entrance = [1, 0]
    const expected = 2
    const result = nearestExit(maze, entrance)

    console.log(expected === result)
    console.log('------------------')
}

{
    const maze = [
        [".", "+"]
    ]
    const entrance = [0, 0]
    const expected = -1
    const result = nearestExit(maze, entrance)

    console.log(expected === result)
    console.log('------------------')
}

