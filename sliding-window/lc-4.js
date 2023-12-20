let letters 

const init = () => {
    letters = new Map()
}

const add = (x) => {
    if(letters.has(x)) {
        letters.set(x, letters.get(x) + 1)
    } else {
        letters.set(x, 1)
    }
}

const remove = (x) => {
    letters.set(x, letters.get(x) - 1)
}

const getMostFrequentLetter = () => {
    let max = 0

    for (let [key, value] of letters) {
        if(value > max) {
            max = value
        }
    }

    return max
}

const good = (k, windowLength) => {
    const mostFreq = getMostFrequentLetter()

    return windowLength - mostFreq <= k
}

const characterReplacement = (s, k) => {
    init()
    let max = 0
    let L = 0
    
    for(let R = 0; R < s.length; R++) {
        add(s[R])

        let windowLength = R - L + 1

        while(!good(k, windowLength)) {
            remove(s[L])
            L++
            windowLength = R - L + 1
        }

        max = Math.max(max, windowLength)
    }

    return max
};


[
    {s: "ABAB", k: 2},
    {s: "AABABBA", k: 1},
    {s: "A", k: 1},
    {s: "", k: 1},
].forEach(({s, k}) => {
    console.log(
        characterReplacement(s, k)
    );
})