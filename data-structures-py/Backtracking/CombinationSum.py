# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique 
# combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

# Constraints:
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      res = []

      def dfs(i,cur,total):
        # base cases we FOUND SUCCESS
        if total == target:
          # adding a copy of cur to the result
          # add copy because we are modifying cur on the fly
          res.append(cur.copy())
          return

        # Base Case if we went over or out of bounds
        if i >= len(candidates) or total > target:
          return
        
        # This is good so append this cur element
        cur.append(candidates[i])
        # call the DFS for decision #1 (which includes the dupe i)
        dfs(i, cur, total + candidates[i])
        # 2nd decision doesn't include dupes so POP first
        cur.pop()
        # 2nd dfs decision
        dfs(i + 1, cur, total)

      # now call out created internal dfs func to kick start process
      # i value will start at 0
      # cur will start as empty array []
      # total will start at 0
      dfs(0, [], 0)
      # now this ran all the way through and we return res
      return res
