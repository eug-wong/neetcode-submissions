class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        for k, v in trust:
            indegree[v] += 1
            outdegree[k] += 1
        
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        
        return -1