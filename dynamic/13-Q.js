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
      if (str[i] === str[j]) {
        dp[i][j] = dp[i+1][j-1] + 2
      } else {
        dp[i][j] = Math.max(dp[i][j-1], dp[i+1][j])
      }
    }
  }

  dp.forEach(row => console.log(...row))

  const result = []
  let i = 0, j = L - 1
  while (i < j) {
      if (str[i] === str[j]) {
          result.push(str[i])
          // console.log(`i,j: `, i,j)
          i += 1
          j -= 1
      } else if (dp[i][j - 1] > dp[i + 1][j]) {
          j -= 1
      } else {
          i += 1
      }
  }

  // console.log(`i, j: `, i, j)
  const resStr = [...result, i === j ? str[i] : '', ...result.reverse()]
  console.log(resStr)

  return [dp[0][L-1], resStr.join('')]
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

THISISEASI

ISISEASI


HTEOLFEOLEH
1 1 1 1 1 1 3 3 3 5 7
0 1 1 1 1 1 3 3 3 5 5
0 0 1 1 1 1 3 3 3 5 5
0 0 0 1 1 1 1 3 3 3 3
0 0 0 0 1 1 1 1 3 3 3
0 0 0 0 0 1 1 1 1 3 3
0 0 0 0 0 0 1 1 1 3 3
0 0 0 0 0 0 0 1 1 1 1
0 0 0 0 0 0 0 0 1 1 1
0 0 0 0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0 0 0 1

*/