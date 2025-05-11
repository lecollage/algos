var areAllResolved = function(dict) {
  for(let i = 0; i < Object.keys(dict).length; i++) {
    if(dict[i].val === undefined) {
      return false
    }
  }

  return true
}

var prepareValidResponse = function(dict) {
  const resolved = []

  for(let i = 0; i < Object.keys(dict).length; i++) {
    const item = dict[i]

    resolved.push(item.val)
  }

  return resolved
}

var prepareInvalidResponse = function(item, val) {
  return {"t": item.diff, "rejected": val}
}

/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
  const dict = {}

  for(let i = 0; i < functions.length; i++) {
    dict[i] = {fn: functions[i]}
  }

  return new Promise((resolve, reject) => {
    for(let i = 0; i < Object.keys(dict).length; i++) {
      const item = dict[i]

      item.fn().then(value => {
        item.val = value

        if (areAllResolved(dict)) {
          resolve(prepareValidResponse(dict))
        }
      }).catch(val => {
        reject(val)
      })
    }
  })
};

{
  const functions = [
    () => new Promise(resolve => setTimeout(() => resolve(4), 50)), 
    () => new Promise(resolve => setTimeout(() => resolve(10), 150)), 
    () => new Promise(resolve => setTimeout(() => resolve(16), 100))
  ]
  const promise = promiseAll(functions)

  promise.then(console.log);
}

{
  const functions = [
    () => new Promise(resolve => setTimeout(() => resolve(1), 200)), 
    () => new Promise((resolve, reject) => setTimeout(() => reject("Error 1"), 100))
  ]
  const promise = promiseAll(functions)

  promise.then(console.log).catch(console.error);
}

{
  const functions = [
    () => new Promise(resolve => setTimeout(() => resolve(5), 200))
  ]
  const promise = promiseAll(functions)

  promise.then(console.log);
}

