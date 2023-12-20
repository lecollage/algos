/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} threshold
 * @return {number}
 */
var numOfSubarrays = function(arr, k, threshold) {
    if(arr.length < k) {
        return 0
    }

    let sum = 0
    let count = 0
    let L = 0;

    for(let R = 0; R < arr.length; R++) {
        sum += arr[R]

        while(R - L + 1 > k) {
            sum -= arr[L]
            L++
        }

        if(R - L + 1 === k && sum/k >= threshold){
            count++
        }
    }

    return count
};


[
    {arr: [2,2,2,2,5,5,5,8], k: 2, threshold: 4},
    {arr: [11,13,17,23,29,31,7,5,2,3], k: 3, threshold: 5},
    {arr: [11,13,17], k: 3, threshold: 5},
    {arr: [11,13,17,23], k: 3, threshold: 5},
    {arr: [11,13,17], k: 4, threshold: 5},
].forEach(({arr, k, threshold}) => {
    console.log(
        numOfSubarrays(arr, k, threshold)
    );
})