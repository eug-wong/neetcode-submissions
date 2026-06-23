class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        mapping = defaultdict(int)
        for k, v in zip(x, y):
            mapping[k] = max(mapping[k], v)
        
        max_sum = -1
        for k1, v1 in mapping.items():
            for k2, v2 in mapping.items():
                for k3, v3 in mapping.items():
                    if k1 != k2 and k2 != k3 and k3 != k1:
                        max_sum = max(max_sum, v1 + v2 + v3)
        
        return max_sum