class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #init array filled with 1's - len of input nums
        output = [1] * (len(nums))
        # assign prefix to multiply
        prefix = 1
        # loop forward and multiply by prefix
        for i in range(len(nums)):
          # reassign value inside list for that index
            output[i] = prefix
            # now multiply for prefix
            prefix *= nums[i]
        # init postfix variable
        postfix = 1    
        # loop backwards and multiply by postfix now
        for i in range(len(nums) - 1,-1,-1):
          # this index in array multipled by current postfix
            output[i] *= postfix
            postfix *= nums[i]
        
        return output