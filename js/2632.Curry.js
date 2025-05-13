/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    const fnArgs = []

    return function curried(...args) {
        fnArgs.push(...args)

        if(fn.length === fnArgs.length) {
            return fn(...fnArgs)
        }

        return curried 
    }
};


function sum(a, b, c) { 
    console.log('inside sum: ', a, b)
    return a + b + c;
}
const csum = curry(sum);
console.log(csum()()(1,2,3)) // 3


function life() { return 42; }
const clife = curry(life);
console.log(clife()) 
