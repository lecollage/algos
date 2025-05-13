/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    return this.reduce((acc, value) => {
        const key = fn(value)

        if(acc[key]) {
            acc[key].push(value)

            return acc
        }

        acc[key] = [value]

        return acc
    }, {})
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */

console.log([1,2,3].groupBy(String))

console.log([
        {"id":"1"},
        {"id":"1"},
        {"id":"2"}
    ].groupBy((item) => item.id)
)

console.log([
    [1, 2, 3],
    [1, 3, 5],
    [1, 5, 9]
  ].groupBy((i) => String(i[0]))
)
console.log(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].groupBy((i) => String(i > 5))
)
