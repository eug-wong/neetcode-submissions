class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(list)
        trusted_by = defaultdict(list)
        for k, v in trust:
            trusts[k].append(v)
            trusted_by[v].append(k)
        
        for i in range(1, n + 1):
            if i in trusts and trusts[i]:
                continue
            
            if i in trusted_by and len(trusted_by[i]) == n - 1 and i not in trusted_by[i]:
                return i
        
        return -1