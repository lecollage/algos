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
var rob = function(nums) {
    memo = new Map()
    const robs = []

    for(let i = 0; i < nums.length; i++) {
        robs.push(robHelper(nums, i))
    }

    return Math.max(...robs)
};



[
    [1,2,3,1],
    [2,7,9,3,1],
    [2,1,1,2],
].forEach(houses => {
    console.log(rob(houses));
})

