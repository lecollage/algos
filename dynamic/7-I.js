/**
 * @param {number} N
 * @return {number}
 */
var calc = function(N) {
    if(N === 0) {
        return 0
    }

    // prepare the matrix (N+3 x M+3) with paddings contain zero 
    const mtx = new Array(N)

    for(let i = 0; i < N; i++) {
      mtx[i] = new Array(N).fill(0)
    }

    // init
    for(let i = 0, j = 0; i < N; i++, j++) {
      mtx[i][j] = 1
    }

    // calc
    for(let i = 0; i < N; i++) {
      for(let j = 0; j < i; j++) {
        for(let k = 0; k < j; k++) {
          mtx[i][j] += mtx[i-j-1][k]
        }
      }
    }

    // output
    // console.log(mtx)

    let sum = 0

    for(let i = 0; i < N; i++) {
      sum += mtx[N - 1][i]
    }

    return sum
};


[
    3,
    4,
    5,
    150
].forEach(N => {
    const count = calc(N)
    console.log(count);
    console.log();
})

/*
[
  [
    1, 0, 0, 0, 0, 0, 
    0, 1, 0, 0, 0, 0, 
    0, 0, 1, 0, 0, 0, 
    0, 0, 0, 1, 0, 0, 
    0, 0, 0, 0, 1, 0, 
    0, 0, 0, 0, 0, 1, 
  ]
]
*/