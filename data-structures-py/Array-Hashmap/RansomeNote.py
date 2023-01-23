# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    mag_hash = {}

    for char in magazine:
        if char in mag_hash:
            mag_hash[char] = 1 + mag_hash.get(char,0)
        else:
            mag_hash[char] = 1

    for char in ransomNote:
        if char in mag_hash and mag_hash[char] > 0:
            mag_hash[char] = mag_hash.get(char,0) - 1
        else:
            return False

    return True
    