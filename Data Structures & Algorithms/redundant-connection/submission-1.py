class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [1] * (len(edges) + 1)
        par = [i for i in range(len(edges) + 1)]

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(s, d):
            p1, p2 = find(s), find(d)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True
        
        for edge in edges:
            s, d = edge
            if not union(s, d):
                return edge
