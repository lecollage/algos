// Approach 1: simple answer - true/false
const calc = (target, arr, sum, i) => {
    if(sum === target) {
        return true
    }

    if (i >= arr.length) {
        return false
    }

    return calc(target, arr, sum + arr[i+1], i+1) || calc(target, arr, sum - arr[i+1], i+1)
};


// Approach 2: answer - true/false + path >> 
const calcPathHelper = (target, arr, sum, i) => {
    if (sum === target) {
        return [true, '']
    }

    if (i >= arr.length) {
        return [false, '']
    }

    const [plusAnswer, plusPath] = calcPathHelper(target, arr, sum + arr[i+1], i+1, '+')
    const [minusAnswer, minusPath] = calcPathHelper(target, arr, sum - arr[i+1], i+1, '-')
    const path = plusAnswer ? `+${arr[i+1]}${plusPath}` : `-${arr[i+1]}${minusPath}`

    return [plusAnswer || minusAnswer, path]
};

const calcPath = (target, arr) => {
    const [answer, path] = calcPathHelper(target, arr, arr[0], 0)

    return [answer, answer ? `${arr[0]}${path}` : '']
};
// << answer - true/false + path

// Approach 3: iterative with the array of arrays
const calcIterative = (target, arr) => {
    if(!arr.length) {
        return false
    }

    const dp = new Array(arr.length)
    
    dp[0] = new Array(1)

    dp[0][0] = arr[0]

    for(let i = 1; i < arr.length; i++) {
        const prevArr = dp[i - 1]

        dp[i] = new Array(prevArr.length * 2)

        for(let j = 0; j < dp[i].length; j++) {
            const multiplier = j % 2 === 0 ? 1 : -1

            dp[i][j] = dp[i-1][Math.floor(j/2)] + multiplier * arr[i]
        }
    }

    // console.log(dp)

    return dp[dp.length - 1].includes(target)
}

[
    {
        target: 13,
        arr: [9,3,7]
    },
    {
        target: 50,
        arr: [9,3,7]
    }
].forEach(({target, arr}) => {
    console.log(calcIterative(target, arr));
})
