


class Node {
  constructor(name) {
    this.name = name;
    this.children = [];
  }

  addChild(name) {
    this.children.push(new Node(name));
    return this;
  }

  depthFirstSearch(array) {
    // Write your code here.
    // each node is a vertex - each line or connection is an edge
    // Time = O(v + e)
    // Space = O(v)
		array.push(this.name)
		for (const child of this.children){
			child.depthFirstSearch(array)
		}
		return array
  }
}