class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        mapping = {}
        for k, v in zip(x, y):
            if k in mapping:
                mapping[k] = max(mapping[k], v)
            else:
                mapping[k] = v
        
        heap = []
        for v in mapping.values():
            heapq.heappush(heap, v)
            if len(heap) > 3:
                heapq.heappop(heap)
        
        return sum(heap) if len(heap) > 2 else -1