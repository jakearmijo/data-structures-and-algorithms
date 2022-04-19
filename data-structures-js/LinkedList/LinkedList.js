
class LinkedList {
  // Single Linked List only has next attribute
  constructor(value) {
    this.value = value
    this.head = null
  }
}

function removeDuplicateFromLinkedList(linkedList) {
  // input list is sort in asending order -> all dupes will be grouped together
  // if not sorted. make a set and store the values we have seen.
  // to "delete" you change pointer to point at next value
  // Time = O(n) | Space = O(n)
  let currentNode = linkedList
  while (currentNode !== null) {
    // create variable to find the next distinct (unique) node
    let nextDistictNode = currentNode.next
    // while loop - while the next distict node is not null (would be at end of linked list) AND the values of the two are the same
    // change the value of nextDistictNode to be the next value (nextDistictNode.next)
    while (nextDistictNode !== null && nextDistictNode.value === currentNode.value) {
      nextDistictNode = nextDistictNode.next
    }
    // "remove:" the connection for the duplicate value by setting it to the next value of the nextDistictNode
    currentNode.next = nextDistictNode
    // now move the point forward and reassign currentNode to be the nextDistictNode
    currentNode = nextDistictNode
  }
  return linkedList
}

// TIME: O(max(n,m)) -> n = 1st LL & m = 2nd LL
// SPACE: O(max(n,m)) -> n = 1st LL & m = 2nd LL
function sumOfLinkedLists(linkedListOne, linkedListTwo) {
  // move tnrough bothj linked list at the same time
  // add the pointer to the next node and carry and carry over
  // create a dummy node to track head
  let dummyHeadPointer = new LinkedList(0)
  // create variable to keep track of current node
  // set the current node to the dummy head
  let currentNode = dummyHeadPointer
  //make a carry to track the sum
  let carry = 0
  // create nodeOne and nodeTwo used to iterate thropugh LL's
  let nodeOne = linkedListOne
  let nodeTwo = linkedListTwo
  //while loop - noneOne or nodeTwo is not null or carry != 0
  // while loop will run the length of the max LL
  while (nodeOne !== null || nodeTwo !== null || carry !== 0) {
    // assign values property to node.value
    let valueNodeOne = nodeOne === null ? 0 : nodeOne.value
    let valueNodeTwo = nodeTwo === null ? 0 : nodeTwo.value
    // sum these values and add the carry to them (carry needed for carry over)
    let sumOfValues = valueNodeOne + valueNodeTwo + carry
    //save the new value that we want to add to our new node -> MOD 10 to handle if there is a carry situation
    let newValue = sumOfValues % 10
    //create new LinkedList add this new node to our linked list by assigning next
    let newNode = new LinkedList(newValue)
    // add this newNode to our list with currentNode.next
    currentNode.next = newNode
    // change our current node to this node we just added
    currentNode = newNode
    // figure out carry and set variable
    carry = sumOfValues / 10
    // if the nodeOne value is not null iterate along .next else set it to null 
    nodeOne = nodeOne !== null ? nodeOne.next : null
    // if the nodeTwo value is not null iterate along with .next else set it to null
    nodeTwo = nodeTwo !== null ? nodeTwo.next : null
    // return the next node after the dummy node which is the head of our new list
    return dummyHeadPointer.next
  }


}

function mergeTwoLinkedList(linkedListOne, linkedListTwo) {
  // TIME = O(n + m) n = lngth LL 1 || m = lngth LL 2
  // SPACE = O(1) Constant
  let p1 = linkedListOne
  let p2 = linkedListTwo
  let prev
  while (p1 !== null && p2 !== null) {
    if (p1.value < p2.value) {
      prev = p1
      p1 = p1.next
    } else {
      if (prev !== null) prev.next = p2
      prev = p2
      p2 = p2.next
      prev.next = p1
    }
  }
  if (p1 === null) prev.next = p2
  return linkedListOne.value < linkedListTwo.value ? linkedListOne : linkedListTwo
}