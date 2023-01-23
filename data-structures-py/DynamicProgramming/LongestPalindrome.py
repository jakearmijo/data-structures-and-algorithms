# 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, 
# return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

class Solution:
    def longestPalindrome(self, s: str) -> int:
      s_set = set()
      #we have created a set that will track unique letter
      for char in s:
        # if the char is not in the set remove it else add it
        if char not in s_set:
          s_set.add(char)
        else:
          s_set.remove(char)
      # if the len of the set !== 0 - we have a small pali
      if len(s_set) != 0:
        # return the len of input s minus the length of the set + 1
        return len(s) - len(s_set) + 1
        # else the entire string is a pali so return it
      else:
        return len(s)
