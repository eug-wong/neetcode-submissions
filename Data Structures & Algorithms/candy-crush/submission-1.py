class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # split into 2 parts
        # crush all available, set to 0
        # apply gravity
        # rinse and repeat
        rows, cols = len(board), len(board[0])
        while True:
            pop = set()

            # find horizontal pops
            for i in range(rows):
                l, r = 0, 0
                while r < cols:
                    t = set()
                    while r < cols and board[i][l] == board[i][r]:
                        if board[i][r] != 0:
                            t.add((i, r))
                        r += 1
                    
                    if len(t) > 2:
                        pop = pop | t
                    
                    l = r

            # find vertical pops
            for j in range(cols):
                l, r = 0, 0
                while r < rows:
                    t = set()
                    while r < rows and board[l][j] == board[r][j]:
                        if board[r][j] != 0:
                            t.add((r, j))
                        r += 1
                    
                    if len(t) > 2:
                        pop = pop | t
                    
                    l = r

            # exit if there's nothing to pop!
            if len(pop) == 0:
                break

            # pop
            for i, j in pop:
                board[i][j] = 0
            
            # gravity
            for j in range(cols):
                l, r = rows - 1, rows - 1
                while r >= 0:
                    if board[r][j] == 0 and board[l][j] != 0:
                        l = r
                    
                    if board[r][j] != 0 and board[l][j] == 0:
                        board[l][j] = board[r][j]
                        board[r][j] = 0
                        l -= 1

                    r -= 1

        return board