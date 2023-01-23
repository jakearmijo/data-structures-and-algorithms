# Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. 
# Only compress the string if it saves space.

# Constraints
# Can we assume the string is ASCII?
# Yes
# Note: Unicode strings could require special handling depending on your language
# Is this case sensitive?
# Yes
# Can we use additional data structures?
# Yes
# Can we assume this fits in memory?
# Yes

# Test Cases
# None -> None
# '' -> ''
# 'AABBCC' -> 'AABBCC'
# 'AAABCCDDDD' -> 'A3BC2D4'

class Solution:
  def CompressString(self, string: str) -> str:

    if not string is None or not string:
      return string

    result = ''
    count = 1
    prev_char = string[0]
    
    # looping over string
    for char in string:
      # If char is the same as last_char, increment count
      if char == prev_char:
        count += 1
      else:
        # Append prev_char and count to compressed_string
        result += self.calculate_partial_result(prev_char, count)
        # moving prev_char to the new char
        prev_char = char
        # resetting count to 1
        count = 1
    # after for loop appending our calc partial result to the result
    result += self.calculate_partial_result(prev_char, count)

    # return our new compressed string if the len of this string 
    # is less than the original string else returning the original string
    return result if len(result) < len(string) else string

  # Append prev_char and count to compressed_string if the count is greater than 1 else nothing
  def calculate_partial_result(self, prev_char: str, count: int) -> str:
    return prev_char + (str(count) if count > 1 else '')

# Complexity:
# Time: O(n)
# Space: O(n)
# Complexity Note:
# Although strings are immutable in Python, appending to strings is optimized in 
# CPython so that it now runs in O(n) and extends the string in-place. 
# Refer to this Stack Overflow post.

testing = Solution()
print('None --> ',testing.CompressString(None))
print('"" --> ',testing.CompressString('""'))
print('AABBCC --> ',testing.CompressString('AABBCC'))
print('AAABCCDDDDE --> ',testing.CompressString('AAABCCDDDDE'))
print('BAAACCDDDD --> ',testing.CompressString('BAAACCDDDD'))
print('AAABAACCDDDD --> ',testing.CompressString('AAABAACCDDDD'))

