/**
 * @param {number} n
 * @return {number}
 */
const calc = (n) => {
  if(!n) {
    return 0
  }

  const dp = new Array(n)

  for(let i = 0; i < n; i++) {
    dp[i] = new Array(10).fill(0)
  }

  // init
  for(let i = 1; i < 10; i++) {
    dp[0][i] = 1
  }

  // console.log(dp)

  for(let i = 1; i < n; i++) {
    for(let j = 0; j < 10; j++) {
      const one = dp[i-1][j-1] ?? 0
      const two = dp[i-1][j]
      const three = dp[i-1][j+1] ?? 0

      dp[i][j] = one+two+three
    }
  }

  // console.log(dp)

  let sum = 0
  for(let j = 0; j < 10; j++) {
    sum += dp[dp.length-1][j]
  }

  return sum
}

[
  // 0,
  // 1,
  // 2,
  3
].forEach(n => {
    console.log(n)
    const count = calc(n)
    console.log(count);
    console.log();
})

/*
i-1
i
i+1
*/