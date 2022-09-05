class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort first
        nums.sort()
        # init list for result
        all_triplets = []
        
        # enumerate with loop to grab index and value
        for i, val in enumerate(nums):
          # if its the same value move on
            if i > 0 and val == nums[i - 1]:
                continue
            # now two sum II with pointers and search
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                target = val + nums[p1] + nums[p2]
                if target > 0:
                    p2 -= 1
                elif target < 0:
                    p1 += 1
                else:
                  # value is what we need append to result array
                    all_triplets.append([val, nums[p1], nums[p2]])
                    p1 += 1
                    # make sure pointers are not on same value
                    while nums[p1] == nums[p1 - 1] and p1 < p2:
                        p1 += 1
            
            
        return all_triplets