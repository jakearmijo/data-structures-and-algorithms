# 417. Pacific Atlantic Water Flow

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

# Example 1:
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.


# Example 2:
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

# Constraints:
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac_visited, atl_visited = set(), set()

        #define our DFS taking in r,c,visited_set,prev_height
        def dfs(r,c,visited,prev_height):
          # now if this current position has already been viisted return
          # if r < 0 or r is out of bounds meaning r == ROWS
          # if c < 0 or c is out of bounds meaning c == COLS
          # or if the current heights[r][c] is less then the prev height

          if((r,c) in visited or r < 0 or r == ROWS or c < 0 or c == COLS or heights[r][c] < prev_height):
            return
          # now if we dont return we need to add the current r,c to the visited
          visited.add((r,c))
          # now run the fs function on each of the neighbor nodes
          dfs(r + 1,c,visited,heights[r][c])
          dfs(r - 1,c,visited,heights[r][c])
          dfs(r,c + 1,visited,heights[r][c])
          dfs(r,c - 1,visited,heights[r][c])

        # loop over every single position in the first row. so each col
        for c in range(COLS):
          # REMEMBER we are now reversed. So we are running from the middle to the ocean.
          # which means we are looking for larger values 

          #run dfs on first row - top are left are PACIFIC
          dfs(0,c,pac_visited,heights[0][c])
          #run dfs on last row - bottom and right are ATLANTIC 
          # our prevHeight will be the value of this current height
          dfs(ROWS - 1, c, atl_visited,heights[ROWS - 1][c])

        # now we need to run it on the first column PAC and last col ATL
        for r in range(ROWS):
          # we want every position in the left most column and call dfs on it - this is PAC ocean value
          dfs(r,0,pac_visited,heights[r][0])
          # we want the last column which we know is ATL
          dfs(r, COLS - 1, atl_visited,heights[r][COLS - 1])

        #   ONCE THESE TWO LOOPS ABOVE EXECUTE WE WILL HAVE MARKED EVERY SINGLE POSITION THAT CAN REACH THE 
        # PAC OVEAN IN THE PAC_VISITED HASHSET AND SAME FOR ATL HASH SET
        
        #decalre result to push into
        result = []
        # NOW WE LOOP OVER EVERY SINGLE POSITION IN GRID
        for r in range(ROWS):
          for c in range(COLS):
            if (r,c) in pac_visited and (r,c) in atl_visited:
              result.append([r,c])
        
        return result

        