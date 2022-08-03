

function nextGreaterElement(array) {
  //define result
  const result = new Array(array.length).fill(-1)
  // define stack to use
  const stack = []
  // FOR - loop through array
  for (let i = 0; i < 2 * array.length; i++) {
    // create circularIdx variable to handle the circular array
    let circularIdx = i % array.length
    // WHILE LOOP
    // 1.) check is stack length is greater than 0
    //2.) AND is the value on top of stack is less than the value at the array iteration 
    while (stack.length > 0 && array[stack[stack.length - 1]] < array[circularIdx]) {
      // create top variable to store popped off value
      const top = stack.pop()
      // assign the now popped off element to the result array at the proper idx
      result[top] = array[circularIdx]
    }
    stack.push(circularIdx)
  }
  return result
}