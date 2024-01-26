/**
 * @param {number} N
 * @return {string}
 */
const calc = (N) => {
  if(N === 0) {
    return ''
  }

  const steps = new Array(N+1).fill(0)

  for(let i = 2; i < N+1; i++) {
    steps[i] = Math.min(steps[i-1], i%2===0 ? steps[i/2] : N, i%3===0 ? steps[i/3] : N) + 1
  }

  let i = N
  const operations = []

  while(i > 1) {
    if(steps[i] === steps[i-1]+1) {
      operations.push('+1')
      i--
    } else if(i%2 === 0 && steps[i]===steps[i/2]+1) {
      operations.push('*2')
      i /= 2
    } else if(i%3 === 0 && steps[i]===steps[i/3]+1) {
      operations.push('*3')
      i /= 3
    }
  }

  operations.push('1')

  // console.log(dp)
  console.log(operations.reverse().join(''))

  return steps[N]
}

[
  10,
  3,
  5,
  32718,
  562340
].forEach(N => {
    console.log(N)
    const count = calc(N)
    console.log(count);
    console.log();
})
