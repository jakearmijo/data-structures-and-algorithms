function getPermutations(array) {
  let permutations = []
  permutationsHelper(0, array, permutations)
  return permutations
}

function permutationsHelper(index, array,permutations) {
  if (index === array.length -1 ) {
    permutations.push(array.slice())
  } else {
    for (let j = index; j < array.length; j++) {
      swap(index,j,array)
      permutationsHelper(index + 1, array, permutations)
      swap(index,j,array)
    }
  }
}

function swap(i,j,array) {
  let temp = array[i]
  array[i] = array[j]
  array[j] = temp
}