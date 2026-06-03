class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = [x * -1 for x in nums]
        heapq.heapify(largest)
        res = -1
        for _ in range(k):
            res = heapq.heappop(largest)
        
        return res * -1
