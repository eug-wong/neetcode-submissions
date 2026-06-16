class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mapping = defaultdict(list)
        for v, e in zip(values, equations):
            mapping[e[0]].append([e[1], v])
            mapping[e[1]].append([e[0], 1/v])
        
        def dfs(start, end, cur, visited):
            if start == end:
                return cur
            
            if start in visited:
                return -1
            
            visited.add(start)
            
            res = -1
            for adj, v in mapping[start]:
                res = max(res, dfs(adj, end, cur * v, visited))

            return res
        
        res = []
        for q in queries:
            if q[0] in mapping and q[1] in mapping:
                visited = set()
                res.append(dfs(q[0], q[1], 1, visited))
            else:
                res.append(-1)
        
        return res
