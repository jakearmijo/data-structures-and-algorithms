# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # init left point
        left = 0
        # create set to act as window
        charSet = set()
        # init longest tracker
        longest = 0
        
        # right pointer is in loop
        for r in range(len(s)):
          # if the char is in our char set remove it and slide window
            while s[r] in charSet:
              # removing char from set
                charSet.remove(s[left])
                # sliding window
                left += 1
            # adding the string[right] value to window - cause we slid it right
            charSet.add(s[r])
            # update longest between current longest and (right - left + 1)
            longest = max(longest, r - left + 1)
        # return longest
        return longest



sol_class = Solution()

s = "abcabcbb"
sol_class.lengthOfLongestSubstring(s)    
s = "bbbbb"
sol_class.lengthOfLongestSubstring(s)    
s = "pwwkew"
sol_class.lengthOfLongestSubstring(s)               
        