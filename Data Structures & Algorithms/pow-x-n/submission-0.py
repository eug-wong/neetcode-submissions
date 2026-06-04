class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for _ in range(n):
            res *= x
        
        if n < 0:
            for _ in range(-n):
                res *= 1/x

        return res