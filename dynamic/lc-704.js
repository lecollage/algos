/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if(nums.length === 0) {
        return -1
    }

    let left = 0, right = nums.length

    while(left + 1 < right) {
        const middle = Math.floor((left + right) / 2)

        if(nums[middle] <= target) {
            left = middle
        } else {
            right = middle
        }
    }

    return nums[left] === target ? left : -1
};

[
    {
        arr: [-1,0,3,5,9,12],
        target: 9
    },
    {
        arr: [-1,0,3,5,9,12],
        target: 2
    },
    {
        arr: [-1,0,3,5,9,12],
        target: -9
    },
    {
        arr: [-1,0,3,5,9,12],
        target: 15
    },
    {
        arr: [-1,0,3,5,9,12],
        target: -1
    },
    {
        arr: [-1,0,3,5,9,12],
        target: 12
    },
    {
        arr: [-1],
        target: -1
    },
].forEach(({arr, target}) => {
    console.log(search(arr, target));
})


