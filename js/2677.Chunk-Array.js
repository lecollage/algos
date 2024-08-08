/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const chunkedArr = []
    let chunk = []

    for(let i = 0; i < arr.length; i++) {
        chunk.push(arr[i]);

        if(chunk.length === size) {
            chunkedArr.push(chunk)
            chunk = []
        }
    }

    if(chunk.length > 0) {
        chunkedArr.push(chunk)
    }

    return chunkedArr;
};


console.log(chunk([1,2,3,4,5], 1))
console.log(chunk([1,2,3,4,5], 2))
console.log(chunk([1,2,3,4,5], 3))
console.log(chunk([1,2,3,4,5], 4))
console.log(chunk([1,2,3,4,5], 5))
console.log(chunk([1,2,3,4,5], 6))

console.log(chunk([1,9,6,3,2], 3))
console.log(chunk([8,5,3,2,6], 6))

console.log(chunk([], 1))