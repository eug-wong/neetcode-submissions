class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        mapping = defaultdict(int)
        for k, v in zip(x, y):
            mapping[k] = max(mapping[k], v)
        
        heap = []
        heapq.heapify(heap)
        for v in mapping.values():
            heapq.heappush(heap, v)

            if len(heap) > 3:
                heapq.heappop(heap)
        
        return sum(heap) if len(heap) > 2 else -1