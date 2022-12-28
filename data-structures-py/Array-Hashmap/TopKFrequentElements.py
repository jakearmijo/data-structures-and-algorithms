
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #init hash map to track values
        count = {}
        # init array to track frequency of each number
        frequency = [ [] for i in range(len(nums) + 1) ]
        # loop over nums and map the value to the hashmap
        for n in nums:
          count[n] = 1 + count.get(n, 0)
        # loop over the hashmap items and at the value in the array 
        # in example if value 1 occurs twice. Then inside the array index 2 will have [1]
        for n, c in count.items():
          frequency[c].append(i)
        # declare a result array must return last value of frequency
        result = []
        # loop over frequency array backwards and append the values until it is k size
        for i in range(len(frequency) - 1, 0, -1):
          for n in frequency[i]:
            result.append(n)
            if len(result) == k:
              return result
