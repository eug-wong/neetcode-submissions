class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        res = []
        nums = deque(nums)
        cur = 0
        while nums:
            cur = nums.popleft()
            if lower == cur:
                lower += 1
                continue
            
            res.append([lower, cur - 1])
            lower = cur + 1
        
        if cur + 1 <= upper:
            res.append([cur + 1, upper])
        
        return res