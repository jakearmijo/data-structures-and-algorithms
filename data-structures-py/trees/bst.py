import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
  def __init__(self, val=None):
    self.root = val

  def insert(self, val):
    new_node = TreeNode(val)
    if not self.root:
      self.root = new_node
    else:
      cur_node = self.root
      while True:
        if val < cur_node.val:
          if not cur_node.left:
            cur_node.left = new_node
            return self
          cur_node = cur_node.left
        else:
          if not cur_node.right:
            cur_node.right = new_node
            return self
          cur_node = cur_node.right
  
  def contains(self, val):
    if not self.root:
      return False
    cur_node = self.root
    while cur_node:
      if val < cur_node.val:
        cur_node = cur_node.left
      elif val > cur_node.val:
        cur_node = cur_node.right
      elif val == cur_node.val:
        return cur_node.val
    
    return False

  def remove(self, val, parent_node = None):
    pass

  def BreadthFirstSearch(self):
    cur_node = self.root
    result = []
    que = collections.deque()
    que.append(cur_node)

    while len(que) > 0:
      cur_node = que.popleft()
      result.append(cur_node.val)
      if cur_node.left:
        que.append(cur_node.left)
      if cur_node.right:
        que.append(cur_node.right)
      
    return result

  def BreadthFirstSearchRecursive(self, que,list_result):
    if not len(que):
      return list_result
    cur_node = que.popLeft()
    list_result.append(cur_node.val)

    if cur_node.left:
      que.append(cur_node.left)
    if cur_node.right :
      que.append(cur_node.right)
    
    return self.BreadthFirstSearchRecursive(que,list_result)

  def DFTPreOrder(self,cur_node):
    if not cur_node:
      return

    def traversePreOrder(node,result):
      if not node:
        return
      result.append(node.val)
      if node.left:
        traversePreOrder(node.left,result)
      if node.right:
        traversePreOrder(node.right,result)
      return result
    
    return traversePreOrder(self.root,[])

  def DFTInOrder(self,cur_node):
    if not cur_node:
      return

    def traverseInOrder(node,result):
      if not node:
        return
      if node.left:
        traverseInOrder(node.left,result)
      result.append(node.val)
      if node.right:
        traverseInOrder(node.right,result)
      return result
    
    return traverseInOrder(self.root,[])
  
  def DFTPostOrder(self,cur_node):
    if not cur_node:
      return

    def traversePostOrder(node,result):
      if not node:
        return
      if node.left:
        traversePostOrder(node.left,result)
      if node.right:
        traversePostOrder(node.right,result)
      result.append(node.val)
      return result
    
    return traversePostOrder(self.root,[])





tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print('BFS ->',tree.BreadthFirstSearch())
new_que = collections.deque()
print('BFSR ->',tree.BreadthFirstSearchRecursive(new_que, []))
print('DFS PRE ->',tree.DFTPreOrder(tree.root))
print('DFS IN ->',tree.DFTInOrder(tree.root))
print('DFS POST ->',tree.DFTPostOrder(tree.root))

# ('BFS ->', [9, 4, 20, 1, 6, 15, 170])
# ('BFSR ->', [])
# ('DFS PRE ->', [9, 4, 1, 6, 20, 15, 170])
# ('DFS IN ->', [1, 4, 6, 9, 15, 20, 170])
# ('DFS POST ->', [1, 6, 4, 15, 170, 20, 9])