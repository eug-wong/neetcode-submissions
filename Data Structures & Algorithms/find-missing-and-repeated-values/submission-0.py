class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq = defaultdict(int)
        n = len(grid)
        for i in range(n):
            for j in range(n):
                freq[grid[i][j]] += 1
        
        repeated = 0
        missing = 0
        for i in range(1, n * n + 1):
            if freq[i] == 0:
                missing = i
            if freq[i] == 2:
                repeated = i
                
        return [repeated, missing]