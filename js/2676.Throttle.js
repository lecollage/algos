/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let counter = 0
    let latestArgs
    let firstTime = true

    const repeat = () => {
        const iteration = counter

        setTimeout(() => {
            // console.log("inside repeat >> ", latestArgs, iteration , counter)

            if(latestArgs) {
                fn(...latestArgs)
                repeat()
            }

            if(iteration == counter) {
                latestArgs = undefined
            }
        }, firstTime ? 0 : t)
    }
    
    return function(...args) {
        latestArgs = args
        counter++

        if(firstTime) {
            repeat()
        }

        firstTime = false
    }
};


const throttled = throttle(console.log, 1000);
throttled("log"); // logged immediately.
