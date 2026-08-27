class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def recurse(i):
            if i == len(s):
                return True
            
            if i in cache:
                return cache[i]
            
            res = False
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    res = res or recurse(i + len(word))
            
            cache[i] = res
            return res
        
        return recurse(0)
