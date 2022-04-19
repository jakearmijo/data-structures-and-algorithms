function insertionSort(array) {
  // lots of swaps and operations in not in correct order
  // all in place
  // TIME = O(n2)
  // SPACE = O(1) -> constant
  for (let i = 0; i < array.length; i++) {
    let j = i
    while (j > 0 && array[j] < array[j-1]) {
      swap(i,j-1,array)
      j--
    }
  }
  return array
}

function swap(i,j,array) {
  let temp = array[i]
  array[i] = array[j]
  array[j] = temp
}