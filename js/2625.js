/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let value = init

    return {
        increment: function () {
            value++;
            return value;
        },
        decrement: function () {
            value--;
            return value;
        },
        reset: function () {
            value = init;
            return value;
        }
    }
};

const counter = createCounter(5)
console.log(counter.increment()); // 6
console.log(counter.reset()); // 5
console.log(counter.decrement()); // 4

