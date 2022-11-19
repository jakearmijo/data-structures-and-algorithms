# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # edge case if lev s1 is greater then s2
        if len(s1) > len(s2):
          return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
          # this will produce an index we can assign to array index
          s1_count[ord(s1[i]) - ord('a')] += 1
          s2_count[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
          # increasing matches if indexes in each array have same value
          matches += (1 if s1_count[i] == s2_count[i] else 0)

        l = 0 

        for r in range(len(s1), len(s2)):
          if matches == 26:
            return True
          # updater matches and Move LEFT
          index = ord(s2[r]) - ord('a')
          s2_count[index] += 1
          # moved window and change 
          if s1_count[index] == s2_count[index]:
            matches += 1
          elif s1_count[index] + 1 == s2_count[index]:
            matches -= 1

          # updater matches and Move RIGHT
          index = ord(s2[l]) - ord('a')
          s2_count[index] -= 1
          # moved window and change 
          if s1_count[index] == s2_count[index]:
            matches += 1
          elif s1_count[index] - 1 == s2_count[index]:
            matches -= 1
          l += 1

        return matches == 26

          
