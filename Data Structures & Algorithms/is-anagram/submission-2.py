class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            freq1[s[i]] = freq1.get(s[i], 0) + 1
            freq2[t[i]] = freq2.get(t[i], 0) + 1
        
        return freq1 == freq2