/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const newArr = [...arr];

    for (let i=0; i<newArr.length; i++) {
        newArr[i] = fn(newArr[i], i)
    }

    return newArr;
};


console.log(map([1,2,3], (n) => n + 1))
console.log(map([1,2,3], (n, i) => n + i))


