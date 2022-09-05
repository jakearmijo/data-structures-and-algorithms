# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # if no height return 0
        if not height: return 0
        # init right and left pointer
        left, right = 0, len(height) - 1
        # setting leftMax and right Max variable to the height[either left or right]
        leftMax, rightMax = height[left], height[right]
        # total 
        totalWater = 0
        # while left is less than right
        while left < right:
          # if left Max is less than right Max
            if leftMax < rightMax:
                # increment left by 1
                left += 1
                # re assign leftMax to the max of current leftMax and new height[left]
                leftMax = max(leftMax, height[left])
                # to our total water add the difference of the leftMax minus height[left]
                totalWater += leftMax - height[left]
            else:
                # else the leftMax is greater than rightMax
                # decrement right
                right -= 1
                # re assign rightMax and the max of rightMax and height[right]
                rightMax = max(rightMax, height[right])
                # to the total water total add the difference of rightMax minus height[right]
                totalWater += rightMax - height[right]
        return totalWater
    


Solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
Solution.trap([4,2,0,3,2,5])