/**
 * @param {number[]} arr
 * @return {string}
 */
const calc = (nums) => {
  if(!nums?.length) {
    return 0
  }

  const L = nums.length
  const dp = new Array(L)

  for(let i = 0; i < L; i++) {
    for(let j = 0; j < i; j++) {
      if(nums[j] < nums[i]) {
        back.push(dp[j])
      }
    }

    dp[i] = back.length > 0 ? Math.max(...back) + 1 : 1
  }

  console.log(dp)

  return Math.max(...dp)
}

[
  [3, 29, 5, 5, 28, 6],
  [100, 29, 5, 5, 28, 6],
  [100, 29, 5, 5, 28, 6, 101, 99, 102, -1],
  [5, 4, 3, 2, 1],
  [1, 2, 3, 4, 5],
  [],
  [100],
  [100, 101, 1000, 9],
  [-100, -99, 500, -98, 9],
  [10, 11, 12, -100, -99, 500, -98, 9, 20, 30, 40, 1, 2, 3],
].forEach(arr => {
    console.log(arr)
    const max = calc(arr)
    console.log(max);
    console.log();
})
