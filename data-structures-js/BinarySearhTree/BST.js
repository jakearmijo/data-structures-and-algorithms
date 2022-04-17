// What are Binary trees?
// A binary Tree is a special type of tree where each node can have at most two children.
// Binary tree is generally partitioned into three disjoint subsets, i.e. the root of the tree, left sub-tree and right sub-tree.
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
    this.description = {
      explain: "A binary Tree is a special type of tree where each node can have at most two children.",
      tips: "the root of the tree, left sub-tree and right sub-tree. Time => O(log(n)). Smallest on far left largest on far right",
      traverse: "3 Traversal Methods -> in Order / Pre Order / Post Order"
    }
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

function validateBST(tree) {
// minimum value and max value
// value of child has a min value
// going left the value of the child has to be less than the index node
// helper function to pass the min and max value to validateBST
// depth is the length of the longest branch
// Time = O(N)
//Space = O(d) d is the depth of the tree
return validateBSTHelper(tree, -Infinity, Infinity)

}

function validateBSTHelper(tree, minValue, maxValue) {
  if (tree === null) return true
  if (tree.value < minValue || tree.value >= maxValue) return false
  let leftIsValid = validateBSTHelper(tree.left, minValue, tree.value)
  return leftIsValid && validateBSTHelper(tree.right, tree.value, maxValue)
}

function inOrderTraverse(tree, array) {
  if (tree !== null) {
    inOrderTraverse(tree.left, array)
    array.push(tree.value)
    inOrderTraverse(tree.right, array)
  }
  return array
}

function preOrderTraverse(tree, array) {
  if (tree !== null) {
    array.push(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
  }
  return array
}

function postOrderTravers(tree, array) {
  if (tree !== null) {
    postOrderTravers(tree.left, array)
    postOrderTravers(tree.right, array)
    array.push(tree.value)
  }
  return tree
}

function findKthLargestValueInBst(tree, k) {
  // O(n) time | O(n) space - where n is the number of nodes in the tree
  // traverse IN ORDER to compile array of sorted values.
  // return value at the length of the sorted values array minus k
  const sortedValues = []
  inOrderTraverse(tree,sortedValues)
  return sortedValues[sortedValues.length - k]
}
