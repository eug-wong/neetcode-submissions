class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        l, r = 0, 0
        check = set()
        res = []
        while r < len(s):
            freq[s[r]] -= 1
            check.add(s[r])
            
            finished = True
            for c in check:
                if freq[c] != 0:
                    finished = False
            
            if finished:
                res.append(r - l + 1)
                l = r + 1
                check.clear()

            r += 1
        
        return res
