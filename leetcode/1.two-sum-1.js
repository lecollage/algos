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

        const diff = target - key;
        const diffIndexes = map.get(diff);

        if(!diffIndexes) {
            continue;
        }

        const sameKeyAndDiff = diff === key;

        if(!sameKeyAndDiff) {
            const diffIndex = diffIndexes[0];

            return [diffIndex, i].sort()
        }

        if(diffIndexes.length > 1) {
            const diffIndex = diffIndexes[0] !== i ? diffIndexes[0] : diffIndexes[1];

            return [diffIndex, i].sort();
        }
    }
};
// @lc code=end

console.log(twoSum([1,1,1,2,2], 3))
console.log(twoSum([2,7,11,15], 9))
console.log(twoSum([3,2,4], 6))
console.log(twoSum([3,3], 6))
console.log(twoSum([3,8,4,3], 6))