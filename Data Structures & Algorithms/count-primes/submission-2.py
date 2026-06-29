class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        sieve = [True] * (n)
        sieve[0], sieve[1] = False, False
        p = 2

        while p * p <= n:
            if sieve[p]:
                for i in range(p * p, n, p):
                    sieve[i] = False
            p += 1
            
        return sieve.count(True)