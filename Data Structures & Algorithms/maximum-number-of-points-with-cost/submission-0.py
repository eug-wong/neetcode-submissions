class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # figure out time complexity
        cache = {}
        def dp(row, col):
            # base case is out of bounds
            if row == len(points) - 1:
                return 0
            
            if (row, col) in cache:
                return cache[(row, col)]
            
            res = 0
            for col2 in range(len(points[0])):
                res = max(res, dp(row + 1, col2) + points[row + 1][col2] - abs(col2 - col))
            
            cache[(row, col)] = res
            
            return res
        
        res = 0
        for col in range(len(points[0])):
            res = max(res, points[0][col] + dp(0, col))
        
        return res