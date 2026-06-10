class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            
            if (i, j) in visited:
                return
            
            if grid[i][j] == "0":
                return
            
            visited.add((i, j))

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

            return
        
        islands = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] != "0":
                    dfs(i, j)
                    islands += 1
        
        return islands