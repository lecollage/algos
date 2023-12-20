let letters

const init = () => {
    letters = new Map()
}

const add = (l) => {
    if(letters.has(l)) {
        letters.set(l, letters.get(l) + 1)
    } else {
        letters.set(l, 1)
    }
}

const remove = (l) => {
    letters.set(l, letters.get(l) - 1)
}

const good = () => {    
    for (let value of letters.values()) {
    	if (value > 1) {
            return false
        }
    }

    return true
}

const lengthOfLongestSubstring = (s) => {
    init()
    let max = 0
    let L = 0
    for(let R = 0; R < s.length; R++) {
        add(s[R])

        while(!good(s[R])) {
            remove(s[L])
            L++
        }

        max = Math.max(max, R - L + 1)
    }

    return max
};



///////


[
    'abcabcbb',
    'bbbbb',
    'pwwkew'
].forEach(w => {
    console.log(
        lengthOfLongestSubstring(w)
    );
})