/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort()

    const map = new Map()

    nums.forEach(n => {
        if(map.has(n)) {
            map.set(n, map.get(n) + 1)
        } else {
            map.set(n, 1)
        }
    })

    const tuples = []
    
    nums.forEach((n, index) => {
        map.set(n, map.get(n) - 1)

        if(map.has(n) === 0) {
            map.delete(n)
        }

        for(let i = index + 1; i < nums.length; i++) {
            let sum = n + nums[i]

            if (sum < 0) {
                const compensate = -1 * sum

                if(map.has(compensate)) {
                    tuples.push([n, nums[i], compensate])
                }
            } else if (sum === 0) {
                if(map.has(0)) {
                    tuples.push([n, nums[i], 0])
                }
            } else {
                const compensate = -1 * sum
                if(map.has(compensate)) {
                    tuples.push([n, nums[i], compensate])
                }
            }
        }
    })

    return tuples
};

[
    {arr1: [-1,0,1,2,-1,-4]},
    {arr1: [0,1,1]},
    {arr1: [0,0,0]},
].forEach(({arr1}) => {
    console.log(
        threeSum(arr1)
    );
})

/*
Example 1:
Input: nums = [-1,0,1,2,-1,-4]

[-4,-1,-1,0,1,2]

p1, p2, p3

-4 -1 -1
-4 -1 0 

Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = [0,1,1]

Input: nums = [0,0,0]
Output: [[0,0,0]]


*/