# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.

 

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Constraints:
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [x for x in nums]     
        heapq.heapify(maxHeap)
        print('maxHeap -> Start',maxHeap)
        
        for x in range(len(maxHeap) - k):
            print('maxHeap -> Loop',maxHeap)
            print('k',k)
            the_pop = heapq.heappop(maxHeap)
            print('the_pop ->', the_pop)
        return heapq.heappop(maxHeap)
        
        
        
        