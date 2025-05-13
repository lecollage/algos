/*
 * @lc app=leetcode id=1 lang=javascript
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map()

    for(let i = 0; i < nums.length; i++) {
        const key = nums[i];
        const array = map.get(key);

        if(!array) {
            map.set(key, [i])
        } else {
            array.push(i)
            map.set(key, array)
        }
    }
    
    console.log(map);
};
// @lc code=end

twoSum([1,1,1,2,2], 3)