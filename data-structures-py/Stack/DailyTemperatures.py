# Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have 
# to wait after the ith day to get a warmer temperature. If there is no future 
# day for which this is possible, keep answer[i] == 0 instead.

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # creating list of length temperatures and filling with zeros
        answer = [0] * len(temperatures)
        # init stack 
        stack = []
        
        # loops over temperatures and grabbing index and temp
        for idx,temp in enumerate(temperatures):
            # while there is a stack and the current temp is greater than the last value in the stack
            while stack and temp > stack[-1][0]:
                # destructure out current element of stack temp and index with POP
                stackTemp, stackIdx = stack.pop()
                # adding to our answer result at the same index of the current i
                answer[stackIdx] = (idx - stackIdx)
            # if there is no values or the temp is not greater than top of stack value append to stack
            stack.append([temp,idx])
        # return result. default is 0 and our answer list is filled with zeros - from description
        return answer
            