class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = Counter(s)
        odds = 0
        for v in freq.values():
            odds += v % 2
        
        return odds <= 1