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

    constructor() {}

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


{
    const queue = new MyQueue()

    queue.push(1)
    queue.push(2)
    queue.push(3)

    console.log(JSON.stringify(queue, null, 2))

    console.log(queue.pop())
    console.log(queue.pop())
    console.log(queue.pop())
    console.log(queue.pop())
    console.log(queue.pop())

    console.log(JSON.stringify(queue, null, 2))

    queue.push(5)
    queue.push(6)

    console.log(queue.pop())

    queue.push(7)

    console.log(queue.pop())
    console.log(queue.pop())
    console.log(queue.length)
}
