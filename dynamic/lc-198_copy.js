const nums = [1,2,3,1], start = 2, layer = []

console.log(nums[start], layer.length > 0 ? Math.max(...layer) : 0)
console.log(nums[start] + (layer.length > 0 ? Math.max(...layer) : 0))