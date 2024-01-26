/**
 * @param {number[][]} arr
 * @return {number}
 */
const calc = (arr) => {
    if(!arr?.length) {
        return 0
    }

    // Arrange
    const dp = new Array(arr.length)

    for(let i = 0; i < arr.length; i++) {
      dp[i] = [0, 0]
    }

    // Init
    dp[0][0] = 0
    dp[0][1] = arr[0][0]

    if(arr.length === 1) {
      return dp[0][1]
    }

    dp[1][0] = dp[0][1]
    dp[1][1] = Math.min(arr[1][0] + dp[0][1], arr[0][1])

    if(arr.length === 2) {
      return dp[1][1] 
    }

    dp[2][0] = dp[1][1]
    dp[2][1] = Math.min(arr[2][0] + dp[1][1], arr[1][1] + dp[0][1], arr[0][2])

    // console.log(dp)

    // Calc
    for(let i = 3; i < arr.length; i++) {
      dp[i][0] = dp[i-1][1]

      const A = arr[i][0], B = arr[i-1][1], C = arr[i-2][2]

      dp[i][1] = Math.min(dp[i-1][1] + A, dp[i-2][1] + B, dp[i-3][1] + C)
    }

    return dp[dp.length - 1][1]
}


/*
5
5  10 15
2  10 15
5  5  5
20 20 1
20 1  1

5
10 15 5
10 15 2
5  5  1
20 20 1
20 1 1
*/

[
  [
    [5, 10, 15],
    [2, 10, 15],
    [5, 5, 5],
    [20, 20, 1],
    [20, 1, 1],
  ]
].forEach(arr => {
    const count = calc(arr)
    console.log(count);
    console.log();
})
