class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isValid(freq1, freq2):
            invalid = False
            for key in freq1.keys():
                if not (freq1[key] <= freq2[key]):
                    invalid = True
            
            return not invalid


        if len(t) > len(s):
            return ""
        
        freq1 = defaultdict(int)
        for c in t:
            freq1[c] += 1
        
        freq2 = defaultdict(int)
        l, r = 0, 0
        res = "SUPERUNCOMMONANDUNLIKELYSTRING"

        while r < len(s):
            freq2[s[r]] += 1
            if isValid(freq1, freq2):
                while l <= r and isValid(freq1, freq2):
                    if len(res) > r - l + 1:
                        res = s[l: r + 1]
                    freq2[s[l]] -= 1
                    l += 1
            
            r += 1
        
        return res if res != "SUPERUNCOMMONANDUNLIKELYSTRING" else ""