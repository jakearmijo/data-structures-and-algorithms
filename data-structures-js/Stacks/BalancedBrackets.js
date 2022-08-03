function BalancedBrackets() {
  // Time = O(n)
  // Space = O(n)
  // string of all open brackets
  let openBrackets = '[{('
  // string of all closed brackets
  let closedBrackets = ']})'
  // map the closing brackets to the open brackets
  let matchingClosingBrackets = {
    ')': '(',
    '}': '{',
    ']': '['
  }
// define stack
  const stack = []
// FOR OF - loop through string and check character 
  for (const char of string) {
    // if the open bracket string includes this value -> push it into the stack
    if (openBrackets.includes(char)) {
      stack.push(char)
      // else if the closed bracket string includes this value
      // IF stack length is 0 return false cause its not balances
    } else if (closedBrackets.includes(char)) {
      if (stack.length === 0) {
        return false
      }
      // if the last value added into the stack  matches in the dic
      // pop it off
      // if it doesnt return false -> not balanced
      if (stack[stack.length - 1] === matchingClosingBrackets[char]){
        stack.pop()
      } else {
        return false
      }
    }
  }
  // this will return true if it is true and false if its false
  return stack.length === 0
}