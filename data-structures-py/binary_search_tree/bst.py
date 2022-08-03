
class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    currentNode = self
    while True:
      if value < currentNode.value:
        if currentNode.left is None:
          currentNode.left = BST(value)
          break
        else:
          currentNode = currentNode.left
      else:
        if currentNode.right is None:
          currentNode.right = BST(value)
          break
        else:
          currentNode = currentNode.right
    return self
  
  def contains(self, value):
    pass
  
  def remove(self, value, parent_node = None):
    pass