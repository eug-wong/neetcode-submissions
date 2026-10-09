class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counts = Counter(s)
        n = len(s)
        res = "1"
        counts["1"] -= 1
        res = "0" * counts["0"] + res
        res = "1" * counts["1"] + res
        return res
