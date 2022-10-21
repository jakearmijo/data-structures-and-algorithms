# 130. Surrounded Regions
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]

# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfsCapture(r,c):
          if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O':
            return
          board[r][c] = 'T'
          dfsCapture(r + 1,c)
          dfsCapture(r - 1,c)
          dfsCapture(r,c + 1)
          dfsCapture(r,c - 1)

        for r in range(ROWS):
          for c in range(COLS):
            if board[r][c] == '0' and (r in [0, ROWS - 1] or c in [0, COLS -1]):
              dfsCapture(r,c)

        for r in range(ROWS):
          for c in range(COLS):
            if board[r][c] == 'O':
              board[r][c] == 'X'
        
        for r in range(ROWS):
          for c in range(COLS):
            if board[r][c] == 'T':
              board[r][c] == 'O'