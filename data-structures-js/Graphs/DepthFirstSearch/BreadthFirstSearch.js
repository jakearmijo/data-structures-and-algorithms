
class Node {
  constructor(name) {
    this.name = name
    this.children = []
  }

  addChild(name) {
    this.children.push(new Node(name))
    return this
  }

  // Time = O(v + e) | Space = O(v)
  breadthFirstSearch(array) {
    //create queue from this context
    let queue = [this]
    // while loop - while queue is not empty ( length > 0)
    while (queue.length > 0) {
      // shift (removes and return first value of array) current node out of queue
      let currentNode = queue.shift()
      // current node name -> push into array
      array.push(currentNode.name)
      // add all the current node children nodes to the back of queue
      for (const child of currentNode.children) {
        queue.push(child)
      }
    }
    return array    
  }
}