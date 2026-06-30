class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        adj = defaultdict(list)

        for s, d in edges:
            indegree[d] += 1
            adj[s].append(d)
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                res.append(cur)

                for nei in adj[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        
        return res if len(res) == n else []