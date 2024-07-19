class Solution:
    def solve(self, board):
        ROWS = len(board)
        COLS = len(board[0])
        def capture(r,c):
            if ( r < 0 or r == ROWS or c == COLS or c<0 or board[r][c] != "O"):
                return 
            if board[r][c] == "O":
                board[r][c] = "T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS-1] or c in [0, COLS-1]:
                    capture(r,c)

        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        
s = Solution()
board =   [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]
s.solve(
    board
)