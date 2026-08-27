class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) >= len(text2):
            text1, text2 = text2, text1
        
        cache = {}
        def recurse(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            res = 0
            # case 1: we match
            if text1[i] == text2[j]:
                res = max(res, recurse(i + 1, j + 1) + 1)
            # case 2: we don't match, increment j or i
            res = max(res, recurse(i, j + 1))
            res = max(res, recurse(i + 1, j))
            cache[(i, j)] = res
            return res
        
        return recurse(0, 0)