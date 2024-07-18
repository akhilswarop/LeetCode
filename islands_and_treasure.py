from collections import deque


class Solution:
    def islandsAndTreasure(self, grid) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        def addCell(r,c):
            if (
                r<0 or r == ROWS or c<0 or c == COLS or grid[r][c] == -1 or (r,c) in visited
            ):
                return 
            q.append([r,c])
            visited.add((r,c))

        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
            distance+=1
            
s = Solution()
s.islandsAndTreasure([
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
])