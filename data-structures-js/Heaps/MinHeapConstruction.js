// A Heap is a special Tree-based data structure in which the tree is a complete binary tree. Generally, Heaps can be of two types:
// Max-Heap: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
// Min-Heap: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.

class MinHeap {
  constructor(array) {
    this.heap = this.buildHeap(array)
  }

  buildHeap(array) {
    const firstParentIdx = Math.floor((array.length - 2) / 2)
    for (let currentIdx = firstParentIdx; currentIdx >= 0; currentIdx--){
      this.siftDown(currentIdx, array.length - 1, array)
    }
    return array
  }

  peek() {
    return this.heap[0]
  }

  siftUp(currentIdx, heap) {
    let parentIdx = Math.floor((currentIdx - 1) / 2)
    while (currentIdx > 0 && heap[currentIdx] < heap[parentIdx]) {
      this.swap(currentIdx,parentIdx,heap)
      currentIdx = parentIdx
      parentIdx = Math.floor((currentIdx - 1) / 2)
    }
  }

  siftDown(currentIdx, finalIdx, heap) {
    let childOneIdx = currentIdx * 2 + 1
    while (childOneIdx <= finalIdx) {
      // check for child 2. Each node has 2 children. If childOne exist check for child 2 
      const childTwoIdx = currentIdx * 2 + 2 <= finalIdx ? currentIdx * 2 + 2 : -1
      // declare swap variable
      let indexToSwap
      if (childTwoIdx !== -1 && heap[childTwoIdx] < heap[childOneIdx]) {
        indexToSwap = childTwoIdx
      } else {
        indexToSwap = childOneIdx
      }
      if (heap[indexToSwap] < heap[currentIdx]) {
        this.swap(currentIdx, indexToSwap, heap)
        currentIdx = indexToSwap
        childOneIdx = currentIdx * 2 + 1
      } else {
        return
      }
    }
  }

  remove() {
    this.swap(0,this.heap.length - 1, this.heap)

  }

  insert(value) {
    this.heap.push(value)
    this.siftUp(this.heap.length - 1, this.heap)
    let valueToRemove = this.heap.pop()
    this.siftDown(0, this.heap.length - 1, this.heap)
    return valueToRemove
  }
  
  swap(i,j,heap) {
    let temp = heap[j]
    heap[j] = heap[i]
    heap[i] = temp
  }
}