

from re import S


class Solution:
  """
  """
  def encode(self, strs: List[str]) -> str:
    """
    """
    res = ''
    for s in strs:
      res += str(len(s)) + '#' + s

    return res

  def decode(self, str: str) -> List[str]:
    """
    """
    res, i = [], 0

    while i < len(str):
      j = i
      while str(j) != '#':
        j += 1
      length = int(str[i:j])
      res.append(str[i + 1: j + 1 + length])
      i = j + 1 + length

    return res