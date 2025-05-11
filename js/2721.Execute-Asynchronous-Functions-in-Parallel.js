var areAllResolved = function(dict) {
  for(let i = 0; i < Object.keys(dict).length; i++) {
    if(dict[i].val === undefined) {
      return false
    }
  }

  return true
}

var prepareValidResponse = function(dict) {
  const response =  {"t": 0, "resolved": []}

  for(let i = 0; i < Object.keys(dict).length; i++) {
    const item = dict[i]

    if (item.diff > response["t"]) {
      response["t"] = item.diff
    }

    response["resolved"].push(item.val)
  }

  return response
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

      item.startDate = performance.now()

      item.fn().then(value => {
        item.val = value
        item.finishDate = performance.now()
        item.diff = Math.round(item.finishDate - item.startDate)

        if (areAllResolved(dict)) {
          resolve(prepareValidResponse(dict))
        }
      }).catch(val => {
        item.finishDate = performance.now()
        item.diff = Math.round(item.finishDate - item.startDate)

        resolve(prepareInvalidResponse(item, val))
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
    () => new Promise((resolve, reject) => setTimeout(() => reject("Error"), 100))
  ]
  const promise = promiseAll(functions)

  promise.then(console.log);
}

{
  const functions = [
    () => new Promise(resolve => setTimeout(() => resolve(5), 200))
  ]
  const promise = promiseAll(functions)

  promise.then(console.log);
}

