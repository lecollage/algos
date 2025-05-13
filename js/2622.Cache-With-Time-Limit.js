var TimeLimitedCache = function() {
    this._map = {}
    this._count = 0
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const exists = key in this._map;

    if(exists) {
        clearTimeout(this._map[key].timeout)
    }

    const timeout = setTimeout(() => {
        if(key in this._map) {
            delete this._map[key]
            this._count--
        }
    }, duration)

    this._map[key] = {value: value, timeout: timeout};

    if(!exists) {
        this._count++;
    }

    return exists;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if(key in this._map) {
        return this._map[key].value;
    }

    return -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this._count;
};


const timeLimitedCache = new TimeLimitedCache()

console.log(timeLimitedCache.set(1, 42, 1000)); // false
console.log(timeLimitedCache.get(1)) // 42
console.log(timeLimitedCache.count()) // 1

setTimeout(() => {
    console.log(timeLimitedCache.get(1)) // -1
    console.log(timeLimitedCache.count()) // 0


    console.log(timeLimitedCache.set(1, 50, 1000)); // false
    console.log(timeLimitedCache.set(1, 99, 1000)); // true
    console.log(timeLimitedCache.get(1)) // 99
    console.log(timeLimitedCache.count()) // 1

    setTimeout(() => {
        console.log(timeLimitedCache.get(1)) // -1
        console.log(timeLimitedCache.count()) // 0
    }, 1001)
}, 1001)
