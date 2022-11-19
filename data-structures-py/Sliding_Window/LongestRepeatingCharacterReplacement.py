# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
 

# Constraints:
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # take every char and count occurences of each char
        count = {}
        # int result to return
        result = 0
        # left point at zero
        left = 0
        # window is valid? take len of window and count of most freq char to get # of chars to replace in window to match most frequent
        # windowLen - Count[B] = # of chars in window that needs to be replaced

        # HUGE IMPROVEMENT - here
        max_f = 0
        # sliding window - right pointer in for loop in range(len(input))
        for right in range(len(s)):
            # to our hasmap add window right or increment it if it alrdy exist
            count[s[right]] = 1 + count.get(s[right], 0)
            max_f = max(max_f, count[s][right])
            # if right minus left plus 1 minus the max of the count value is less than k
            if (right - left + 1) - max_f > k:
                # shifting left pointer
                count[s[left]] -= 1
                # increment left to shift window right
                left += 1
            # update result -> max of current result or right minus left plus 1
            result = max(result, (right - left + 1))
        # return result  
        return result



        # max f = most frequent count variable - ONE PROBLEM WHEN SHIFTING MUST UPDATE COUNT MAP
        # result is only changed when a NEW max freq occurs
        # length - maxF <= k