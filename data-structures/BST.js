// Binary Search Tree
// each Node has up to 2 children nodes
// Time => O(log(n))
// K-ary Tree => nodes have up to k child-nodes. Binary Tree is K-ary Tree where k == 2
// Perfect Binary Tree => interior nodes have 2 children and whose lead nodes all have the same depth
// Complete Binary Tree => interior nodes all have two children but its leaf nodes dont necessarily have the same depth
// Balanced Binary Tree => nodes all have left and right subtree whose heights differ by no more than 1 -> Logarithmic time somplexity
// Full Binary Tree => noes all have either two child-nodes or zero child-nodes

class BST {
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }
  insert(value) {
    // start by comparing the node we have to the value
    // if smaller insert the value to the left of this.value
    // if larger insert the value to the right of this.value
    // return BST at the end
    if (value < this.value) {
      if (this.left === null) {
        this.left = new BST(value)
      } else {
        this.left.insert(value)
      }
    } else {
      if (this.right === null) {
        this.right = new BST(value)
      } else {
        this.right.insert(value)
      }
    }
    return this
  }
  contains(value) {
    // checking if the value is small then check left
    // if null it doesnt exist
    // recursive call on left node to continue the process
    // check right if the value is larger then check right
    // if null it doesnt exist
    // recursive call on the right node
    // if all above fails return true - you found it
    if (value < this.value) {
      if (this.left == null) {
        return false
      } else {
        return this.left.contains(value)
      }
    } else if (value > this.value) {
      if (this.right == null) {
        return false
      } else {
        return this.right.contains(value)
      }
    } else {
      return true
    }
  }
  remove(value, parent = null) {
    // grabbing smallest value on the left most node
    // then replace the this.value with the left most node this.value
    if (value < this.value) {
      if (this.left !== null) {
        this.left.remove(value, this)
      }
    } else if (value > this.value) {
      if (this.right !== null) {
        this.right.remove(value, this)
      }
    } else {
      if (this.left !== null && this.right !== null) {
        this.value = this.right.getSmallestValue()
        this.right.remove(this.value, this)
      } else if (parent === null) {
        if (this.left !== null) {
          this.value = this.left.value
          this.left = this.left.left
          this.right = this.right.right
        } else if (this.right !== null) {
          this.value = this.right.value
          this.left = this.right.left
          this.right = this.right.right
        } else {
          // do nothing
        }
      } else if (parent.left === this) {
        parent.left = this.left !== null ? this.left : this.right
      } else if (parent.right === this) {
        parent.right = this.right !== null ? this.left : this.right
      }
    }
    return this
  }
  getSmallestValue() {
    // helper function that continues left to find smallest value
    if (this.left === null) {
      return this.value
    } else {
      return this.left.getSmallestValue()
    }
  }
}