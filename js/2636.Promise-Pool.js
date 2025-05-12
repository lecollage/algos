/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
    if(!functions.length || !n) {
        return new Promise(resolve => {
            resolve([])
        })
    }

    const pool = {}
    const maxPoolSize = functions.length > n ? n : functions.length
    const results = []

    for (let i = 0; i < maxPoolSize; i++) {
        pool[i] = functions.shift()
    }

    // console.log(pool)

    return new Promise(resolve => {
        const subscribe = (i) => {
            pool[i]().then(val => {
                results.push(val)

                if (functions.length) {
                    pool[i] = functions.shift()

                    subscribe(i)
                } else {
                    delete pool[i]

                    if (!Object.keys(pool).length) {
                        resolve(results)
                    }
                }
            })
        }

        for(let i = 0; i < maxPoolSize; i++) {
            subscribe(i)
        }
    })
};

const sleep = (t) => new Promise(res => setTimeout(res, t));

promisePool([
    () => new Promise(res => setTimeout(res, 300)),
    () => new Promise(res => setTimeout(res, 400)),
    () => new Promise(res => setTimeout(res, 200))
], 1)
   .then(console.log)

