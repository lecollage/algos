/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let currArgs
    let timeoutId
    let counter = 0

    const execute = () => {
        const currentIteration = counter

        if (currArgs) {
            fn(...currArgs)
        }

        timeoutId = setTimeout(() => {
            if(currentIteration === counter) {
                currArgs = undefined
            } else {
                execute()
            }
        }, t)
    }
    
    return function(...args) {
        currArgs = args
        counter++

        if (!timeoutId) {
            execute()
        }
    }
};


const throttled = throttle(console.log, 1000);
throttled("log"); 
throttled("log"); 
