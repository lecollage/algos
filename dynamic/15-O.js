const calcHelper = (n, i, memo) => {
  if(i < 0 || i > 9) {
    return 0
  }

  if(n === 0) {
    return 1
  }

  const key = `${n}:${i}`

  if(memo.has(key)) {
    console.log(key, memo.get(key))
    return memo.get(key)
  }

  let count = 0

  count += calcHelper(n-1, i-1, memo)
  count += calcHelper(n-1, i, memo)
  count += calcHelper(n-1, i+1, memo)

  memo.set(key, count)

  return count
}

/**
 * @param {number} n
 * @return {number}
 */
const calc = (n) => {
  if(!n) {
    return 0
  }

  let count = 0
  const memo = new Map()

  for(let i = 1; i <= 9; i++) {
    count += calcHelper(n-1, i, memo)
  }

  return count
}

[
  1,
  2,
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