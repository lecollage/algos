/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    if(obstacleGrid.length === 0) {
        return 0
    }

    if(obstacleGrid[0][0] === 1) {
        return 0
    }

    const m = obstacleGrid.length, n = obstacleGrid[0].length

    obstacleGrid[0][0] = 1

    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if((i + j) > 0 && obstacleGrid[i][j] === 1) {
                obstacleGrid[i][j] = 0
            } else {
                const top = i > 0 ? obstacleGrid[i-1][j] : 0
                const left = j > 0 ? obstacleGrid[i][j-1] : 0

                obstacleGrid[i][j] += top + left
            }
        }
    }

    // console.log(obstacleGrid)

    return obstacleGrid[m-1][n-1]
};

[
    [[0,0,0],[0,1,0],[0,0,0]],
    [[0,1],[0,0]],
    [[1,0],[0,0]],
    [],
    [[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]],
].forEach(costs => {
    console.log(uniquePathsWithObstacles(costs));
})


