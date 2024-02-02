const calcHelper = (nums, startFrom, memo) => {
  if(!nums?.length) {
    return 0
  }

  if(memo.has(startFrom)) {
    return memo.get(startFrom)
  }
  
  const lengths = []

  for(let i = startFrom + 1; i < nums.length; i++) {
    if(nums[startFrom] < nums[i]) {
      lengths.push(calcHelper(nums, i, memo))
    }
  }

  // console.log(startFrom, lengths)

  const value = lengths.length ? Math.max(...lengths) + 1 : 1

  memo.set(startFrom, value)

  return value
}

/**
 * @param {number[]} arr
 * @return {string}
 */
const calc = (nums) => {
  if(!nums?.length) {
    return 0
  }

  const lengths = []
  const memo = new Map()

  for(let i = 0; i < nums.length; i++) {
    lengths.push(calcHelper(nums, i, memo))
  }

  return Math.max(...lengths)
}

[
  [3, 29, 5, 5, 28, 6],
  [100, 29, 5, 5, 28, 6],
  [100, 29, 5, 5, 28, 6, 101, 99, 102],
  [5, 4, 3, 2, 1],
  [1, 2, 3, 4, 5],
  [],
  [100],
  [100, 101, 1000, 9],
  [-100, -99, 500, -98, 9],
].forEach(arr => {
    console.log(arr)
    const max = calc(arr)
    console.log(max);
    console.log();
})

/*
0 1 2 3 4 5 6 7 8 9
T H I S I S E A S I

*/