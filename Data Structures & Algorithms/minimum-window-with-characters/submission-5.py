class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1

        window_chars = {}
        l = 0
        res = ""
        have, need = 0, len(freq_t)
        for r in range(len(s)):
            c = s[r]
            if c in t:
                window_chars[c] = window_chars.get(c, 0) + 1
                if window_chars[c] == freq_t[c]:
                    have += 1

            while l <= r and have == need:
                res = s[l: r + 1] if r - l + 1 < len(res) or res == "" else res
                if s[l] in t:
                    window_chars[s[l]] -= 1
                    if window_chars[s[l]] < freq_t[s[l]]:
                        have -= 1
                l += 1
        
        return res
