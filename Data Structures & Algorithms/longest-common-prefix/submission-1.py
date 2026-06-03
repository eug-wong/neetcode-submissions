class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = [len(s) for s in strs]
        shortest = min(lengths)
        cur = ""
        for i in range(shortest + 1):
            prev = cur
            cur = strs[0][0: i]
            for s in strs:
                if s[0: i] != cur:
                    return prev
        
        return cur