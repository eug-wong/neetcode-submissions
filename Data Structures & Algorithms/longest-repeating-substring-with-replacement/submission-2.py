class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        out = 0
        counts = {}

        i = 0
        for j in range(len(s)):
            counts[s[j]] = counts.get(s[j], 0) + 1
            if (j - i + 1) - max(counts.values()) > k:
                counts[s[i]] -= 1
                i += 1
            out = max(out, j - i + 1)
            print(out)
        
        return out