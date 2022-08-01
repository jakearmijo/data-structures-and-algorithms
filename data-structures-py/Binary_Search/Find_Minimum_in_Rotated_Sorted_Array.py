class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1
        min_element = nums[0]
        
        while left <= right:
            # if left is less then right we know we are in a sorted array
            # this means nums[left] is our smallest possible value
            if nums[left] <= nums[right]:
                min_element = min(min_element, nums[left])
                break
            
            # find mid value
            mid = (left + right) // 2
            # update min_element to the minimum element b/w the current value and the new nums[mid]
            min_element = min(min_element,nums[mid])
            
            # check is the value at mid is a part of left sorted portion
            if nums[mid] >= nums[left]:
                left = mid + 1
            # the else case - we are in the right sorted portion and will move the right pointer
            else:
                right = mid - 1
        #we have looped through and can return the minimum element value
        return min_element
            
            