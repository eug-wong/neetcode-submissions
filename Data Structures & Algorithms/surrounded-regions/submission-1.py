class Solution:
    def solve(self, board: List[List[str]]) -> None:
        notSurrounded = set()
        
        # i and j is within bounds
        def isValid(i, j):
            return i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and (i, j) not in notSurrounded and board[i][j] == "O"
        
        # searches for Os connected to ocean
        def dfs(i, j):
            nonlocal notSurrounded
            notSurrounded.add((i, j))

            # check up
            if isValid(i - 1, j):
                dfs(i - 1, j)
            # check down
            if isValid(i + 1, j):
                dfs(i + 1, j)
            # check left
            if isValid(i, j - 1):
                dfs(i, j - 1)
            # check right
            if isValid(i, j + 1):
                dfs(i, j + 1)

            return
        

        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    dfs(i, j)
        
        for i in range(len(board)):
            for j in [0, len(board[0]) - 1]:
                if board[i][j] == "O":
                    dfs(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in notSurrounded:
                    board[i][j] = "X"
        print(notSurrounded)
        return