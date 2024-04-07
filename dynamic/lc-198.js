/* top-down + memo approach
let memo = new Map()
const robHelper = (nums, start) => {
    if(memo.has(start)) {
        return memo.get(start)
    }

    if(nums[start] === undefined) {
        return 0
    }

    const layer = []

    for(let i = start + 2; i < nums.length; i++) {
        const sum = robHelper(nums, i)

        if(!memo.has(i)) {
            memo.set(i, sum)
        }

        layer.push(sum)
    }

    return nums[start] + (layer.length > 0 ? Math.max(...layer) : 0)
}


/**
 * @param {number[]} nums
 * @return {number}
 */
/*
var rob = function(nums) {
    memo = new Map()
    const robs = []

    for(let i = 0; i < nums.length; i++) {
        robs.push(robHelper(nums, i))
    }

    return Math.max(...robs)
};
*/

// bottom-up
/**
 * @param {number[]} nums
 * @return {number}
 */
const rob = (nums) => {
    if(!nums.length) {
        return 0
    }

    let dp1 = 0, dp2 = nums[0], tmp

    for(let i = 1; i < nums.length; i++) {
        tmp = dp1
        dp1 = Math.max(dp1, dp2)
        dp2 = tmp + nums[i]
    }

    return Math.max(dp1, dp2)
}

[
    [1,2,3,1],
    [2,7,9,3,1],
    [2,1,1,2],
    [2],
    []
].forEach(houses => {
    console.log(rob(houses));
})

