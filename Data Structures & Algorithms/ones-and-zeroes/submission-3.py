class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        freqs = []
        for s in strs:
            counts = Counter(s)
            freqs.append([counts["0"], counts["1"]])

        def recurse(i, m, n):
            nonlocal memo
            nonlocal freqs
            if i == len(strs):
                return 0
            
            if m == 0 and n == 0:
                return 0
            
            if (i, m, n) in memo:
                return memo[(i, m, n)]
            
            freq = freqs[i]

            res = recurse(i + 1, m, n)
            if m - freq[0] >= 0 and n - freq[1] >= 0:
                res = max(res, 1 + recurse(i + 1, m - freq[0], n - freq[1]))
            
            memo[(i, m, n)] = res
            
            return res
        
        return recurse(0, m, n)