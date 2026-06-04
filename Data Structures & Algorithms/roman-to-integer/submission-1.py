class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                   'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        l, r = 0, 0
        res = 0
        while r < len(s):
            while r < len(s) and s[l: r + 1] in mapping.keys():
                r += 1
            
            res += mapping[s[l: r]]
            l = r
        
        return res
