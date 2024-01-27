/**
 * @param {number} N
 * @return {string}
 */
const calc = (N) => {
  if(N === 0) {
    return 0
  }

  if(N === 1) {
    return 8
  }

  // Arrange
  const dp = new Array(N)

  for(let i = 0; i < N; i++) {
    dp[i] = new Array(10).fill(0)
  }

  // Init
  dp[0][0] = 0
  dp[0][1] = 1
  dp[0][2] = 1
  dp[0][3] = 1
  dp[0][4] = 1
  dp[0][5] = 0
  dp[0][6] = 1
  dp[0][7] = 1
  dp[0][8] = 0
  dp[0][9] = 1

  const allIndexes = [
    [4,6],
    [6,8],
    [7,9],
    [4,8],
    [0,3,9],
    [],
    [0,1,7],
    [2,6],
    [1,3],
    [2,4],
  ]

  // calc
  for(let i = 1; i < N; i++) {
    const line = dp[i-1]

    for(let j = 0; j < allIndexes.length; j++) {
      const indexes = allIndexes[j]

      for(let k = 0; k < indexes.length; k++) {
        const index = indexes[k]

        dp[i][j] += line[index]
      }
    }
  }

  let sum = 0

  for(let i = 0; i < 10; i++) {
    sum += dp[dp.length - 1][i]
  }

  return sum
}

[
  0,
  1,
  10,
].forEach(N => {
    console.log(N)
    const count = calc(N)
    console.log(count);
    console.log();
})
