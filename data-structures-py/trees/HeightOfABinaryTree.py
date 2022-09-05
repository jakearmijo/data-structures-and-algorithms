class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def heightOfABinaryTree(self, root: TreeNode) -> int:
    if not root:
      return -1

    return 1 + max(self.heightOfABinaryTree(root.left), self.heightOfABinaryTree(root.right))