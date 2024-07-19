class Solution:
    def pacificAtlantic(self, heights):
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()
        def dfs(r, c, visited, prevHeight):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or prevHeight < heights[r][c]):
                return 
            visited.add((r,c))
            dfs(r+1, c, visited, prevHeight)
            dfs(r-1, c, visited, prevHeight)
            dfs(r, c+1, visited, prevHeight)
            dfs(r, c-1, visited, prevHeight)
            


        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, atl, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in ROWS:
            for c in COLS:
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res

        

                
s = Solution()
s.pacificAtlantic(
    [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
)