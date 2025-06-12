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

/*
 * @lc app=leetcode id=542 lang=javascript
 *
 * [542] 01 Matrix
 */

// @lc code=start
/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function (mat) {
  const visited = []

  for (let i = 0; i < mat.length; i++) {
    visited.push(new Array(mat[i].length).fill(false))
  }

  const zeros = []

  for (let i = 0; i < mat.length; i++) {
    for (let j = 0; j < mat[i].length; j++) {
      if (mat[i][j] === 0) {
        zeros.push([i, j])
        visited[i][j] = true
      }
    }
  }

  const explore = (zeros) => {
    const queue = new MyQueue();

    for (let k = 0; k < zeros.length; k++) {
      const [i,j] = zeros[k];

      queue.push({ i, j, distance: 0 });
    }

    const directions = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ];
    const isValid = (i, j) => {
      if (i < 0 || i >= mat.length) {
        return false;
      }

      if (j < 0 || j >= mat[i].length) {
        return false;
      }

      return true;
    };

    while (queue.length) {
      const { i, j, distance } = queue.pop();

      //   console.log(i, j);

      for (let k = 0; k < directions.length; k++) {
        const [di, dj] = directions[k];

        const newI = i + di;
        const newJ = j + dj;

        if (isValid(newI, newJ) && !visited[newI][newJ]) {
          if (mat[newI][newJ] === 1) {
            mat[newI][newJ] = distance + 1;
          }

          queue.push({ i: newI, j: newJ, distance: distance + 1 });
          visited[newI][newJ] = true
        }
      }
    }
  };

  
  explore(zeros)

  return mat;
};
// @lc code=end

{
  const matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
  ];

  const expected = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
  ];

  const answer = updateMatrix(matrix);

  console.log(answer === expected, answer);
}

{
  const matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
  ];

  const expected = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 2, 1],
  ];

  const answer = updateMatrix(matrix);

  console.log(answer === expected, answer);
}

{
  const matrix = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
  ];

  const expected = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 2, 1, 2],
    [2, 3, 2, 3],
  ];

  const answer = updateMatrix(matrix);

  console.log(answer === expected, answer);
}

{
  const matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
  ];

  const expected = [
    [0, 1, 2, 3],
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
  ];

  const answer = updateMatrix(matrix);

  console.log(answer === expected, answer);
}
