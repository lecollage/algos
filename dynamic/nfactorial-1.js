const calc = (target, arr, sum, i) => {
    if(sum === target) {
        return true
    }

    if (i >= arr.length) {
        return false
    }

    return calc(target, arr, sum + arr[i+1], i+1) || calc(target, arr, sum - arr[i+1], i+1)
};


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
    console.log(calcPath(target, arr));
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
