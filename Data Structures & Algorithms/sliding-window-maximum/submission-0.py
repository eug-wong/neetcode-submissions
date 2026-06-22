class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(0, len(nums) - k + 1):
            heap = [-1 * x for x in nums[i : i + k]]
            heapq.heapify(heap)
            res.append(-1 * heapq.heappop(heap))
        
        return res
