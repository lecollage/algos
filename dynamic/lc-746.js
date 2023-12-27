/*
var minCostClimbingStairs = function(costs) {
    if(costs.length === 0) {
        return 0
    }

    if(costs.length === 1) {
        return costs[0]
    }

    costs.push(0)

    let i = costs.length - 3

    // console.log(i)

    for(let i = costs.length - 3; i >= 0; i--) {
        costs[i] = Math.min(costs[i + 1], costs[i + 2]) + costs[i]
    }
    
    // console.log(costs)

    return Math.min(costs[0], costs[1]);
};
*/

var minCostClimbingStairs = function(costs) {
    const dp = new Array(costs.length)

    dp[0] = costs[0]
    dp[1] = costs[1]

    for(let i = 2; i < dp.length; i++) {
        dp[i] = Math.min(dp[i - 1], dp[i - 2]) + costs[i]
    }

    return Math.min(dp[dp.length - 2], dp[dp.length - 1])
};


[
    [10,15,20],
    [1,100,1,1,1,100,1,1,100,1],
    [100, 100, 2, 2, 1 ,0],
].forEach(costs => {
    console.log(minCostClimbingStairs(costs));
})



/*
10,15,20,0
10,15,20,15
100, 100, 2, 2, 1 ,0
100, 100, 2, 2, 1 ,0
100, 100, 3, 2, 1 ,0
100, 102, 3, 2, 1 ,0
103, 102, 3, 2, 1 ,0
*/
