/*
 * @lc app=leetcode id=863 lang=javascript
 *
 * [863] All Nodes Distance K in Binary Tree
 */

// @lc code=start
class Node {
  next;
  value;

  constructor(value) {
    this.value = value;
  }
}

class MyQueue {
  _head = null;
  _tail = null;

  length = 0;

  constructor() {}

  push(value) {
    const node = new Node(value);

    if (!this._head) {
      this._head = node;
      this._tail = node;
      this.length++;

      return;
    }

    this._tail.next = node;
    this._tail = this._tail.next;
    this.length++;
  }

  pop() {
    if (!this._head) {
      return null;
    }

    const node = this._head;

    if (this._tail === this._head) {
      this._tail = null;
      this._head = null;
    } else {
      this._head = this._head.next;
    }

    this.length--;

    return node.value;
  }
}

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} target
 * @param {number} k
 * @return {number[]}
 */
var distanceK = function (root, target, k) {
  // traverce all tree and set parent to all nodes
  const queue = new MyQueue();

  queue.push(root);

  let targetNode = null;

  while (queue.length) {
    const node = queue.pop();

    if (node.val === target) {
      targetNode = node;
    }

    if (node.left) {
      node.left.parent = node;
      queue.push(node.left);
    }

    if (node.right) {
      node.right.parent = node;
      queue.push(node.right);
    }
  }

  if (!targetNode) {
    return [];
  }

  console.log(root);

  // BFS to parents and childs

  const queueBFS = new MyQueue();
  const result = [];

  queueBFS.push({ node: targetNode, distance: 0 });

  while (queueBFS.length) {
    const { node, distance } = queueBFS.pop();

    console.log(node.val, distance, k, node.left, node.right, node.parent);

    if (distance === k) {
      result.push(node.val);
    } else {
      if (node.parent) {
        queue.push({ node: node.parent, distance: distance + 1 });
      }

      if (node.left) {
        queue.push({ node: node.left, distance: distance + 1 });
      }

      if (node.right) {
        queue.push({ node: node.right, distance: distance + 1 });
      }
    }
  }

  return result;
};
// @lc code=end

/**

stack/queue
queue: 3 5 1

3 5 1

LL 3 <-> 5 <-> 1 <-> 0 <-> 8

left
right
parent




*/

{
  // const root = [3,5,1,6,2,0,8,null,null,7,4]
  const target = 5;
  const k = 2;
  const root = {
    val: 3,
    left: {
      val: 5,
      left: { val: 6 },
      right: { val: 2, left: { val: 7 }, right: { val: 4 } },
    },
    right: { val: 1, left: { val: 0 }, right: { val: 8 } },
  };

  const expected = [7, 4, 1];
  const result = distanceK(root, target, k);

  console.log(expected === result, result);
  console.log("------------------");
}

{
  const target = 999;
  const k = 2;
  const root = {
    val: 3,
    left: {
      val: 5,
      left: { val: 6 },
      right: { val: 2, left: { val: 7 }, right: { val: 4 } },
    },
    right: { val: 1, left: { val: 0 }, right: { val: 8 } },
  };

  const expected = [];
  const result = distanceK(root, target, k);

  console.log(expected === result, result);
  console.log("------------------");
}
