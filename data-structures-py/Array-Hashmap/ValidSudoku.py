# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
import collections

class Solution(object):
  def isValidSudoku(self, board: list[list[str]]) -> bool:
    # init 3 hashmap with sets to track cols / rows / squares
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    # loop over each row in range of 9 -> its a 9x9 square
    for r in range(9):
      # loop over ech col
      for c in range(9):
        # check if the current value is empty continue
        if board[r][c] == '.':
          continue
        # if value is in any of our 3 hashmaps we return false
        # squares value will be divided by 3
        if (
            board[r][c] in rows[r] or
            board[r][c] in cols[c] or
            board[r][c] in squares[(r //3, c //3)]):
            # value is in one of our hashmaps so we return false
            return False
        # add current value to our hashmaps
        rows[r].add(board[r][c])
        cols[c].add(board[r][c])
        squares[r // 3, c // 3].add(board[r][c])
    # not found return True    
    return True