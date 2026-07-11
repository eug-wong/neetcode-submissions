class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def recurse(i, j):
            nonlocal memo
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            
            if (i, j) in memo:
                return memo[(i, j)]

            res = float('inf')
            if word1[i] == word2[j]:
                res = min(res, recurse(i + 1, j + 1))
            else:
                res = min(res, recurse(i + 1, j + 1), recurse(i, j + 1), recurse(i + 1, j)) + 1
            
            memo[(i, j)] = res
            
            return memo[(i, j)]

        return recurse(0, 0)

            