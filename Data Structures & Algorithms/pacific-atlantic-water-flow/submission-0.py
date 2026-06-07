class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def isValid(i, j):
            return i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0])
        
        def dfs(i, j, ocean):
            if not isValid or (i, j) in ocean:
                return
            
            ocean.add((i, j))

            if isValid(i + 1, j) and heights[i + 1][j] >= heights[i][j]:
                dfs(i + 1, j, ocean)
            
            if isValid(i - 1, j) and heights[i - 1][j] >= heights[i][j]:
                dfs(i - 1, j, ocean)

            if isValid(i, j + 1) and heights[i][j + 1] >= heights[i][j]:
                dfs(i, j + 1, ocean)
            
            if isValid(i, j - 1) and heights[i][j - 1] >= heights[i][j]:
                dfs(i, j - 1, ocean)

            return
        
        pacific = set()
        atlantic = set()
        for i in range(len(heights)):
            dfs(i, 0, pacific)
            dfs(i, len(heights[0]) - 1, atlantic)

        for j in range(len(heights[0])):
            dfs(0, j, pacific)
            dfs(len(heights) - 1, j, atlantic)

        res = []
        for p in pacific:
            for a in atlantic:
                if p == a:
                    res.append([p[0], a[1]])
        
        return res