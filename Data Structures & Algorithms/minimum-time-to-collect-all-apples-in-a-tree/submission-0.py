class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        def dfs(vertex):
            nonlocal visited
            if vertex in visited:
                return 0

            visited.add(vertex)

            res = 0
            for nei in adj[vertex]:
                if nei not in visited:
                    t = dfs(nei)
                    if t > 0 or hasApple[nei]:
                        res += t + 2
                
            return res
        
        visited = set()
        return dfs(0)
            