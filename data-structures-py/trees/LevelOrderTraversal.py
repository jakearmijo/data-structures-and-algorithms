import collections

class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def levelOrderTraversal(self, root: TreeNode) -> str:
    result = []
    q = collections.deque()
    q.append(root)

    while q:
      qLen = len(q)
      for i in range(qLen):
        node = q.popleft()
        if node:
          result.append(str(node.val))
          q.append(node.left)
          q.append(node.right)

    print(" ".join(result))
