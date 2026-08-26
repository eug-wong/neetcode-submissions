class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # 2 steps
        # 1. mark for popping
        # 2. apply "gravity"

        rows, cols = len(board), len(board[0])
        while True:
            popped = set()
            # mark rows first
            for row in range(rows):
                for col in range(2, cols):
                    if board[row][col] == board[row][col - 1] == board[row][col - 2] and board[row][col] != 0:
                        popped.add((row, col))
                        popped.add((row, col - 1))
                        popped.add((row, col - 2))
            
            for col in range(cols):
                for row in range(2, rows):
                    if board[row][col] == board[row - 1][col] == board[row - 2][col] and board[row][col] != 0:
                        popped.add((row, col))
                        popped.add((row - 1, col))
                        popped.add((row - 2, col))
            
            for row, col in popped:
                board[row][col] = 0
            
            if len(popped) == 0:
                break

            for col in range(cols):
                l, r = rows - 1, rows - 1
                while r >= 0:
                    if board[r][col] != 0:
                        board[l][col], board[r][col] = board[r][col], board[l][col]
                        l -= 1
                    r -= 1

        return board
            
