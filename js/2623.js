/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map()

    return function(...args) {
        const key = JSON.stringify(args)

        // console.log('key', key)

        if(cache.has(key)) {
            // console.log('return from cache')

            return cache.get(key);
        }

        // console.log('execute a function')

        const res = fn(...args);

        cache.set(key, res);

        return res;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */

//  let callCount = 0;

//  const memoizedFn = memoize(function (a, b) {
//   callCount += 1;
//    return a + b;
//  })

//  console.log(memoizedFn(2, 3)) // 5
//  console.log(memoizedFn(2, 3)) // 5
//  console.log(memoizedFn(3, 2)) // 5
//  console.log(memoizedFn(2, 2)) // 4
//  console.log(memoizedFn(2, 2)) // 4
//  memoizedFn(2, 3) // 5
//  console.log(callCount) // 1 



const factorial = (n) => (n <= 1) ? 1 : (n * factorial(n - 1));
const memoFactorial = memoize(factorial);
console.log(memoFactorial(2)); // "call" - returns 2.
console.log(memoFactorial(3)); // "call" - returns 6.
console.log(memoFactorial(2)); // "call" - returns 2. However factorial was not called because 2 was seen before.