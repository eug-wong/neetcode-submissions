class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbours = defaultdict(list)
        for s, d in edges:
            neighbours[s].append(d)
            neighbours[d].append(s)
        
        def getHeight(root):
            nonlocal visited
            visited.add(root)
            
            res = 0
            for neighbour in neighbours[root]:
                if neighbour not in visited:
                    res = max(res, getHeight(neighbour))
            
            return res + 1
        
        res = []
        min_height = float('inf')
        for e in range(n):
            visited = set()
            height = getHeight(e)
            if height < min_height:
                min_height = height
                res = [e]
            elif height == min_height:
                res.append(e)
        
        
        return res
        
