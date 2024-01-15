/**
 * @param {number[]} dp
 * @return {number}
 */
const calc = (arr) => {
    if(!arr?.length) {
        return 0
    }

    const dp = new Array(arr.length)

    for(let i = 0; i < arr.length; i++) {
      dp[i] = [0, 0]
    }


    // init
    dp[0][0] = 0
    dp[0][1] = 0

    // calc
    for(let i = 1; i < arr.length; i++) {
      dp[i][0] = dp[i-1][1]
      dp[i][1] = Math.min(dp[i-1][0], dp[i-1][1]) + (arr[i] - arr[i-1]) + dp[i-1][0]
    }
    
    console.log(dp)

    return Math.min(dp[dp.length - 1][0], dp[dp.length - 1][1])
}


/*
6
3 4 6 12 13 14
*/

[
  [
    3, 4, 6, 12, 13, 14
  ],
].forEach(arr => {
    const count = calc(arr)
    console.log(count);
    console.log();
})
