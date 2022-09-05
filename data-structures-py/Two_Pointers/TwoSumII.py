class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # array is sorted and garunteed 1 answer
        # 2 pointers Binary Search
        p1 = 0
        p2 = len(numbers) - 1
        
        while p1 <= p2:
            _sum = numbers[p1] + numbers[p2]
            
            if _sum < target:
                p1 = p1 + 1
            if _sum > target:
                p2 = p2 - 1
            if _sum == target:
                return [p1 + 1, p2 + 1]
            