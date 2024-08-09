/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if (Array.isArray(obj)){
        return !obj.length;
    }

    return !Object.keys(obj).length;
};

console.log(isEmpty([]))
console.log(isEmpty([1,2]))

console.log(isEmpty({}))
console.log(isEmpty({x: 1}))