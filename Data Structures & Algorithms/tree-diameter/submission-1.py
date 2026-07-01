class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # bfs to find the farthest from any node
        # then bfs backwards to find the furthest from that node
        # guaranteed to find diameter
        # O(v + e) or O(n) for # of edges basically!
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        if not edges:
            return 0

        q = deque([edges[0][0]])
        visited = set()
        order = []
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                
                visited.add(cur)
                order.append(cur)
                for nei in adj[cur]:
                    if nei not in visited:
                        q.append(nei)
    
        q = deque([order[-1]])
        visited = set()
        dist = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                
                visited.add(cur)
                for nei in adj[cur]:
                    if nei not in visited:
                        q.append(nei)
            
            dist += 1

        return dist - 1 if dist > 0 else 0