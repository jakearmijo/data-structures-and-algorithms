function ReverseWordsInStringBuiltIn(string) {
  let returnArray = []
  let arrayFromString = string.split(' ')
  for (let i = arrayFromString.length - 1; i >= 0; i--) {
    returnArray.push(arrayFromString[i])
  }
  return returnArray.join(' ')
}

function ReverseWordsInString(string) {
  // TIME =
  // SPACE =
  // 1st find all words that are in string
  // next find all the white spaces
  let words = []
  let startOfWord = 0
  // loop through string and find white spaces to indicate a finished word
  for (let i = 0; i < string.length - 1; i++){
    let char = string[i]
    if (char  === ' ') {
      words.push(string.splice(startOfWord,i))
      startOfWord = i
    } else if (string[startOfWord] === ' ') {
      words.apped(" ")
      startOfWord = i
    }
    words.append(string[startOfWord])
    ReverArray(words)
    return "".join(words)
  }
}

function ReverArray(array) {
  let start = 0
  let end = array.length - 1
  while (start < end) {
    swap(start,end,array)
    start++
    end--
  }
}

function swap(i,j,array) {
  let temp = array[i]
  array[i] = array[j]
  array[j] = temp
}