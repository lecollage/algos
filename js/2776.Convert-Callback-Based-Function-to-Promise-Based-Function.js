/**
 * @param {Function} fn
 * @return {Function<Promise<number>>}
 */
var promisify = function(fn) {
    return async function(...args) {
        return new Promise((resolve, reject) => {
            console.log(fn.length)

            const myCallback = (...callbackArgs) => {
                // console.log('inside callback', callbackArgs.length , args.length)

                if(callbackArgs.length === 1) {
                    resolve(...callbackArgs)
                } else {
                    const [_, ...errors] = callbackArgs
                    reject(...errors)
                }
            }
            const newArgs = [myCallback, ...args]

            console.log(fn(...newArgs))
        })
    }
};

// Test function 1: resolves
function testFn1(callback, a, b, c) {
    console.log(callback, a, b, c)
    callback(a * b * c);
}

// Test function 2: rejects
function testFn2(callback, a, b, c) {
  callback(a * b * c, "Promise Rejected");
}

(async () => {
  const asyncFunc1 = promisify(testFn1);
  const asyncFunc2 = promisify(testFn2);

  try {
    const result1 = await asyncFunc1(1, 2, 3);
    console.log(result1 === 6 ? '✅ Test 1 passed' : '❌ Test 1 failed', result1);
  } catch (e) {
    console.log('❌ Test 1 threw an error:', e);
  }

  try {
    await asyncFunc2(4, 5, 6);
    console.log('❌ Test 2 did not reject as expected');
  } catch (e) {
    console.log(e === "Promise Rejected" ? '✅ Test 2 passed' : '❌ Test 2 failed', e);
  }
})();