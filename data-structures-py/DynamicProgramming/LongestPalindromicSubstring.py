# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"
 
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
      res = ''
      res_len = 0

      for x in range(len(s)):
        # odd length pali
        left, right = x, x
        while left >= 0 and right < len(s) and s[left] == s[right]:
          if right - left + 1 > res_len:
            res = s[left : right + 1]
            res_len = right - left + 1
          left -= 1
          right += 1
        
        #even length pali
        left,right = x, x + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
          if right - left + 1 > res_len:
            res = s[left : right + 1]
            res_len = right - left + 1
          left -= 1
          right += 1

      return res

