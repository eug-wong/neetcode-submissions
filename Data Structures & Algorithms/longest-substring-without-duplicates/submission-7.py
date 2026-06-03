class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        l, r = 0, 1
        seen.add(s[0])
        longest = 1
        # expand window if not yet seen
        # if already seen, shrink window from left until no longer duplicates

        while r < len(s):
            while l <= r and s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            longest = max(longest, r - l + 1)
            seen.add(s[r])
            r += 1

        return longest