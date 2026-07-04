class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        l, r = 0, 0
        longest = 0
        while r < len(s):
            freq[s[r]] += 1
            while l <= r and freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest