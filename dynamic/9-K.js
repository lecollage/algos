/**
 * @param {number[]} dp
 * @return {number}
 */
const calc = (arr) => {
    if(!arr?.length) {
        return 0
    }

    if(arr.length === 1) {
      return 0
    }

    if(arr.length === 2) {
      return arr[1] - arr[0]
    }

    // Arrange
    const dp = new Array(arr.length)

    for(let i = 0; i < arr.length; i++) {
      dp[i] = [0, 0]
    }

    // init
    dp[0][0] = 0
    dp[0][1] = 0

    dp[1][0] = 0
    dp[1][1] = arr[1] - arr[0]

    dp[2][0] = dp[1][1]
    dp[2][1] = dp[1][1] + (arr[2] - arr[1])

    // calc
    for(let i = 3; i < arr.length; i++) {
      dp[i][0] = dp[i-1][1]
      dp[i][1] = Math.min(dp[i-1][0], dp[i-1][1]) + (arr[i] - arr[i-1])

      // console.log(i, dp)
    }
    
    return dp[dp.length - 1][1]
}


/*
6
3 4 6 12 13 14
*/

[
  [3, 4, 6, 12, 13, 14], // 5
  [3, 6, 7, 15, 16],     // 5
  [],                    // 0
  [1],                   // 0
  [1,5],                 // 4
  [1,5,20],              // 19
  [1,5,8,9],             // 5
  [0, 5, 10, 15],        // 10
  [0, 5, 10, 15, 20],    // 15
].forEach(arr => {
    const count = calc(arr)
    console.log(count);
    console.log();
})
