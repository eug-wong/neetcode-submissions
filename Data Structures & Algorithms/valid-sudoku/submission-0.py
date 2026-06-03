class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            freq = {}
            for j in range(9):
                num = board[i][j]
                if num == '.': continue
                freq[num] = freq.get(num, 0) + 1
                if freq[num] > 1:
                    return False
        
        for i in range(9):
            freq = {}
            for j in range(9):
                num = board[j][i]
                if num == '.': continue
                freq[num] = freq.get(num, 0) + 1
                if freq[num] > 1:
                    return False
        
        for square in range(9):
            freq = {}
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    num = board[row][col]
                    if num == '.': continue
                    freq[num] = freq.get(num, 0) + 1
                    if freq[num] > 1:
                        return False
        
        return True