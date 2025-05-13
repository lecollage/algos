var TimeLimitedCache = function() {
    this.keyPairs = {}
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let isValueExist = false

    if (this.keyPairs[key]) {
        clearTimeout(this.keyPairs[key].timeoutRef)
        isValueExist = true
    }

    const timeoutRef = setTimeout(() => {
        delete this.keyPairs[key]
    }, duration);

    this.keyPairs[key] = {
        value,
        duration,
        timeoutRef
    }

    return isValueExist
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return this.keyPairs[key] ? this.keyPairs[key].value : -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    // console.log(Object.keys(this.keyPairs))
    return Object.keys(this.keyPairs).length
};


const timeLimitedCache = new TimeLimitedCache();
console.log(timeLimitedCache.set(1, 42, 1000)); // false
console.log(timeLimitedCache.get(1)); // 42

console.log(timeLimitedCache.set(1, 42, 2000)); // true
console.log(timeLimitedCache.get(1)); // 42

console.log(timeLimitedCache.count()); // 1

setTimeout(() => {
    console.log(timeLimitedCache.count()); // 0
}, 3000)