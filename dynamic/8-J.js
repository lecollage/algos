/**
 * @param {number[][]} mtx
 * @return {number}
 */
var calc = (mtx) => {
    if(!mtx?.length || !mtx[0].length) {
        return 0
    }

    // add paddings
    mtx.unshift(new Array(mtx[0].length).fill(0))

    for(let i = 0; i < mtx.length; i++) {
      mtx[i].unshift(0)
    }

    // calc
    let maxI = 1, maxJ = 1

    for(let i = 1; i < mtx.length; i++) {
      for(let j = 1; j < mtx[0].length; j++) {
        if(mtx[i][j] !== 0){
          mtx[i][j] = Math.min(...[mtx[i-1][j], mtx[i][j-1], mtx[i-1][j-1]]) + 1
        }

        if(mtx[i][j] > mtx[maxI][maxJ]) {
          maxI = i
          maxJ = j
        }
      }
    }
    
    console.log(mtx)

    return mtx[maxI][maxJ]
}


[
  [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1],
  ],
  [
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
  ]
].forEach(mtx => {
    const count = calc(mtx)
    console.log(count);
    console.log();
})
