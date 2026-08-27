class Solution:
    def numDecodings(self, s: str) -> int:
        # 10 1 2
        # J  A B
        # 10 12
        # J  L

        cache = {}
        def recurse(i):
            nonlocal cache
            if i >= len(s):
                return 1
            
            # choices
            # if it starts with 1 and ends in 0123456789 or 2 and ends in 0123456:
            # we can consider next letter
            # if it starts with 0, we return 0
            # else, accept by itself
            if i in cache:
                return cache[i]

            res = 0
            if s[i] == "0":
                return 0

            if (i < len(s) - 1
                and ((s[i] == "1" and s[i + 1] in "0123456789")
                or (s[i] == "2" and s[i + 1] in "0123456"))):
                res += recurse(i + 2)

            res += recurse(i + 1)
            cache[i] = res
            
            return res
        
        return recurse(0)