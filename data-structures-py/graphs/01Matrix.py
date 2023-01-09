# 542. 01 Matrix
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

import collections

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # find size of graph - ROWS and COLS
        ROWS, COLS = len(mat), len(mat[0])
        # defines internal BFS func
        def bfs(r,c):
          # init a queue for processing
          q = collections.deque()
          # append the r, c and dist values to the queue
          q.append(((r,c),0))
          # init visited set for no rework
          visited = set()
          # create directions variable for looping later
          directions = [[1,0],[-1,0],[0,1],[0,-1]]
          # while there is a q - we do work
          while q:
            # looping over the q
            for i in range(len(q)):
              # unpack values from q.popLeft()
              coor, dist = q.popleft()
              # unpack row and col values from coor
              row, col = coor
              # if the current row , col value in matrix is a zero
              if mat[row][col] == 0:
                # just return its dist
                return dist
              # add the current coor value to the visited set
              visited.add(coor)
              # now loop over directions and unpack dr,dc
              for dr,dc in directions:
                # the new_r and new_c value will be the row + dr and col + dc
                new_r, new_c = row + dr, col + dc
                # if this new_r value is greater than or equal to 0 and the rew_r is within the range of ROWS 
                # and the new_c value is greater than or equal to 0 and the new_c is within the range of COLS
                # and the new_r, new_c has not been visited yet
                if (new_r >= 0 and new_r in range(ROWS) and
                    new_c >= 0 and new_c in range(COLS) and
                    (new_r, new_c) not in visited):
                    # append this (new_r, new_c), dist PLUS 1) to the queue
                     q.append(((new_r, new_c), dist + 1))
          # return the while loop
          return
        # loops over every element in graph
        for r in range(ROWS):
            for c in range(COLS):
              # the current element does not equal 0
              if mat[r][c] != 0:
                # run our bfs func to return the distance
                dist = bfs(r,c)
                # change the current value of the current element to this distance
                mat[r][c] = dist
        # after all is complete return the mat
        return mat
