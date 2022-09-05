
class Solution(object):
  def containsDuplicate(self, nums: list) -> bool:

    hashmap = {}

    for x in nums:
      if x in hashmap:
        return True
      hashmap[x] = 1
    
    return False
