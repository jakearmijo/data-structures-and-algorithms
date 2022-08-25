
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def isBalanced(self, root: TreeNode) -> bool:
    
    # dfs helper func
    def dfs(root):
      # base case if root is null
      if not root:
        # empty tree is balanced
        return [True, 0]
      # declare left and right to find balance
      # by running dfs on root.left and root.right
      left, right = dfs(root.left), dfs(root.right)
      # If balanced has 3 conditions
      # 1 - if the left[0] is true
      # 2 - if the right[0] is true
      # 3 - if the differnce is <= 1
      balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
      # return our array with index 1 as T/F and idx 2 as the hight
      # calculate hieght by using 1 + max(left height, right height)
      return [balanced, 1 + max(left[1], right[1])]
    
    #our helper ran on every inner node
    # run it on root to return value of entire tree
    # idx [0] is our T/F value
    return dfs(root)[0]