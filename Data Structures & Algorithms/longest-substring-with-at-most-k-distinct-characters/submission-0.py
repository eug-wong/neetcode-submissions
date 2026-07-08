class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        seen = set()
        longest = 0
        l, r = 0, 0
        while r < len(s):
            freq[s[r]] += 1
            seen.add(s[r])
            while len(seen) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    seen.remove(s[l])
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
            
        return longest