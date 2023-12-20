const getFibonacci = (n) => {
    let el = 0, elNext = 1

    for(let i = 0; i < n - 1; i++) {
        const buf = el

        el = elNext
        elNext += buf
    }
    
    return elNext
}


[1, 2, 3, 4, 5, 6].forEach(n => {
    console.log(getFibonacci(n));
})



