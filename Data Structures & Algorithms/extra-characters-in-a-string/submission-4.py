class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        memo = {}
        def recurse(i):
            nonlocal dictionary
            # choose to replace here
            if i == len(s):
                return 0
            
            if i in memo:
                return memo[i]
            
            # choose to continue, not replace (incurs 1 extra char)
            res = 1 + recurse(i + 1)

            # otherwise, choose ot replace starting at i
            for j in range(i, len(s)):
                if s[i: j + 1] in dictionary:
                    res = min(res, recurse(j + 1))

            memo[i] = res
            return res
        
        return recurse(0)
