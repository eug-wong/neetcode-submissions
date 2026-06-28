class Solution:
    def maxScore(self, s: str) -> int:
        score = Counter(s[1: ])["1"]
        max_score = score
        if s[0] == "1":
            s = s[1: ]
        for n in s[: -1]:
            if n == "0":
                score += 1
            
            if n == "1":
                score -= 1
            
            max_score = max(score, max_score)
        
        return max_score
