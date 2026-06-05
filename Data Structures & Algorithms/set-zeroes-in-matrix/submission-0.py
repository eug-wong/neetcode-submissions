class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.append([i, j])
        
        for zero in zeroes:
            for i in range(len(matrix)):
                matrix[i][zero[1]] = 0
            
            for j in range(len(matrix[0])):
                matrix[zero[0]][j] = 0
                
        return