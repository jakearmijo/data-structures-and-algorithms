import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # https://www.w3schools.com/python/python_regex.asp

        #trim all spaces and make lower case
        s = s.lower(re.sub(r'[^a-zA-Z0-9]', '', s))
        L = 0
        R = len(s) - 1
        
        # Binary Search to see if each pointer is the exact same
        while L <= R:
            if s[L] != s[R]:
                return False
            else:
                L += 1
                R -= 1
        return True