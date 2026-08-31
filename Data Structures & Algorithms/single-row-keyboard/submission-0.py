class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        loc = {}
        for i, c in enumerate(keyboard):
            loc[c] = i
        
        res = 0
        prev = 0
        for c in word:
            res += abs(loc[c] - prev)
            prev = loc[c]
        
        return res
            