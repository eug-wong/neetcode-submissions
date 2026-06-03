class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        exists = False
        rows = len(board)
        cols = len(board[0])

        if len(word) > rows * cols:
            return False
        # print(rows, cols)
        # print(board[rows - 1][cols - 1])
        def check(row, col, running, length, mod_board):
            nonlocal exists
            # base case, length reached
            if length >= len(word):
                return
            
            # print(running)
            if running == word:
                exists = True
                return
            
            # check if left available, if so, explore
            if col - 1 > -1 and col - 1 < cols and mod_board[row][col - 1] != -1:
                temp = running + board[row][col - 1]
                temp_b = board[row][col - 1]
                mod_board[row][col - 1] = -1
                check(row, col - 1, temp, length + 1, mod_board)
                mod_board[row][col - 1] = temp_b

            # check if right available, if so, explore
            if col + 1 > -1 and col + 1 < cols and mod_board[row][col + 1] != -1:
                temp = running + board[row][col + 1]
                temp_b = board[row][col + 1]
                mod_board[row][col + 1] = -1
                check(row, col + 1, temp, length + 1, mod_board)
                mod_board[row][col + 1] = temp_b


            # check if up available, if so, explore
            if row - 1 > -1 and row - 1 < rows and mod_board[row - 1][col] != -1:
                temp = running + board[row - 1][col] 
                temp_b = board[row - 1][col]
                mod_board[row - 1][col] = -1
                check(row - 1, col, temp, length + 1, mod_board)
                mod_board[row - 1][col] = temp_b

            # check if down available, if so, explore
            if row + 1 > -1 and row + 1 < rows and mod_board[row + 1][col] != -1:
                temp = running + board[row + 1][col]
                temp_b = board[row + 1][col]
                mod_board[row + 1][col] = -1
                check(row + 1, col, temp, length + 1, mod_board)
                mod_board[row + 1][col] = temp_b

        for row in range(rows):
            for col in range(cols):
                check(row, col, board[row][col], 0, board)

        return exists
            