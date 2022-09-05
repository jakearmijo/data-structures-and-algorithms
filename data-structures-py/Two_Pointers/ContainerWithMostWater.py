# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
# of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
          return 0
        # init max area at zero
        maximumArea = 0
        # 2 pointers start and end
        left, right = 0, len(height) - 1
        # anything inside pointers can contain water. 
        # pointers have to be 
        while left < right:
          # area is height * width
          # width = right - left
            area = (right - left) * min(height[left], height[right])
            # maximum area is the max of the current max area and the new area
            maximumArea = max(maximumArea, area)
            # check which height is lower (water will spill out of the lower)
            if height[left] < height[right]:
              # increment left if lower
                left += 1
            else:
              # if left is greater decrement right
                right -= 1
                
        # return your maximumArea
        return maximumArea