/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    id = undefined
    

    return function(...args) {
        clearTimeout(id)

        id = setTimeout(() => {
            fn(...args)
        }, t)
    }
};


const log = debounce(console.log, 100);
log('Hello1'); // cancelled
log('Hello2'); // cancelled
log('Hello3'); // Logged at t=100ms

