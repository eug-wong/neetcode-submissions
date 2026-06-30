class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [x for x in range(n)]
        h = [1] * n

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        for edge in edges:
            s, d = edge
            rep_s, rep_d = find(s), find(d)
            if rep_s == rep_d:
                continue
            if h[s] > h[d]:
                par[rep_d] = rep_s
                h[rep_d] += h[s]
            else:
                par[rep_s] = rep_d
                h[rep_s] += h[d]

        components = 0
        for i, p in enumerate(par):
            if p == i:
                components += 1

        return components
        