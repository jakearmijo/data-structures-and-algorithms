class HashTable {
  constructor(size=53) {
    this.keyMap = new Array(size)
  }

  _hash(key) {
    let total = 0
    let WEIRD_PRIME = 31
    for (let i = 0; i < Math.min(key.length, 100); i++) {
      let char = key[i]
      let value = char.charCodeAt(0) - 96
      total = (total * WEIRD_PRIME + value) % this.keyMap.length
    }
    return total
  }

  set(key,value) {
    // accepts a key and a value
    // hashes the key
    let hashedKey = this._hash(key)
    // stores the key-value pair in the hash table array via separate chaining
    for (let i = 0; i < this.keyMap.length - 1; i++) {
      if (!this.keyMap[i]) {
        this.keyMap[i] = []
      }
      this.keyMap.push([key,value])
    }
  }

  get(key) {
    // hash the key
    let index = this._hash(key)
    // if key index exists
    if (this.keyMap[index]) {
      // loop over the nested array and grab the wanted value
      for (let i = 0; i < this.keyMap[index].length; i++) {
        if (this.keyMap[index][i][0] === key) {
          return this.keyMap[index][i][1]
        }
      }
    }
    return undefined
  }

  keys() {

  } 

  values() {
    let valuesArr = []
    for (let i = 0; i < this.keyMap.length; i++) {
      if (this.keyMap[i]) {
        for(let j = 0; j < this.keyMap[i]; j++) {
          if (!valuesArr.includes(this.keyMap[i][j][1])) {
              valuesArr.push(this.keyMap[i][j][1])
          }
        }
      }
    }
    return valuesArr
  }
}