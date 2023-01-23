# 647. Palindromic Substrings

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
          # since logic is the same we created a helper function that will assist with pali logic

            # this is for odd pali
            result += self.countPalindrome(s,i,i)
            # this is for even pali
            result += self.countPalindrome(s,i,i+1)
        return result

    # pali helper to check the length of the palindrome 
    # traversing from the current element outward
    def countPalindrome(self, s, left, right):
        result = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
        return result