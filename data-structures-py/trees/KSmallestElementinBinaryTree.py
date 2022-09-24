# 230. Kth Smallest Element in a BST
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 
# Constraints:
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

# Definition for a binary tree node.

## Iterative

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class IterativeSolution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur and stack:
          while cur:
            stack.append(cur)
            cur = cur.left
            
          cur = stack.pop()
          n += 1
          if n == k:
            return cur.val
          cur = cur.right

## Recursive

class RecursiveSolution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.result = None
        self.inOrder(root)
        return self.result

    def inOrder(self,node):
      if not node:
        return
      self.inOrder(node.left)
      self.k -= 1

      if self.k == 0:
        self.result = node.val
        return

      self.inOrder(node.right)
