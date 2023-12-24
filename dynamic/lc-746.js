var minCostClimbingStairs = function(costs) {
    if(costs.length === 0) {
        return 0
    }

    if(costs.length === 1) {
        return costs[0]
    }

    costs = [...costs, 0];

    let i = costs.length - 3

    // console.log(i)

    for(let i = costs.length - 3; i >= 0; i--) {
        costs[i] = Math.min(costs[i + 1], costs[i + 2]) + costs[i]
        console.log(Math.min(costs[i + 1], costs[i + 2]) + costs[i])
    }
    
    // console.log(costs)

    return Math.min(costs[0], costs[1]);
};

[
    [10,15,20],
    [1,100,1,1,1,100,1,1,100,1],
].forEach(costs => {
    console.log(minCostClimbingStairs(costs));
})



