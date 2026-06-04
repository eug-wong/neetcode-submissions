class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def backtrack(i, j):
            nonlocal memo
            if i == len(text1):
                return 0
            
            if j == len(text2):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            matches = 0
            if text1[i] == text2[j]:
                matches = 1 + backtrack(i + 1, j + 1)
            else:
                matches = max(backtrack(i + 1, j), backtrack(i, j + 1))

            memo[(i, j)] = matches
            return matches
    
        return backtrack(0, 0)