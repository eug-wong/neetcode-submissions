class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # technically O(n)... but could be better
        
        freq = {}
        for i, c in enumerate(s):
            freq[c] = i

        size, end = 0, 0
        res = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, freq[c])

            if i == end:
                res.append(size)
                size = 0
                end = 0
        
        return res
