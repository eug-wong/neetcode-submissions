class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def hashmaps_match(h1, h2):
            for k, v in h2.items():
                if h1[k] < h2[k]:
                    return False
            return True

        freq1 = defaultdict(int)
        freq2 = Counter(t)
        l, r = 0, 0
        shortest = ""
        while r < len(s):
            freq1[s[r]] += 1
            while hashmaps_match(freq1, freq2):
                if not shortest or len(shortest) > r - l + 1:
                    shortest = s[l: r + 1]
                freq1[s[l]] -= 1
                l += 1

            r += 1
            
        
        return shortest