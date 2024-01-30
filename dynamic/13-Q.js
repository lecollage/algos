/**
 * @param {number} N
 * @return {string}
 */
const calc = (str) => {
  if(!str) {
    return 0
  }

  const L = str.length;

  // Arrange
  const dp = new Array(L)

  for(let i = 0; i < L; i++) {
    dp[i] = new Array(L).fill(0)
  }

  // Init
  for(let i = 0; i < L; i++) {
    dp[i][i] = 1
  }

  // Calc
  const diagCnt = L * 2 - 1

  for(let d = 0; d < diagCnt; d++) {
    for(let i = 0, j = d + 1; j < L; i++, j++) {
      const add = str[i] === str[j] ? 2 : 0

      dp[i][j] = Math.max(dp[i+1][j-1] + add, dp[i+1][j], dp[i][j-1])
    }
  }

  dp.forEach(row => console.log(...row))

  const result = []
  let i = 0, j = L - 1
  while (i < j) {
      if (str[i] === str[j]) {
          result.push(str[i])
          console.log(`i,j: `, i,j)
          i += 1
          j -= 1
      } else if (dp[i][j - 1] > dp[i + 1][j]) {
          j -= 1
      } else {
          i += 1
      }
  }

  console.log(`i, j: `, i, j)
  console.log(`result: `, [...result, ...result.reverse()])

  return dp[0][L-1]
}

[
  'HTEOLFEOLEH',
  'ABCDEF',
  'THISISEASI',
  'AAA',
  'AACCA',
  'ABAA',
  'CABAAC1',
  'AA',
  'AAAA',
  '',
].forEach(N => {
    console.log(N)
    const count = calc(N)
    console.log(count);
    console.log();
})

/*
0 1 2 3 4 5 6 7 8 9
T H I S I S E A S I

*/