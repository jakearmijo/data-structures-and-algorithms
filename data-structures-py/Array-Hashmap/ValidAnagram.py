# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different 
# word or phrase, typically using all the original letters exactly once.

class Solution(object):
  def validAnagram(self,s,t ) -> bool:
    hashmap = {}
    for x in s:
      if x in hashmap:
        hashmap[x] += 1
      else:
        hashmap[x] = 1

    for y in range(len(t)):
      if y in hashmap:
        hashmap[y] += 1
      else:
        return False

    return True

