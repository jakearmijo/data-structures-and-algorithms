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

        # sliding window - right pointer in for loop in range(len(input))
        for right in range(len(s)):
            # to our hasmap add window right or increment it if it alrdy exist
            count[s[right]] = 1 + count.get(s[right], 0)
            # if right minus left plus 1 minus the max of the count value is less than k
            if (right - left + 1) - max(count.values()) > k:
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