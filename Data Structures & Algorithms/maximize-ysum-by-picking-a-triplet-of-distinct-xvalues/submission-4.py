class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        mapping = {}
        for k, v in zip(x, y):
            if k in mapping:
                mapping[k] = max(mapping[k], v)
            else:
                mapping[k] = v
        
        return sum(sorted(mapping.values())[::-1][: 3]) if len(mapping) > 2 else -1