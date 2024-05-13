/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = n
    return function() {
        return count++
    };
};

{
    const counter = createCounter(10)
    console.log(counter())
    console.log(counter())
    console.log(counter())
}
{
    const counter = createCounter(-2)
    console.log(counter())
    console.log(counter())
    console.log(counter())
}