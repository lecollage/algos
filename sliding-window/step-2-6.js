    process.stdin.resume();
    process.stdin.setEncoding("utf-8");

    let inputArray = [];
    let inputString = "";
    let currentLine = 0;

    process.stdin.on("data", (inputStdin) => {
        inputArray.push(inputStdin)
    });

    process.stdin.on("end", (_) => {
        inputString = inputArray.join('')
        inputString = inputString
            .trim()
            .split("\n")
            .map((string) => {
                return string.trim();
            });

        main();
    });

    function readline() {
        return inputString[currentLine++];
    }



    /////////////////


    const Stack = () => {
        const s = [], smin = [], smax = []

        return {
            push: (x) => {
                s.push(x)
                smin.push(smin.length === 0 ? x : Math.min(smin[smin.length - 1], x))
                smax.push(smax.length === 0 ? x : Math.max(smax[smax.length - 1], x))
            },
            pop: () => {
                smin.pop()
                smax.pop()

                return s.pop()
            },
            min: () => {
                return smin.length === 0 ? +Infinity : smin[smin.length - 1]
            },
            max: () => {
                return smax.length === 0 ? -Infinity : smax[smax.length - 1]
            },
            empty: () => {
                return s.length === 0
            }
        }
    }

    const s1 = Stack()
    const s2 = Stack()


    const add = (x) => {
        s2.push(x)
    }

    const remove = (x) => {
        if(s1.empty()) {
            while(!s2.empty()) {
                s1.push(s2.pop())
            }
        }

        s1.pop()
    }

    const good = (k) => {
        const max = Math.max(s1.max(), s2.max())
        const min = Math.min(s1.min(), s2.min())

        return max - min <= k
    }

    function main() {
        const [n, k] = readline().split(' ').map(Number)
        const arr = readline().split(' ').map(Number)
        let L = 0
        let count = 0
    
        for(let R = 0; R < n; R++) {
            add(arr[R])
            
            while (!good(k)) {
                remove()
                L++
            }

            // console.log(L, R, count)
    
            count += R - L + 1
        }
        
        console.log(count)
    }

    /*

    7 3
    2 6 4 3 6 8 9

    */
