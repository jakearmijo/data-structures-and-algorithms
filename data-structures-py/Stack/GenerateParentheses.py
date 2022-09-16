# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # init stack
        stack = []
        # init array to track combos
        combos = []

        # RESURSIVE FUNCTION INSIDE
        def back_track(open_count, closed_count):
          # if the open count is equal to closed cloud equal to n append the join() string to stack
          # return
          if open_count == closed_count == n:
            # append into combos array
            combos.append(''.join(stack))
            return

          # if open is less than n we can add open
          if open_count < n:
            # append open
            stack.append('(')
            # recursive call with open + 1
            back_track(open_count + 1, closed_count)
            # clean up stack
            stack.pop()
          # if closed count is less than open we can add closed
          if closed_count < open_count:
            # append closed to stack
            stack.append(')')
            # recursive call with closed + 1
            back_track(open_count, closed_count + 1)
            # clean up stack
            stack.pop()

        # call our recursive function
        back_track(0,0)
        # return our combos array
        return combos