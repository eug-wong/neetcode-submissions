class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents = [x for x in range(n)]
        heights = [1] * n

        def find_parent(n):
            cur = parents[n]
            while cur != parents[cur]:
                parents[cur] = parents[parents[cur]]
                cur = parents[cur]
            return cur
        
        res = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    par_1, par_2 = find_parent(i), find_parent(j)
                    if par_1 == par_2:
                        continue
                    res -= 1
                    if heights[par_1] >= heights[par_2]:
                        parents[par_2] = par_1
                        heights[par_2] += heights[par_1]
                    else:
                        parents[par_1] = par_2
                        heights[par_1] += heights[par_2]
        
        return res
